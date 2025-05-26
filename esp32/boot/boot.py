# Configurações ESP32
from configuracao import DISTANCIA_LIXEIRA_ABERTA_SEM_PESSOA_OU_OBJETO_NA_FRENTE
from configuracao import ESTAGIO_LIXEIRA_NIVEL_1,ESTAGIO_LIXEIRA_NIVEL_2,ESTAGIO_LIXEIRA_NIVEL_3,ESTAGIO_LIXEIRA_NIVEL_4,ESTAGIO_LIXEIRA_NIVEL_5

# Services
from services.informativo_service import informar_nivel_lixeira
from services.lixeira_service import atualizar_lixeira
from services.wifi_service import conectar_wifi, verificar_conectividade_wifi

# Classes
import time 

# Utils 
from utils.obter_distancia import get_distancia_entre_sensor_lixo
from utils.converte_nivel_lixeira_em_porcentagem import calcular_nivel_lixeira_em_porcentagem
from utils.calibrar_lixeira import Calibracao

import time

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

        distancia_entre_sensor_lixo_atual = get_distancia_entre_sensor_lixo()
        print("Distancia entre o sensor e o lixo : ",distancia_entre_sensor_lixo_atual,' cm')

        profundidade_lixeira = Calibracao.get_atribute(Calibracao,'profundidade_calibrada')

        if not Calibracao.get_atribute(Calibracao,'lixeira_esta_calibrada'):

            print("Sensor está configurado para ser calibrado novamente! \n")
            time.sleep(1)
            
            if(not Calibracao.calibrar_profundidade(Calibracao)):

                continue

            profundidade_lixeira = int(Calibracao.get_atribute(Calibracao,'profundidade_calibrada'))
        

        nivel_lixeira = calcular_nivel_lixeira_em_porcentagem(distancia_entre_sensor_lixo_atual)
        altura_lixo = (nivel_lixeira/100) * profundidade_lixeira

        print("Altura lixo : ", altura_lixo)
        print( "Mão aproximada: ", distancia_entre_sensor_lixo_atual)
        print("Estágio de abertura :", estagio)
        print('Nível Lixeira : ', nivel_lixeira,'%')

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

            print("Lixeira está Fechada !")
            ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior = False
            lixeira_esta_aberta = False
            distancia_entre_sensor_lixo_lida_anteriormente = distancia_entre_sensor_lixo_atual
            guardar_ultimo_nivel_lixeira_valido = nivel_lixeira
            contador_tempo_lixeira_aberta =0
            estagio = 1 # Lixeira Fechada


            if nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_1:

                mensagem= "Lixeira esta vazia !"
                print(mensagem)

                if estagio_lixeira_nivel_anterior_enviado == 1:
                    print("Não enviado informação para o servidor novamente devido já ter sido enviado na leitura anterior...")
                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 1

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_2:

                mensagem = "Lixeira com nivel baixo !"
                print(mensagem)
                
                if estagio_lixeira_nivel_anterior_enviado == 2:
                    print("Não enviado informação para o servidor novamente devido já ter sido enviado na leitura anterior...")
                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 2

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_3:

                mensagem = "Lixeira esta com nivel quase na metade !"
                print(mensagem)

                if estagio_lixeira_nivel_anterior_enviado == 3:
                    print("Não enviado informação para o servidor novamente devido já ter sido enviado na leitura anterior...")
                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 3

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_4:

                mensagem= "Lixeira quase cheia !"
                print(mensagem)
                
                if estagio_lixeira_nivel_anterior_enviado == 4:
                    print("Não enviado informação para o servidor novamente devido já ter sido enviado na leitura anterior...")
                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 4
            
            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_5:

                mensagem= "Lixeira está cheia !"
                print(mensagem)
                
                if estagio_lixeira_nivel_anterior_enviado == 5:
                    print("Não enviado informação para o servidor novamente devido já ter sido enviado na leitura anterior...")
                    time.sleep(2)
                    continue
                
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
                    estagio_lixeira_nivel_anterior_enviado = 5

        else:

            print("Lixeira está aberta !")
            lixeira_esta_aberta = True
            contador_tempo_lixeira_aberta +=1

            estagio = 2 # Lixeira aberta

            retorno = False
            
            if not ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior:
                
                retorno = atualizar_lixeira(guardar_ultimo_nivel_lixeira_valido,esta_aberta=lixeira_esta_aberta)

            if retorno:

                informar_nivel_lixeira(nivel_lixeira=guardar_ultimo_nivel_lixeira_valido, observacao="Lixeira está aberta !")
            
                ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior = True

            print(" Tempo lixeira aberta :", contador_tempo_lixeira_aberta)

            # Se passar 10 segundos e a lixeira ainda não foi fechada....fecha automaticamente lixeira
            if distancia_atual_esta_dentro_da_tolerancia_em_relacao_a_anterior or contador_tempo_lixeira_aberta >=10 and lixeira_esta_aberta:
            
                print("Lixeira foi fechada !")
                distancia_entre_sensor_lixo_lida_anteriormente = distancia_entre_sensor_lixo_atual
                estagio=1
                lixeira_esta_aberta = False

                mensagem = "Lixeira Fechada !"
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)

            time.sleep(2)


        print()
        print()
        print()

except KeyboardInterrupt as e:

    print("A execução foi encerrada !")

except Exception as e:

    print("Falha na execução",str(e))

    
