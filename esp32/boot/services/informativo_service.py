import json
from configuracao import PONTO_LIXO_ID,ID_INFORMADOR,API_INFORMATIVO_LIXEIRA,SCRIPT_SENDO_EXECUTADO_NO_ESP32
import requests
from store.log import log_message

dados = { "ponto_lixo_id" : PONTO_LIXO_ID, "informado_por_id" : ID_INFORMADOR,"observacao":"Atualizado Nivel Lixeira !","nivel_lixeira":1}


def informar_nivel_lixeira(nivel_lixeira,observacao=dados['observacao']):
    
    dados['nivel_lixeira'] = int(nivel_lixeira)
    dados['observacao'] = observacao
    
    try:

        log_message("Enviando dados para o servidor....","SUCCESS")
        log_message(f"{dados}")
        resposta = requests.post(API_INFORMATIVO_LIXEIRA,json=dados)
        body = json.loads(resposta.text)

        if not resposta.status_code == 201:

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
