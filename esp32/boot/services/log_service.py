from configuracao import API_LOG
import requests
from store.log import log_message, get_log_messages
import json

dados = {}


def cadastrar_logs():

    try:
    
        log_message("Enviando Log para servidor.....","WARNING")
        resposta = requests.post(url=API_LOG,headers = {'content-type': 'application/json'}, json = get_log_messages())
        body = json.loads(resposta.text)

        if not resposta.status_code == 201:

            raise Exception(f"{body['message']}")

        log_message(f"{body['message']}","SUCCESS")

        return True
    
    except Exception as e:

        log_message(f"Falha ao enviar log para o servidor : {str(e)}","ERROR")
        
        return False
