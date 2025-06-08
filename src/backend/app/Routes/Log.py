from flask import request, jsonify, Blueprint
import time
import json
import pprint

log = Blueprint('log',__name__)

def formatar_label(label):

    if label == 'SUCCESS':

        return f"\033[0;30;42mSUCCESS\033[m"
    
    if label == 'ERROR':

        return f'\033[0;30;41mERROR\033[m'
    
    if label == 'WARNING':

        return f'\033[0;30;43mWARNING\033[m'
    
    return ''

def imprimir_log_esp32(mensagens):

    for mensagem in mensagens:

        log = f"{mensagem['time_execucao']} - {formatar_label(mensagem['label'])} - {mensagem['message']}\n"
        print(log)
    

@log.route('/cadastrar_log_esp32',methods=['POST'])
def cadastrar_log():

    data = request.get_json()
    
    imprimir_log_esp32(data)


    return jsonify({'message':'Log cadastrado com sucesso !'}),201



