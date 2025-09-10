from machine import Pin
from time import sleep
import dht

# Configuração do sensor DHT
sensor = dht.DHT11(Pin(15))  # Substitua DHT11 por DHT22 se necessário

# Configuração do botão e do buzzer
botao = Pin(14, Pin.IN, Pin.PULL_DOWN)  # Botão conectado ao GPIO 14
buzzer = Pin(15, Pin.OUT)  # Buzzer conectado ao GPIO 15

# Loop principal
while True:
    try:
        sensor.measure()
        temperatura = sensor.temperature()
        umidade = sensor.humidity()
        print(f"Temperatura: {temperatura}°C, Umidade: {umidade}%")
    except Exception as e:
        print("Erro ao ler o sensor:", e)
    if botao.value() == 1:  # Verifica se o botão foi pressionado
        print("Botão pressionado! Ativando o buzzer.")
        buzzer.on()  # Liga o buzzer
        sleep(1)  # Mantém o buzzer ligado por 1 segundo
        buzzer.off()  # Desliga o buzzer
    else:
        buzzer.off()  # Garante que o buzzer está desligado
    sleep(0.1)  # Aguarda um curto intervalo antes de verificar novamente