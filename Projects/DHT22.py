from machine import Pin
from dht import DHT22 # da biblioteca DHT eu vou importar o DHT22
from utime import sleep

sensor = DHT22(Pin(15))  # Cria o objeto 'sensor' no pino GP15 usando o sensor DHT22

while True:
    sensor.measure()  # Solicita ao sensor que faça a medição de temperatura e umidade
    temp = sensor.temperature()  # Lê a temperatura medida
    umid = sensor.humidity()  # Lê a umidade medida

    if temp != None and umid != None:
        print("Temperatura: {}°C".format(temp))  # Exibe a temperatura no console serial
        #print(f"Temperatura: {temp} }°C)
        print("Umidade: {}%".format(umid))  # Exibe a umidade no console serial
    else:
        print("Falha na leitura dos dados.")  # Caso algo anormal aconteça (por segurança)

    sleep(3)  # Aguarda 3 segundos antes da próxima medição
