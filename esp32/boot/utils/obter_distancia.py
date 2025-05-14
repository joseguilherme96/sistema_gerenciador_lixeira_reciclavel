from configuracao import SCRIPT_SENDO_EXECUTADO_NO_ESP32,TRIGGER_PIN,ECHO_PIN
import random

sensor = {}
distancia_entre_sensor_lixo = 0

if SCRIPT_SENDO_EXECUTADO_NO_ESP32:

    from hcsr04 import HCSR04

    sensor = HCSR04(trigger_pin=TRIGGER_PIN, echo_pin=ECHO_PIN)

def get_distancia_entre_sensor_lixo():

    if SCRIPT_SENDO_EXECUTADO_NO_ESP32 :
        
        distancia_entre_sensor_lixo = sensor.distance_cm() 
    
    if not SCRIPT_SENDO_EXECUTADO_NO_ESP32:

        distancia_entre_sensor_lixo = random.randrange(1,300)

    return distancia_entre_sensor_lixo