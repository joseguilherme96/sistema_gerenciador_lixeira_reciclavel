import time
from utils.configuracao_esp32 import configuracao
from utils import obter_distancia
from configuracao import LIXEIRA_ESTA_CALIBRADA, PROFUNDIDADE_LIXEIRA

class Calibracao :

    lixeira_esta_calibrada = LIXEIRA_ESTA_CALIBRADA
    profundidade_calibrada = PROFUNDIDADE_LIXEIRA
    profundidade_lixeira_encontrada = 0

    def __init__(self):

        print("Calibração de Profundidade !")
        print()
        print(f'Profundidade atual da lixeira : {getattr(Calibracao,'profundidade_calibrada')} cm \n')

    def get_atribute(self,name):

        return getattr(self,name)
    
    def set_atribute(self,name,value):
        setattr(self, name, value)


    def calibrar_profundidade(self):

        try:

            if LIXEIRA_ESTA_CALIBRADA:

                return True

            print("Escolha uma das opções : 1 - Calibrar automaticamente 2 - Inserir Manualmente")
            opcao = input()

            print()

            if(opcao == '1'):

                while True:
                    
                    profundidade_encontrada = obter_distancia.get_distancia_entre_sensor_lixo()
                    print(f"Profundidade Lixeira Encontrada : {profundidade_encontrada} (ctrl+c) para confirmar calibramento.")

                    self.set_atribute(Calibracao,'profundidade_encontrada',profundidade_encontrada)
                    self.set_atribute(Calibracao,'profundidade_calibrada',profundidade_encontrada)
                        
                    time.sleep(3)

            elif opcao == '2':

                print()
                profundidade_encontrada = input("Digite a profundidade da lixeira : \n")
                self.set_atribute(Calibracao,'profundidade_encontrada',profundidade_encontrada)
                self.set_atribute(Calibracao,'profundidade_calibrada',profundidade_encontrada)
                configuracao.salvar_profundidade_lixeira(Calibracao)


            print()
            print("Profundidade Calibrada da lixeira :", getattr(Calibracao,'profundidade_calibrada'),' cm')
            self.set_atribute(Calibracao,'lixeira_esta_calibrada',True)
            
            return True



        except KeyboardInterrupt as e:

            print()
            self.set_atribute(Calibracao,'lixeira_esta_calibrada',True)
            print("Profundidade Calibrada da lixeira :", getattr(Calibracao,'profundidade_calibrada'),' cm')
            configuracao.salvar_profundidade_lixeira(Calibracao)
            return  True

        except Exception as e:

            print("Falha ao calibrar ! \n")
            return  False

    

