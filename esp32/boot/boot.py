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
lixeira_esta_aberta = None

try:

    while True:

        verificar_conectividade_wifi()

        distancia_entre_sensor_lixo = get_distancia_entre_sensor_lixo()
        print("Distancia entre o sensor e o lixo : ",distancia_entre_sensor_lixo,' cm')

        profundidade_lixeira = Calibracao.__getattribute__(Calibracao,'profundidade_calibrada')

        if not Calibracao.__getattribute__(Calibracao,'lixeira_esta_calibrada'):

            print("Sensor está configurado para ser calibrado novamente! \n")
            time.sleep(1)
            
            if(not Calibracao.calibrar_profundidade()):

                continue

            profundidade_lixeira = int(Calibracao.__getattribute__(Calibracao,'profundidade_calibrada'))
        

        if distancia_entre_sensor_lixo >= profundidade_lixeira:


            print("Lixeira Aberta !")
            lixeira_esta_aberta = True
            if not ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior:
                
                retorno = atualizar_lixeira(guardar_ultimo_nivel_lixeira_valido,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira=guardar_ultimo_nivel_lixeira_valido, observacao="Lixeira Aberta !")

            ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior = True

        elif distancia_entre_sensor_lixo <= profundidade_lixeira:

            ja_foi_informado_sobre_lixeira_aberta_no_loop_anterior = False
            lixeira_esta_aberta = False

            nivel_lixeira = calcular_nivel_lixeira_em_porcentagem(distancia_entre_sensor_lixo)
            guardar_ultimo_nivel_lixeira_valido = nivel_lixeira

            print('Nível Lixeira : ',nivel_lixeira,'%')

            if nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_1:

                mensagem= "Lixeira esta vazia !"
                print(mensagem)
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_2:

                mensagem = "Lixeira com nivel baixo !"
                print(mensagem)
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_3:

                mensagem = "Lixeira esta com nivel na metade !"
                print(mensagem)
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_4:

                mensagem= "Lixeira quase cheia !"
                print(mensagem)
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)
            
            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_5:

                mensagem= "Lixeira está cheia !"
                print(mensagem)
                retorno = atualizar_lixeira(nivel_lixeira,esta_aberta=lixeira_esta_aberta)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira,observacao=mensagem)


            
        print()

        time.sleep(1)

except KeyboardInterrupt as e:

    print("A execução foi encerrada !")

except Exception as e:

    print("Falha na execução",str(e))

    
