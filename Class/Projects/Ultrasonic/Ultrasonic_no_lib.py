# Nome do arquivo: main.py

from machine import Pin
from utime import sleep
from hcsr04 import HCSR04 # Importa a nossa nova biblioteca

# --- Configuração do Sensor ---
# Inicializa o sensor usando a nossa classe e especificando os pinos
sensor = HCSR04(trigger_pin=14, echo_pin=15)

# --- Loop Principal ---
print("Iniciando medições com biblioteca...")
while True:
    # Chama o método da biblioteca para obter a distância
    distancia = sensor.distancia_cm()
    
    if distancia < 0:
        print("Falha na leitura. Verifique o sensor e as conexões.")
    else:
        print(f"Distância: {distancia:.2f} cm")
    
    # Pausa de 1 segundo
    sleep(1)