# Configurações ESP32
from configuracao import ESTAGIO_LIXEIRA_NIVEL_1,ESTAGIO_LIXEIRA_NIVEL_2,ESTAGIO_LIXEIRA_NIVEL_3,ESTAGIO_LIXEIRA_NIVEL_4,ESTAGIO_LIXEIRA_NIVEL_5,PONTO_LIXO_ID,LIXEIRA_ID

# Services
from services.informativo_service import informar_nivel_lixeira
from services.lixeira_service import atualizar_lixeira
from services.wifi_service import conectar_wifi, verificar_conectividade_wifi
from services.log_service import cadastrar_logs,gravar_logs_em_arquivo_no_esp32

# Classes
import time 

# Utils 
from utils.obter_distancia import get_distancia_entre_sensor_lixo
from utils.converte_nivel_lixeira_em_porcentagem import calcular_nivel_lixeira_em_porcentagem
from utils.calibrar_lixeira import Calibracao

import time

# store
from store.log import log_message,clear_log_message

log_message('---------------------------------Log ESP32--------------------------------------------',"SUCCESS")
log_message("Iniciando execucao ESP32 !","SUCCESS")

conectar_wifi()

guardar_ultimo_nivel_lixeira_valido = 0
ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior = False
lixeira_esta_aberta = False
distancia_entre_sensor_lixo_lida_anteriormente = 0
estagio = 1 # 1 - Lixeira Fechada, 2 - Lixeira
contador =0
contador_tempo_lixeira_aberta = 0
estagio_lixeira_nivel_anterior_enviado = 0

