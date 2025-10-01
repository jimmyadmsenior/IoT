# Importa apenas as funções e classes necessárias de cada módulo
from machine import Pin
from utime import sleep, sleep_us, ticks_us, ticks_diff

# --- Configuração dos Pinos ---
# Altere os números dos pinos se sua conexão for diferente
TRIGGER_PIN = 14
ECHO_PIN = 15

# Inicializa os pinos do Pico
trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def medir_distancia_cm():
    """
    Função que aciona o sensor e calcula a distância em centímetros.
    A lógica de tempo e cálculo matemático é feita diretamente aqui.
    """
    # Garante um pulso limpo, começando com o trigger em nível baixo
    trigger.low()
    sleep_us(2)

    # Envia um pulso de 10 microssegundos para acionar o sensor
    trigger.high()
    sleep_us(10)
    trigger.low()

    # Loop para aguardar o início do pulso de retorno (echo)
    # Usamos uma proteção 'timeout' para não travar o programa indefinidamente
    timeout_start = ticks_us()
    while echo.value() == 0:
        if ticks_diff(ticks_us(), timeout_start) > 1000000: # Timeout de 1 segundo
            print("Erro: Timeout ao esperar o sinal de echo.")
            return -1 # Retorna -1 para indicar um erro
    
    # Marca o tempo de início quando o echo vai para nível alto
    tempo_inicial = ticks_us()

    # Loop para aguardar o fim do pulso de retorno
    while echo.value() == 1:
        if ticks_diff(ticks_us(), tempo_inicial) > 1000000: # Timeout de 1 segundo
            print("Erro: Timeout ao medir o sinal de echo.")
            return -1

    # Marca o tempo final quando o echo volta para nível baixo
    tempo_final = ticks_us()

    # Calcula a duração do pulso em microssegundos
    duracao_pulso = ticks_diff(tempo_final, tempo_inicial)

    # Calcula a distância em cm
    # Velocidade do som no ar é aprox. 343.2 m/s, que é 0.03432 cm/µs.
    # A duração do pulso é o tempo de IDA e VOLTA, por isso dividimos por 2.
    distancia = (duracao_pulso * 0.03432) / 2
    
    return distancia

# --- Loop Principal ---
print("Iniciando medições...")
while True:
    dist = medir_distancia_cm()

    # Verifica se não ocorreu um erro na medição
    if dist > 0:
        print(f"O objeto está a: {dist:.2f} cm")

    # Pausa de 1 segundo entre as medições
    sleep(1)