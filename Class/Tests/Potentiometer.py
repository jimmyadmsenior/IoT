from machine import Pin, PWM, ADC
from utime import sleep

pot = ADC(26)          # Leitura do potenciômetro no ADC0
led = PWM(Pin(15))     # LED no pino 15
led.freq(1000)

while True:
    val = pot.read_u16()         # Valor de 0 a 65535
    led.duty_u16(val)            # Aplica ao LED
    sleep(0.01)
