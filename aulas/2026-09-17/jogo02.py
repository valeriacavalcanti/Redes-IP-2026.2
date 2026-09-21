# Jogo 2.0

import random

NUMERO_SECRETO = random.randint(1, 100)

chute = int(input('Chute: '))

while chute != NUMERO_SECRETO:
    print('Tente novamente')
    chute = int(input('Chute: '))

print('Acertou!')
print(chute, NUMERO_SECRETO)
