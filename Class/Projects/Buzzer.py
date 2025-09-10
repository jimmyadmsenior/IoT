from machine import Pin, PWM
from time import sleep

buzzer = PWM(Pin(15))
buzzer.freq(2000)  # Frequência de 2kHz, ajuste conforme necessário

while True:
    buzzer.duty_u16(20000)  # Volume moderado
    sleep(1)
    buzzer.duty_u16(0)      # Desliga o buzzer
    sleep(1)