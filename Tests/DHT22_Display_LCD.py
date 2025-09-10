from machine import I2C, Pin
from time import sleep
from dht import DHT22
from pico_i2c_lcd import I2cLcd

# Configuração do sensor DHT22 no pino GP15
sensor = DHT22(Pin(15))

# Configuração do barramento I2C nos pinos GP16 (SDA) e GP17 (SCL)
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# Descobre o endereço I2C automaticamente (geralmente é 0x27 ou 0x3F)
I2C_ADDR = i2c.scan()[0]

# Cria o objeto do display LCD com 2 linhas e 16 colunas
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# Mensagem inicial
lcd.putstr("Iniciando sensor...")
sleep(2)
lcd.clear()

while True:
    sensor.measure()
    temp = sensor.temperature()
    umid = sensor.humidity()

    lcd.clear()
    lcd.putstr(f"Temp: {temp:.2f} C")
    lcd.move_to(0, 1)
    lcd.putstr(f"Umid: {umid:.1f}%")

    sleep(2)
