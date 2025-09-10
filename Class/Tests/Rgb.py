from machine import Pin
from utime import sleep

led_vermelho = Pin(16, Pin.OUT)

led_verde = Pin(15, Pin.OUT)

led_azul = Pin(14, Pin.OUT)

while(True):
  led_vermelho.on()