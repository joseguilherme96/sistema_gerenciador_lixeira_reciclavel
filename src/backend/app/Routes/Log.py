from flask import request, jsonify, Blueprint
import time
import json
import pprint
from datetime import datetime
from flask_jwt_extended import jwt_required

log = Blueprint('log',__name__)

def formatar_label(label):

    if label == 'SUCCESS':

        return f"\033[0;30;42mSUCCESS\033[m"
    
    if label == 'ERROR':

        return f'\033[0;30;41mERROR\033[m'
    
    if label == 'WARNING':

        return f'\033[0;30;43mWARNING\033[m'
    
    return ''

def imprimir_log_esp32_no_console(mensagens):

    for mensagem in mensagens:

        log = f"{mensagem['time_execucao']} - {formatar_label(mensagem['label'])} - {mensagem['message']}\n"
        print(log)

def gravar_log_esp32_em_arquivo(logs):

    try:

        nome_arquivo = str(datetime.now()).split(" ")[0]

        with open(f'logs/{nome_arquivo}.txt', 'a') as arquivo:

            tempo_servidor = time.time()

            for log in logs:

                arquivo.write(f"{log['time_execucao']} - {log['label']} - {log['message']}\n")

            arquivo.write(f"{tempo_servidor} - SUCCESS -  A gravação do log do dispositivo ESP32 foi feita com sucesso ! \n")
        
        log = f"{tempo_servidor} - {formatar_label('SUCCESS')} - A gravação do log do dispositivo ESP32 em arquivo foi feita com sucesso ! \n"
        print(log)

        return True

    except Exception as e:

        log = f"122222 - {formatar_label('ERROR')} - Erro ao gravar o log do dispositivo ESP32 no arquivo ! \n"
        print(log)
        raise Exception(str(e))
    

@log.route('/cadastrar_log_esp32',methods=['POST'])
@jwt_required()
def cadastrar_log():

    try:

        logs = request.get_json()
        
        imprimir_log_esp32_no_console(logs)

        gravar_log_esp32_em_arquivo(logs)
    
    except Exception as e:

        return jsonify({'message':str(e)}),500


    return jsonify({'message':'Log cadastrado com sucesso !'}),201



