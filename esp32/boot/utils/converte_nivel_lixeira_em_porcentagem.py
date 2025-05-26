from utils.calibrar_lixeira import Calibracao

def calcular_nivel_lixeira_em_porcentagem(distancia_entre_sensor_lixo):

    profundidade_lixeira = int(Calibracao.get_atribute(Calibracao,'profundidade_calibrada'))

    nivel_lixeira = profundidade_lixeira - int(distancia_entre_sensor_lixo)

    return (nivel_lixeira / profundidade_lixeira) * 100