from configuracao import SSID,PASSWORD,SCRIPT_SENDO_EXECUTADO_NO_ESP32,NUMERO_TENTATIVAS_CONECTAR_UMA_REDE_WIFI
import network
import time
from store.log import log_message

if SCRIPT_SENDO_EXECUTADO_NO_ESP32:

    wlan = network.WLAN()
    wlan.active(True)

def conectar_wifi():

    if SCRIPT_SENDO_EXECUTADO_NO_ESP32:

        try:
            conectado = False
            tentativas = 0
            wlan.active(False)
            wlan.active(True)

            while not conectado:

                wlan.connect(SSID, PASSWORD)
                log_message("Aguardando conexao...","WARNING")
                time.sleep(10)

                if wlan.isconnected():

                    conectado = True
                    log_message("O wifi foi conectado com sucesso !","SUCCESS")
                
                if tentativas == NUMERO_TENTATIVAS_CONECTAR_UMA_REDE_WIFI:

                    wlan.active(False)
                    log_message("O numero de tentativas para conectar ao wifi foi excedido !","ERROR")
                    return False
                
                tentativas +=1
            
            return True
        except Exception as e:

            log_message("Falha ao tentar se conectar ao wifi !","ERROR")
            return False
        

def verificar_conectividade_wifi():

    if not SCRIPT_SENDO_EXECUTADO_NO_ESP32:

        return False

    if not wlan.isconnected():

        log_message("Tentando reconectar wifi.....","WARNING")
        conectar_wifi()

        if wlan.isconnected():

            return True

        elif not wlan.isconnected():

            return False

    log_message("O esp32 foi conectado ao wifi com sucesso !","SUCCESS")
    return True

