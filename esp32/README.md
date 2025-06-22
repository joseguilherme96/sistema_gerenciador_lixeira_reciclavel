# Microcontrolador ESP32

Este é um módulo extra do sistema, além dos niveis da lixeiras poderem ser informado por usuários através do sistema, também poderão ser informados e atualizados automaticamente por dispositivos previamente configurados e instalados nas lixeiras recicláveis. Gerando dados precisos e em tempo real. Fazendo com que empresas possam se programar antecipadamente e agendar coleta de uma maneira mais eficiente. Criando rotas estratégicas.

Placas ESP32 podem ser instaladas nas lixeiras e integradas ao sistema. Automaticamente começam coletar dados, processar e enviar requisições para o sistema/API Flask.
O sistema identificando estas requisições, faz atualização do nivel da lixeira no banco de dados, e através de outra API Websocket que foi criada, todos os sistemas que estão conectados e recebem a informação que os niveis da lixeira foram atualizados em tempo real. Fazendo com que os dados sistema atualize automaticamente.

## Funcionalidades do Microcontrolador ESP32

- Permite configuração personalizada de acordo com cada lixeira que o dispositivo é implementado.
- Possui conectividade com Wifi.
- Permite calibração de altura da lixeira de acordo com cada lixeira que o ESP32 é implementado.
- Exibe e registra todas as atividades que estão sendo executadas no dispositivo em um arquivo de log que é gerado no Microcontrolador.
- Realiza leitura do nivel da lixeira.
- Coleta dados, processa e envia informações para o sistema/servidor.

## Passos que foram necessários para integrar o ESP32 ao sistema(API)

Estes foram basicamente os passos que permitiram que o ESP32 começasse a medir os niveis das lixeiras e enviar as informações para o sistema, para que pudesse ter informação em tempo real.

- Uma Placa ESP32_GENERIC
- Instalação do Python >= 3.10.11
- Driver para ESP32 para permitir computador reconhecer o dispositivo.
- Firmware Micropython para ser instalado no ESP32.
- ESPTOOL ferramenta que permite a instalação do firmware Micropython.
- Emulador Tera Term 5 para processar os primeiros comandos com python direto no ESP32.
- Pacote adafruit-ampy  1.1.0 responsável por permitir copiar scripts python criados para a placa ESP32.
- Uma classe base do python hcsr04.py para medição do nivel da lixeira.
- Criação do script para processamento das medições no ESP32 e enviar para o sistema(API).
- Implementação de todos os scripts criados no ESP32.

O código na pasta ESP32 pode ser executado de duas maneiras :

- Ser executado diretamente dentro do ESP32
- Ou em modo simulação

Aqui será focado na instalação, para o script rodar Modo Simulação, já que possívelmente não tenha como executar o script ESP32 no momento. Mas caso queira implementar este script siga basicamente os passos acima.

## Instalação

Abra a pasta ESP32 partindo da raiz de todo o projeto.

Instale as dependências.


```sh

    pip install -r requirements.txt

```

## Código sendo executado em modo simulação

Abra a pasta boot

Renomeie o arquivo configuracao_exemplo para configuracao.py

Abra o arquivo configuracao.py e edite algumas informações.

### Definido script em modo simulação

Defina False para variável abaixo. Assim quando você pode executar o script no próprio computador. O script começará a gerar numeros aleatórios como se estivesse sendo gerado por um sensor.

```sh

SCRIPT_SENDO_EXECUTADO_NO_ESP32 = False


```


## Defina a rede que o script será direcionado

Ainda dentro do arquivo configuracao.py, temos possíveis destinos de endereços quando as requisições são feitas para o servidor Flask, escolha a variável que contém o endereço que está sendo executado ou será exeutado o servidor Flask. Reatribua valores caso necessário. 

```sh

# Endereço de API para ser enviado a informação automaticamente
API_FLASK_BASE_URL_LOCAL='http://127.0.0.1:5000' # Local
API_FLASK_BASE_URL_NETWORK1='http://192.168.1.13:5000' # Rede Wifi 1
API_FLASK_BASE_URL_NETWORK2='http://192.168.43.243:5000' # Rede Wifi 2

API_FLASK_BASE_URL = f'${API_FLASK_BASE_URL_LOCAL}'


API_INFORMATIVO_LIXEIRA = f'${API_FLASK_BASE_URL}/cadastrar_informativo_lixeira'
API_ATUALIZAR_LIXEIRA = f'{API_FLASK_BASE_URL}/atualizar_nivel_lixeira'

```

Na variável API_FLASK_BASE_URL reatribua a ela um valor que melhor corresponde a base url que o servidor Flask está sendo ou será executado. Conforme padrão do servidor é iniciado no endereço 'http://127.0.0.1:5000'. Mas pode ser que mude caso esteja sendo executado em rede, o valor deverá ser alterado.

## Ative o ambiente virtual

Ainda dentro da pasta esp32. Ative o ambiente virtual usando o seguinte comando dentro da pasta backend

```sh

    .venv\scripts\activate

```

## Execute arquivo principal

Abra a pasta boot. E execute o arquivo boot.py


```sh

    cd boot

    python boot.py

```
