## Arquivo reponsável por realizar a configuração inicial para ESP32, trazendo maior agilidade na configuração e implementação do boot.

## Ao executar o boot.py este script será carregado automaticamente caso ainda o boot.py esteja em modo de configuração.

###

## Caso contrário, caso queira configurar novamente, tecle Ctrl + Z, e escolha a opção 2. Automaticamente você será levado para configuração do boot, 
## onde poderá realizar o processo de configuração de maneira simplificada.

###

## 

## Os recursos de configuração que este script oferece :

### Possibilidade de configurar o o boot para rodar em modo simulação no pc...sem que o esp32 esteja ainda o ESP32 esteja processando o script.
### Possibilidade de configurar o boot para rodar direto no ESP32.
### Permite configurar ligação dos pinos do ESP32 com os pinos do sensor TRIGGER_PIN/ECHO_PIN de maneira prática.
### Permite definir estagios de lixo da lixeira, ou seja ajustando os avisos de acordo que frequência que a lixeira enchida.

# Exemplo :

# Nivel 1 = 0%
# Nivel 2 = 25%
# NIvel 3 = 50%
# Nivel 4 = 75%
# Nivel 5 = 100%

# Os valores podem ser ou para mais ou para menos no intervalo de 0 a 100 facilitando em que momento os avisos de mudanças do nivel de lixo serão disparados pelo ESP32.

### Permite definir o PONTO_LIXO_ID que o ESP32 está monitorando
### Permite definir a LIXEIRA_ID que o ESP32 está monitorando
### Permite definir o GRUPO_ID que o ESP32 está monitorando

# Permite definir o endereço do servidor que o ESP32 irá se conectar e enviar os dados.
# Permite definir o nome da rede que o ESP32 irá se conectar
# Permite definir a senha da rede que o ESP32 irá se conectar
# Pemite denifir o numero de tentativas na rede
# Permite definir um ID único para o ESP32 diferenciando dos demais.

# Por fim o boot conta com este arquivo de configuraração que visa facilitar a implementação do boot em um ESP32 para já começar a coletar dados e enviar para o servidor
# sitema para serem analisados..

import time
import sys
from utils.input_cli import is_number_or_error,is_option_invalid
from store.log import log_message


