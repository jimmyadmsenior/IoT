# Nome do arquivo: hcsr04.py

from machine import Pin
from utime import sleep_us, ticks_us, ticks_diff

class HCSR04:
    """
    Classe para encapsular a lógica de funcionamento do sensor ultrassônico HC-SR04.
    """
    def __init__(self, trigger_pin, echo_pin):
        """
        Inicializa o sensor com os pinos GPIO especificados.
        """
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)

    def distancia_cm(self):
        """
        Mede e retorna a distância em centímetros.
        """
        self.trigger.low()
        sleep_us(2)
        self.trigger.high()
        sleep_us(10)
        self.trigger.low()

        # Medição com timeout para evitar travamentos
        start_time = ticks_us()
        while self.echo.value() == 0:
            if ticks_diff(ticks_us(), start_time) > 500000:
                return -1 # Erro de timeout

        pulse_start = ticks_us()
        while self.echo.value() == 1:
            if ticks_diff(ticks_us(), pulse_start) > 500000:
                return -1 # Erro de timeout
        
        pulse_end = ticks_us()
        
        duracao_pulso = ticks_diff(pulse_end, pulse_start)
        distancia = (duracao_pulso * 0.03432) / 2
        
        return distancia