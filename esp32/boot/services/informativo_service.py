import json
from configuracao import PONTO_LIXO_ID,ID_INFORMADOR,API_INFORMATIVO_LIXEIRA,SCRIPT_SENDO_EXECUTADO_NO_ESP32
import requests

dados = { "ponto_lixo_id" : PONTO_LIXO_ID, "informado_por_id" : ID_INFORMADOR,"observacao":"Informado por ESP32"}

def informar_nivel_lixeira(nivel_lixeira):

    dados['nivel_lixeira'] = int(nivel_lixeira)
    
    try:
        print("Enviando dados para o servidor....")
        resposta = requests.post(API_INFORMATIVO_LIXEIRA,json=dados)

        if not resposta.status_code == 201:

            raise

        body = json.loads(resposta.text)

        print(f"\033[0;30;42mSUCESS\033[m ${body['message']}")

        return True

    except Exception as e:

        print("\033[0;30;41mERROR\033[m",str(e))
        return False
