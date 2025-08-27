from machine import Pin
from time import sleep

buzzer = Pin(15, Pin.OUT)

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)