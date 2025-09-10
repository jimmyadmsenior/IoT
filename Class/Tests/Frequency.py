from machine import Pin, PWM
from utime import sleep

"""
Definimos a porta 16 como PWM e ela já sabe que é para 
ESCREVER como saída ANALÓGICA
"""

led_potencia = PWM(Pin(16))

led_potencia.freq(1000)

while(True):
    led_potencia.duty_u16(63000)
    sleep(2)
    led_potencia.duty_u16(33000)
    sleep(2)
    led_potencia.duty_u16(15000)
    sleep(2)
    led_potencia.duty_u16(8000)
    sleep(2)
    led_potencia.duty_u16(1000)
    sleep(2)
    led_potencia.duty_u16(100)
    sleep(2)