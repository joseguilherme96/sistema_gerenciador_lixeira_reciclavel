import json
from configuracao import LIXEIRA_ID,API_ATUALIZAR_LIXEIRA,SCRIPT_SENDO_EXECUTADO_NO_ESP32
import requests
from store.log import log_message

dados = { "lixeira_id" : LIXEIRA_ID}

def atualizar_lixeira(nivel_lixeira,esta_aberta):

    dados['nivel_lixeira'] = int(nivel_lixeira)
    dados['esta_aberta'] = esta_aberta

    try:
        
        log_message("Enviando dados para o servidor para atualizacao nivel de lixo","SUCCESS")
        log_message(f"{dados}",'SUCCESS')
        resposta = requests.put(API_ATUALIZAR_LIXEIRA,json=dados)
        body = json.loads(resposta.text)

        if not resposta.status_code == 200:

            raise Exception(f"{body['message']}")

        label = "SUCCESS"
        mensagem = f"{body['message']}"
        log_message(mensagem,label)

        log_message("Dados recebidos !","SUCCESS")

        mensagem = f'{body['dados']}'
        log_message(mensagem,"SUCCESS")

        return True
    
    except Exception as e:

        label = "ERROR"
        mensagem = f"{str(e)}"
        log_message(mensagem,label)
        return False
