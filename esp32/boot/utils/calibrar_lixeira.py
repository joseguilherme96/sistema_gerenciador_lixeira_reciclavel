from configuracao import PROFUNDIDADE_LIXEIRA,LIXEIRA_ESTA_CALIBRADA
from utils.obter_distancia import get_distancia_entre_sensor_lixo
import time

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


        opcao = input('Deseja realmente calibrar novamente ? 1 - Sim, 2- Não \n')
        print()

        try:
        
            if opcao == '1':

                print("Escolha uma das opções : 1 - Calibrar automaticamente 2 - Inserir Manualmente")
                opcao = input()

                print()

                if(opcao == '1'):

                    while True:
                        
                        profundidade_encontrada = get_distancia_entre_sensor_lixo()
                        print(f"Profundidade Lixeira Encontrada : {profundidade_encontrada} (ctrl+c) para confirmar calibramento.")

                        self.set_atribute(Calibracao,'profundidade_encontrada',profundidade_encontrada)
                            
                        time.sleep(3)

                elif opcao == '2':

                    print()
                    profundidade_encontrada = input("Digite a profundidade da lixeira : \n")
                    self.set_atribute(Calibracao,'profundidade_encontrada',profundidade_encontrada)

            print()
            print("Profundidade Calibrada da lixeira :", getattr(Calibracao,'profundidade_calibrada'),' cm')
            self.set_atribute(Calibracao,'lixeira_esta_calibrada',True)
            
            return True



        except KeyboardInterrupt as e:

            print()
            self.set_atribute(Calibracao,'lixeira_esta_calibrada',True)
            print("Profundidade Calibrada da lixeira :", getattr(Calibracao,'profundidade_calibrada'),' cm')
            return  True

        except Exception as e:

            print("Falha ao calibrar ! \n")
            return  False
    

