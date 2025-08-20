# Aqui declaramos as bibliotecas que vamos utilizar
from machine import Pin
from utime import sleep

# Aqui declaramos as variáveis e os LEDS
led_vermelho = Pin(15, Pin.OUT)
led_amarelo = Pin(16, Pin.OUT)
led_verde = Pin(17, Pin.OUT)


while(True):
    # Liga o LED
    led_vermelho.on()
    sleep(1)
    # Desliga o LED
    led_vermelho.off()
    sleep(1)