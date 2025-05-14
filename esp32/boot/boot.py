# Configurações ESP32
from configuracao import DISTANCIA_LIXEIRA_ABERTA_SEM_PESSOA_OU_OBJETO_NA_FRENTE
from configuracao import ESTAGIO_LIXEIRA_NIVEL_1,ESTAGIO_LIXEIRA_NIVEL_2,ESTAGIO_LIXEIRA_NIVEL_3,ESTAGIO_LIXEIRA_NIVEL_4,ESTAGIO_LIXEIRA_NIVEL_5

# Services
from services.informativo_service import informar_nivel_lixeira
from services.lixeira_service import atualizar_nivel_lixeira
from services.wifi_service import conectar_wifi, verificar_conectividade_wifi

# Classes
import time 

# Utils 
from utils.obter_distancia import get_distancia_entre_sensor_lixo
from utils.converte_nivel_lixeira_em_porcentagem import calcular_nivel_lixeira_em_porcentagem
from utils.calibrar_lixeira import Calibracao

conectar_wifi()

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
        
        nivel_lixeira = calcular_nivel_lixeira_em_porcentagem(distancia_entre_sensor_lixo)

        if distancia_entre_sensor_lixo >= DISTANCIA_LIXEIRA_ABERTA_SEM_PESSOA_OU_OBJETO_NA_FRENTE:

            print("Lixeira Aberta !")

        elif distancia_entre_sensor_lixo >= profundidade_lixeira:

            print("Lixeira aberta com pessoa ou objeto na frente da lixeira  !")

        elif distancia_entre_sensor_lixo <= profundidade_lixeira:

            print('Nível Lixeira : ',nivel_lixeira,'%')

            if nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_1:

                print("Lixeira esta vazia !")
                retorno = atualizar_nivel_lixeira(nivel_lixeira)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira)

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_2:

                print("Lixeira com nivel baixo ! ")
                retorno = atualizar_nivel_lixeira(nivel_lixeira)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira)

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_3:

                print("Lixeira esta com nivel na metade !")
                retorno = atualizar_nivel_lixeira(nivel_lixeira)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira)

            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_4:

                print("Lixeira quase cheia !")
                retorno = atualizar_nivel_lixeira(nivel_lixeira)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira)
            
            elif nivel_lixeira <= ESTAGIO_LIXEIRA_NIVEL_5:

                print("Lixeira esta cheia !")
                retorno = atualizar_nivel_lixeira(nivel_lixeira)

                if retorno:

                    informar_nivel_lixeira(nivel_lixeira)

            
        print()

        time.sleep(1)

except KeyboardInterrupt as e:

    print("A execução foi encerrada !")

except Exception as e:

    print("Falha na execução",str(e))

    
