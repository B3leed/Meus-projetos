import random
import time

while True:
    try:
        Numero_random = int(input('advinhe um numero de 1 a 100: ').strip())
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if Numero_random == 0:
        print('voce digitou 0, numero invalido')
        break

    numero_ronaldo = random.randint(1, 100)
    time.sleep(1)

    if Numero_random == numero_ronaldo:
        print('parabens voce acertou o numero')
    else:
        print('voce erro tabom?')
        time.sleep(1)
        print(f'o numero era {numero_ronaldo}')

    if Numero_random == 67:
        print('677777777777777777777777777777777777777777')

    break
