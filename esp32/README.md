# ESP32

Este é um módulo extra do sistema, além dos niveis da lixeiras poderem ser informado por usuários, também poderão ser informados e atualizados por dispositivos previamente configurados e instalados nas lixeiras recicláveis. Gerando dados muito mais precisos. Fazendo com que empresas possam se programar antecipadamente e agendar coleta de uma maneira mais eficiente.

Placas ESP32 são instaladas nas lixeiras, podem ser integradas ao sistema por meio de requisições programadas feitas
por elas nas APIs disponibilizadas para estes dispositivos no sistema.

O sistema identificando estas requisições, faz atualização do nivel da lixeira no banco de dados, e através de outra API Websocket que será criada, todos os sistemas que estarão conectados e recebem a informação que os niveis da lixeira foram atualizados em tempo real. Fazendo com que a tela do sistema atualize automaticamente.

# Passos que foram necessários para integrar o ESP32 ao sistema(API)

Estes foram basicamente os passos que permitiram que o ESP32 começasse a medir os niveis das lixeiras e enviar as informações para o sistema(API).

-- Placa ESP32_GENERIC
-- Instalação do Python >= 3.10.11
-- Driver para ESP32 para permitir computador reconhecer o dispositivo.
-- Firmware Micropython para ser instalado no esp32
-- Esptool ferramenta que permite a instalação do firmware Micropython
-- Emulador Tera Term 5 para processar os primeiros comandos com python direto no ESP32.
-- Pacote adafruit-ampy  1.1.0 responsável por permitir copiar scripts python criados para a placa ESP32.
-- Uma classe base do python hcsr04.py para medição do nivel da lixeira
-- Criação do script para processamento das medições no ESP32 e enviar para o sistema(API)
-- Criação de API que recebe os dados gerados pelos microcontroladores(ESP32)

