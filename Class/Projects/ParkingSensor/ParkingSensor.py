# Importa as funções e classes necessárias
from machine import Pin, PWM
from utime import sleep, sleep_us, ticks_us, ticks_diff

# --- Configuração dos Pinos ---
# Sensor Ultrassônico
TRIGGER_PIN = 14
ECHO_PIN = 15

# Buzzer
BUZZER_PIN = 16 # Escolha um pino GPIO livre

# --- Inicialização dos Componentes ---
# Sensor
trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

# Buzzer com PWM para controlar o tom
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty_u16(0) # Inicia o buzzer desligado

def medir_distancia_cm():
    """
    Função que aciona o sensor e calcula a distância em centímetros.
    """
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(10)
    trigger.low()

    # Usamos um 'timeout' para evitar que o programa trave se não houver eco
    timeout_start = ticks_us()
    while echo.value() == 0:
        if ticks_diff(ticks_us(), timeout_start) > 500000: # Timeout de 0.5s
            return -1 # Retorna -1 para indicar erro

    tempo_inicial = ticks_us()

    while echo.value() == 1:
        if ticks_diff(ticks_us(), tempo_inicial) > 500000:
            return -1

    tempo_final = ticks_us()
    duracao_pulso = ticks_diff(tempo_final, tempo_inicial)
   
    # Cálculo da distância
    distancia = (duracao_pulso * 0.03432) / 2
   
    return distancia

# --- Loop Principal ---
print("Sensor de proximidade com buzzer ativado.")
print("Aproxime objetos do sensor.")

while True:
    distancia = medir_distancia_cm()

    # Verifica se a leitura da distância foi bem-sucedida
    if distancia > 0:
        print(f"Distância: {distancia:.1f} cm")

        # --- Lógica do Buzzer ---
       
        # 1. Objeto MUITO PERTO (som contínuo e agudo)
        if distancia <= 10:
            buzzer.freq(1500) # Tom mais agudo para alerta
            buzzer.duty_u16(32768) # Liga o buzzer na metade da potência

        # 2. Objeto se APROXIMANDO (bipes rápidos)
        elif 10 < distancia <= 40:
            buzzer.freq(1000) # Tom padrão
            buzzer.duty_u16(32768) # Liga para um bipe curto
            sleep(0.05) # Duração do bipe
            buzzer.duty_u16(0) # Desliga
           
            # A pausa entre os bipes é proporcional à distância
            # Quanto menor a distância, menor a pausa, mais rápido apita
            pausa = distancia / 100
            sleep(pausa)

        # 3. Objeto LONGE (sem som)
        else:
            buzzer.duty_u16(0) # Garante que o buzzer esteja desligado
            sleep(0.5) # Pausa padrão quando não há objetos próximos
           
    else:
        # Se houve erro na leitura, desliga o buzzer e espera um pouco
        buzzer.duty_u16(0)
        print("Falha na leitura.")
        sleep(1)