class configuracao:

    nome_arquivo ='configuracao.py'

    def __init__(self, CONFIGURAR_NOVAMENTE = False):

        try:

            try:

                from configuracao import CONFIGURAR

            except:

                CONFIGURAR = True

            if CONFIGURAR or CONFIGURAR_NOVAMENTE:

                opcao = input("Deseja realizar configuração no ESP32 ou utilizar configurações já salvas ? 1 - Utilizar configuração já salvas, 2 - Configurar : ")
                print()
                    
                is_number_or_error(opcao)
                is_option_invalid(opcao,available_options_cli=[1,2])

                if opcao == '1':

                    self.encerrar_configuracao()
                    

                if opcao == '2':

                    self.criar_arquivo()

                    print("Bem vindo a configuração automática do boot para facilitar no processo de implementação no ESP32 !")

                    print()

                    self.comentar("Arquivo gerado automaticamente com base nos dados de entrada configurado pelo terminal facilitando a implementação do ESP32 na lixeira.")
                    self.pular_linha()
                    self.comentar("Configuração do dispositivo")
                    self.pular_linha()
                    self.configurar_modo_execucao()
                    self.pular_linha()
                    self.configurar_ligacao_pinos_sensores_com_pinos_esp32()
                    self.pular_linha()
                    self.configurar_estagios_lixeira()
                    self.pular_linha()
                    self.configurar_dados_de_monitoramento()
                    self.pular_linha()
                    self.configurar_endereco_servidor()
                    self.pular_linha()
                    self.configurar_dados_da_rede_que_o_esp32_estara_conectado()
                    self.pular_linha()
                    self.configurar_identificacao_esp32()
                    self.pular_linha()
                    self.inicializar_variaveis()
                    self.pular_linha()
                    self.encerrar_configuracao()
                    print()
                    self.pular_linha()
                    self.exibir_arquivo_de_configuracao()

                time.sleep(3)

            if not CONFIGURAR and not CONFIGURAR_NOVAMENTE:
                
                self.exibir_arquivo_de_configuracao()
                time.sleep(3)

        except KeyboardInterrupt as e:

            print()
            print("A configuração foi encerrada !")
            self.adicionar_linha_no_arquivo(f"CONFIGURAR = {True}")
            sys.exit()

        except Exception as e:
            print(f"{str(e)}")
            self.__init__()

        

    def criar_arquivo(self):

        with open(f'{self.nome_arquivo}',"w") as arquivo:
            pass
        

    def adicionar_linha_no_arquivo(self,linha):

        with open(f'{self.nome_arquivo}', "a") as arquivo:
            arquivo.write(linha)

        self.pular_linha()

    def pular_linha(self):

        with open(f'{self.nome_arquivo}', "a") as arquivo:
            arquivo.write("\n")

    def comentar(self,comentario):

        with open(f'{self.nome_arquivo}', "a") as arquivo:
            arquivo.write(f"# {comentario}")
        
        self.pular_linha()

    def configurar_modo_execucao(self):

        try:

            MODO_ID = input("Digite a opção que deseja que seja executado o script : 1 -  Modo Simulação no pc, 2- Modo ESP32 execução do script direto no ESP32 : ")

            is_number_or_error(MODO_ID)
            is_option_invalid(int(MODO_ID),[1,2])

            MODO_SIMULACAO = False if MODO_ID == '1' else True

            self.comentar("Permite que seja executado via cli sem sensor")
            self.adicionar_linha_no_arquivo(f"SCRIPT_SENDO_EXECUTADO_NO_ESP32 = {MODO_SIMULACAO}")
        
        except Exception:

            self.configurar_modo_execucao()

        

    def configurar_ligacao_pinos_sensores_com_pinos_esp32(self):

        try:

            self.comentar("Ligação dos pinos do ESP32 com o sensor HCSR04")
            TRIGGER_PIN = input("Digite o numero do pino ESP32 que foi conectado o TRIGGER_PIN do sensor : ")
            is_number_or_error(TRIGGER_PIN)
            self.adicionar_linha_no_arquivo(f"TRIGGER_PIN = {str(TRIGGER_PIN)}")

            ECHO_PIN = input("Digite o numero do pino ESP32 que foi conectado o ECHO_PIN do sensor : ")
            is_number_or_error(ECHO_PIN)
            self.adicionar_linha_no_arquivo(f"ECHO_PIN = {str(ECHO_PIN)}")
             

        except Exception:

            self.configurar_ligacao_pinos_sensores_com_pinos_esp32()

        

    def configurar_estagios_lixeira(self):

        try:

            for estagio in range(0,int(5)):

                ESTAGIO_LIXEIRA_NIVEL = input(f"Informe o nivel da lixeira no estágio nivel {int(estagio) + 1} : ")

                is_number_or_error(ESTAGIO_LIXEIRA_NIVEL)

                self.adicionar_linha_no_arquivo(f"ESTAGIO_LIXEIRA_NIVEL_{int(estagio) + 1} = {str(ESTAGIO_LIXEIRA_NIVEL)}")

        except Exception:

            self.configurar_estagios_lixeira()


    def configurar_dados_de_monitoramento(self):

        try:

            self.comentar("Informações da Lixeira que está sendo monitorada")
            PONTO_LIXO_ID = input("Informe o PONTO_LIXO_ID que o ESP32 vai monitorar : ")
            is_number_or_error(PONTO_LIXO_ID)
            self.adicionar_linha_no_arquivo(f"PONTO_LIXO_ID = {str(PONTO_LIXO_ID)}")

            LIXEIRA_ID = input("Informe a LIXEIRA_ID que o ESP32 vai monitorar : ")
            is_number_or_error(LIXEIRA_ID)
            self.adicionar_linha_no_arquivo(f"LIXEIRA_ID = {str(LIXEIRA_ID)}")

            GRUPO_ID = input("Informe o GRUPO_ID que o ESP32 vai monitorar : ")
            is_number_or_error(GRUPO_ID)
            self.adicionar_linha_no_arquivo(f"GRUPO_ID = {str(GRUPO_ID)}")

        except Exception:

            self.configurar_dados_de_monitoramento()

    def configurar_endereco_servidor(self):
        
        self.comentar("Base URL do Servidor Flask")
        API_FLASK_BASE_URL = input("Informe o endereço do servidor que o ESP32 irá enviar os dados : ")
        self.adicionar_linha_no_arquivo(f"API_FLASK_BASE_URL = '{str(API_FLASK_BASE_URL)}'")
        self.pular_linha()
        self.configurar_endpoints(API_FLASK_BASE_URL)

    def configurar_endpoints(self,API_FLASK_BASE_URL):

        API_INFORMATIVO_LIXEIRA = f'{API_FLASK_BASE_URL}/cadastrar_informativo_lixeira'
        API_ATUALIZAR_LIXEIRA = f'{API_FLASK_BASE_URL}/atualizar_nivel_lixeira'
        API_LOG=f'{API_FLASK_BASE_URL}/cadastrar_log_esp32'

        self.comentar("ENDPOINTS")
        self.adicionar_linha_no_arquivo(f"API_INFORMATIVO_LIXEIRA = '{str(API_INFORMATIVO_LIXEIRA)}'")
        self.adicionar_linha_no_arquivo(f"API_ATUALIZAR_LIXEIRA = '{str(API_ATUALIZAR_LIXEIRA)}'")
        self.adicionar_linha_no_arquivo(f"API_LOG = '{str(API_LOG)}'")
    
    def configurar_dados_da_rede_que_o_esp32_estara_conectado(self):

        self.comentar("Dados da Rede")
        SSID = input("Informe o nome da rede que o ESP32 estara conectado : ")
        self.adicionar_linha_no_arquivo(f"SSID = '{str(SSID)}'")

        PASSWORD = input("Informe a senha da rede que o ESP32 estara conectado : ")
        self.adicionar_linha_no_arquivo(f"PASSWORD = '{str(PASSWORD)}'")

        NUMERO_TENTATIVAS_CONECTAR_UMA_REDE_WIFI = input("Digite o numero de tentativas ao tentar se conectar a uma rede no ESP32 : ")
        self.adicionar_linha_no_arquivo(f"NUMERO_TENTATIVAS_CONECTAR_UMA_REDE_WIFI = '{NUMERO_TENTATIVAS_CONECTAR_UMA_REDE_WIFI}'")
        self.pular_linha()

    def configurar_identificacao_esp32(self):

        try:

            ID_ESP32 = input("Informe o identificador único para o ESP32 ID_ESP32 : ")
            is_number_or_error(ID_ESP32)
            self.comentar("Identificação ESP32")
            self.adicionar_linha_no_arquivo(f"ID_ESP32 = {ID_ESP32}")
            self.adicionar_linha_no_arquivo(f"ID_INFORMADOR = {2}")
        
        except Exception:

            self.configurar_identificacao_esp32()

    def salvar_profundidade_lixeira(Calibracao):

        profundidade = getattr(Calibracao,'profundidade_encontrada')

        with open(f'{configuracao.nome_arquivo}', "a") as arquivo:
            arquivo.write("\n")
            arquivo.write("#Configuracoes Lixeira \n")
            arquivo.write(f"PROFUNDIDADE_LIXEIRA = {str(profundidade)} \n")
            arquivo.write(f"LIXEIRA_ESTA_CALIBRADA = {True}")
    
    def encerrar_configuracao(self):

        log_message('Configuração finalizada !','SUCCESS')
        self.adicionar_linha_no_arquivo(f"CONFIGURAR = {False}")
    
    def opcoes_dispositivo(self):

        try:

            print()
            interromper_execucao = input("Deseja realmente interromper a execução do script ? 1 - Sim, 2 - Configurar Dispositivo : ")

            is_number_or_error(interromper_execucao)
            is_option_invalid(interromper_execucao,[1,2])

            if int(interromper_execucao) == 1:

                log_message("A execucao do script no esp32 foi encerrada !","SUCCESS")
                sys.exit()
                return 1

            if int(interromper_execucao) == 2:

                return 2
            
        except KeyboardInterrupt as e:

            print()
            log_message("A execucao do script no esp32 foi encerrada !","SUCCESS")
            sys.exit()

        except Exception:
            
            self.opcoes_dispositivo(configuracao)

    def inicializar_variaveis(self):

        # Inicializar variaveis
        self.adicionar_linha_no_arquivo(f"PROFUNDIDADE_LIXEIRA = {1}")
        self.adicionar_linha_no_arquivo(f"LIXEIRA_ESTA_CALIBRADA = {False}")

    def exibir_arquivo_de_configuracao(self):

        print("........................................................Arquivo de configuração ESP32........................................................")
        print()

        with open(f'{self.nome_arquivo}', "r") as arquivo:

            for linha in arquivo:

                if(linha != "\n"):

                    print(linha+".....................................")
                    time.sleep(1)




