# Arquivo exemplo de configuração
# Ao terminar a configuração do arquivo...renomear arquivo para configuracao.py

# Permite que seja executado no terminal sem ESP32 e Sensor. Os valores serão gerados aleatoriamente para teste.
SCRIPT_SENDO_EXECUTADO_NO_ESP32 = True

# Numeros dos Pinos que o sensor conectou no ESP32 Dxx
TRIGGER_PIN = 5
ECHO_PIN = 18

# Caracteristicas lixeira
PROFUNDIDADE_LIXEIRA = 100
DISTANCIA_LIXEIRA_ABERTA_SEM_PESSOA_OU_OBJETO_NA_FRENTE = 250
DISTANCIA_LIXEIRA_ABERTA_COM_PESSOA_OU_OBJETO_NA_FRENTE = PROFUNDIDADE_LIXEIRA + 1


# Estagios Lixeira
QUANTIDADE_ESTAGIOS_NIVEL_LIXEIRA = 5

ESTAGIO_LIXEIRA_NIVEL_1 = 0 # Lixeira vazia(0%)
ESTAGIO_LIXEIRA_NIVEL_2 = 25 # Lixeira com nivel baixo(até 25%)
ESTAGIO_LIXEIRA_NIVEL_3 = 50 # Lixeira na metade(até 50%)
ESTAGIO_LIXEIRA_NIVEL_4 = 75 # Lixeira quase cheia(até 75%)
ESTAGIO_LIXEIRA_NIVEL_5 = 100 # Lxeira está cheia

# Defini para qual ponto de lixo o microcontralador está informando o nivel da lixeira.
PONTO_LIXO_ID = 6
ID_INFORMADOR = 2 # 1 - Usuário(Quando a informação é feita via sistema) 2 - Microcontrolador ESP32
LIXEIRA_ID = 5
GRUPO_ID = 10

# API enviada a informação automaticamente
API_INFORMATIVO_LIXEIRA = 'http://127.0.0.1:5000/cadastrar_informativo_lixeira'
API_ATUALIZAR_LIXEIRA = 'http://127.0.0.1:5000/atualizar_nivel_lixeira'

# REDE
SSID=''
PASSWORD=''
NUMERO_TENTATIVAS_CONECTAR_UMA_REDE_WIFI = 10