try:

    while True:

        verificar_conectividade_wifi()

        # Grava Logs no própio dispositivo
        gravar_logs_em_arquivo_no_esp32()

        # Cadastra Logs no servidor
        cadastrar_logs()

        # Limpa logs gerados
        clear_log_message()

        print()

        log_message('---------------------------------Log ESP32--------------------------------------------',"SUCCESS")
        log_message(f'Ponto de lixo ID : {PONTO_LIXO_ID} Lixeira ID : {LIXEIRA_ID}',"SUCCESS")

        distancia_entre_sensor_lixo_atual = get_distancia_entre_sensor_lixo()
        mensagem = f'Distancia entre o sensor e o lixo : {distancia_entre_sensor_lixo_atual} cm'
        log_message(mensagem,"SUCCESS")

        profundidade_lixeira = Calibracao.get_atribute(Calibracao,'profundidade_calibrada')

        if not Calibracao.get_atribute(Calibracao,'lixeira_esta_calibrada'):

            mensagem = "Sensor esta configurado para ser calibrado novamente! \n"
            log_message(mensagem,"SUCCESS")
            
            time.sleep(1)
            
            if(not Calibracao.calibrar_profundidade(Calibracao)):

                continue

            profundidade_lixeira = int(Calibracao.get_atribute(Calibracao,'profundidade_calibrada'))
        

        nivel_lixeira = calcular_nivel_lixeira_em_porcentagem(distancia_entre_sensor_lixo_atual)
        altura_lixo = (nivel_lixeira/100) * profundidade_lixeira

        mensagem = f'Altura lixo : {altura_lixo} cm'
        log_message(mensagem,"SUCCESS")

        mensagem = f'Nivel lixeira : {nivel_lixeira} %'
        log_message(mensagem,"SUCCESS")


        mensagem = f'Estagio lixeira : {estagio}'
        log_message(mensagem,"SUCCESS")


        mensagem= f'Mao aproximada : {distancia_entre_sensor_lixo_atual}'
        log_message(mensagem,"SUCCESS")
        
        # Guarda valor distância entre sensor e lixo na primeira execução, pois é quando a lixeira está fechada, e serve como base para identificar se a lixeira foi aberta caso o valor seja maior que o valor lido na primeira execução
        if contador == 0:
                
                distancia_entre_sensor_lixo_lida_anteriormente = distancia_entre_sensor_lixo_atual

        contador +=1
 
        # Sensor pode variar 2cm para cima ou para baixo
        variacao_sensor = 2
        minimo_distancia_atual_em_relacao_a_medicao_anterior = distancia_entre_sensor_lixo_lida_anteriormente - variacao_sensor
        maximo_distancia_atual_em_relacao_a_medicao_anterior = distancia_entre_sensor_lixo_lida_anteriormente + variacao_sensor
        distancia_atual_esta_dentro_da_tolerancia_em_relacao_a_anterior = (minimo_distancia_atual_em_relacao_a_medicao_anterior < distancia_entre_sensor_lixo_atual) and (distancia_entre_sensor_lixo_atual < maximo_distancia_atual_em_relacao_a_medicao_anterior)

        

        if distancia_atual_esta_dentro_da_tolerancia_em_relacao_a_anterior and estagio !=2:

            mensagem = 'Lixeira esta Fechada !'
            log_message(mensagem,"SUCCESS")

            ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior = False
            lixeira_esta_aberta = False
            distancia_entre_sensor_lixo_lida_anteriormente = distancia_entre_sensor_lixo_atual
            guardar_ultimo_nivel_lixeira_valido = nivel_lixeira
            contador_tempo_lixeira_aberta =0
            estagio = 1 # Lixeira Fechada


            if nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_1:

                mensagem= "Lixeira esta vazia !"
                log_message(mensagem,"SUCCESS")

                if estagio_lixeira_nivel_anterior_enviado == 1:
                    mensagem = 'Nao enviado informacao para o servidor novamente devido já ter sido enviado na leitura anterior...'
                    log_message(mensagem,"SUCCESS")

                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 1

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_2:

                mensagem = "Lixeira com nivel baixo !"
                log_message(mensagem)
                
                if estagio_lixeira_nivel_anterior_enviado == 2:
                    mensagem = 'Nao enviado informacao para o servidor novamente devido já ter sido enviado na leitura anterior...'
                    log_message(mensagem,"SUCCESS")
                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 2

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_3:

                mensagem = "Lixeira esta com nivel quase na metade !"
                log_message(mensagem,"SUCCESS")

                if estagio_lixeira_nivel_anterior_enviado == 3:
                    mensagem = 'Nao enviado informacao para o servidor novamente devido ja ter sido enviado na leitura anterior...'
                    log_message(mensagem,"SUCCESS")
                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 3

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_4:

                mensagem= "Lixeira quase cheia !"
                log_message(mensagem,"SUCCESS")
                
                if estagio_lixeira_nivel_anterior_enviado == 4:

                    log_message("Nao enviado informacao para o servidor novamente devido ja ter sido enviado na leitura anterior...","SUCCESS")
                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 4
            
            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_5:

                mensagem= "Lixeira esta cheia !"
                log_message(mensagem)
                
                if estagio_lixeira_nivel_anterior_enviado == 5:

                    log_message("Nao enviado informacao para o servidor novamente devido ja ter sido enviado na leitura anterior...","SUCCESS")
                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 5

        else:

            log_message("Lixeira esta aberta !","SUCCESS")
            lixeira_esta_aberta = True
            contador_tempo_lixeira_aberta +=1

            estagio = 2 # Lixeira aberta

            retorno = False
            
            if not ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior:
                
                retorno = atualizar_lixeira(guardar_ultimo_nivel_lixeira_valido,esta_aberta=lixeira_esta_aberta)

            if retorno:

                informar_nivel_lixeira(nivel_lixeira=guardar_ultimo_nivel_lixeira_valido, observacao="Lixeira esta aberta !")
            
                ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior = True

            log_message(f" Tempo lixeira aberta : {contador_tempo_lixeira_aberta}","SUCCESS")

            # Se passar 10 segundos e a lixeira ainda não foi fechada....fecha automaticamente lixeira
            if distancia_atual_esta_dentro_da_tolerancia_em_relacao_a_anterior or contador_tempo_lixeira_aberta >=10 and lixeira_esta_aberta:
            
                log_message("Lixeira foi fechada !","SUCCESS")
                distancia_entre_sensor_lixo_lida_anteriormente = distancia_entre_sensor_lixo_atual
                estagio=1
                lixeira_esta_aberta = False

                mensagem = "Lixeira Fechada !"
                log_message(mensagem,"SUCCESS")
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)

            time.sleep(2)

except KeyboardInterrupt as e:

    log_message("A execucao do script no esp32 foi encerrada !","SUCCESS")
    cadastrar_logs()

except Exception as e:

    log_message(f'Falha na execucao : {str(e)}',"ERROR")
    cadastrar_logs()

    
