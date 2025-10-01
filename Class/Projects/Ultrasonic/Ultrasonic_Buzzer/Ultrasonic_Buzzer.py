# Código para Buzzer Passivo
# Usa PWM para gerar diferentes tons (frequências).

from machine import Pin, PWM
from utime import sleep

# Define o pino GPIO ao qual o buzzer passivo está conectado.
# Não precisa definir como OUT, a classe PWM já faz isso.
buzzer = PWM(Pin(16))

print("Iniciando teste do buzzer passivo...")

# Define a frequência da nota em Hertz (Hz)
# Exemplos: 440Hz = Nota Lá (A4), 523Hz = Nota Dó (C5)
NOTA_DO = 523
NOTA_RE = 587
NOTA_MI = 659

# Função para tocar um som
def tocar_nota(frequencia, duracao):
    if frequencia > 0:
        print(f"Tocando nota com frequência: {frequencia}Hz")
        buzzer.freq(frequencia)      # Define a frequência (o tom da nota)
        buzzer.duty_u16(32768)     # Liga o som com 50% de volume (duty cycle)
        sleep(duracao)               # Toca pela duração especificada
   
    buzzer.duty_u16(0)             # Desliga o som (silêncio)

# Loop para tocar uma pequena melodia
while True:
    try:
        tocar_nota(NOTA_DO, 0.3)
        sleep(0.1) # Pausa entre as notas
        tocar_nota(NOTA_RE, 0.3)
        sleep(0.1)
        tocar_nota(NOTA_MI, 0.3)
        sleep(1.0) # Pausa maior no final

    except KeyboardInterrupt:
        # Se você parar o código (Ctrl+C no Thonny), desliga o PWM.
        print("Programa interrompido.")
        buzzer.deinit()
        breakdd