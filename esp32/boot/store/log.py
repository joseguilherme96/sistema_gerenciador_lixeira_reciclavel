import time

log_messages = []

def print_log_esp32(dados_log):

    print(f"{dados_log['time_execucao']} -- {format_label(dados_log['label'])} -- {dados_log['message']}")

def log_execution_time():

    return time.time()

def log_message(mensagem="",label=""):

    tempo_execucao = str(log_execution_time())
    print_log_esp32({"time_execucao":tempo_execucao,"label":label,"message":mensagem})
    log_messages.append({"time_execucao": tempo_execucao,"label":label,"message": str(mensagem)})

def clear_log_message():

    log_messages.clear()

def format_label(label):

    if label == 'SUCCESS':

        return f"\033[0;30;42mSUCCESS\033[m"
    
    if label == 'ERROR':

        return f'\033[0;30;41mERROR\033[m'
    
    if label == 'WARNING':

        return f'\033[0;30;43mWARNING\033[m'
    
    return ''

def get_log_messages():

    return log_messages

def log_message_insert(index,mensagem="",label=""):

    tempo_execucao = str(log_execution_time())
    print_log_esp32({"time_execucao":tempo_execucao,"label":label,"message":mensagem})
    log_messages.insert(index,{"time_execucao": tempo_execucao,"label":label,"message": str(mensagem)})

def log_message_pop():

    log_messages.pop()
    