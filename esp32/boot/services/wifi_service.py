from configuracao import SSID,PASSWORD,SCRIPT_SENDO_EXECUTADO_NO_ESP32,NUMERO_TENTATIVAS_CONECTAR_UMA_REDE_WIFI
import network
import time

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
                print("Aguardando conexão...")
                time.sleep(10)

                if wlan.isconnected():

                    conectado = True
                    print("\033[0;30;42mSUCESS\033[m O wifi foi conectado com sucesso !")
                
                if tentativas == NUMERO_TENTATIVAS_CONECTAR_UMA_REDE_WIFI:

                    wlan.active(False)
                    print("O numero de tentativas para conectar ao wifi foi excedido !")
                    return False
                
                tentativas +=1
            
            return True
        except Exception as e:

            print("\033[0;30;41mERROR\033[m Falha ao tentar se conectar !")
            return False
        

def verificar_conectividade_wifi():

    if not SCRIPT_SENDO_EXECUTADO_NO_ESP32:

        return False

    if not wlan.isconnected():

        print("Tentando reconectar wifi.....")
        conectar_wifi()

        if wlan.isconnected():

            return True

        elif not wlan.isconnected():

            return False
    
    print("O wifi está conectado !")
    return True

