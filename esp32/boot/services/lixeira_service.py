import json
from configuracao import LIXEIRA_ID,API_ATUALIZAR_LIXEIRA,SCRIPT_SENDO_EXECUTADO_NO_ESP32
import requests

dados = { "lixeira_id" : LIXEIRA_ID}

def atualizar_nivel_lixeira(nivel_lixeira):

    dados['nivel_lixeira'] = int(nivel_lixeira)
    
    try:
        
        print("Enviando dados para o servidor....")
        resposta = requests.put(API_ATUALIZAR_LIXEIRA,json=dados)

        if not resposta.status_code == 200:

            raise

        body = json.loads(resposta.text)

        print(f"\033[0;30;42mSUCESS\033[m ${body['message']}")

        return True
    
    except Exception as e:

        print("\033[0;30;41mERROR\033[m",str(e))
        return False
