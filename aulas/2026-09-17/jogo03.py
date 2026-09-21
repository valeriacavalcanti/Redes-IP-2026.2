# Jogo 3.0

import random

NUMERO_SECRETO = random.randint(1, 100)
print(NUMERO_SECRETO)

chute = int(input('Chute (1-100): '))

while chute != NUMERO_SECRETO:
    #print('Tente novamente')
    if chute > NUMERO_SECRETO:
        print('Seu chute é maior')
    else:
        print('Seu chute é menor')
        
    chute = int(input('Chute (1-100): '))

print('Acertou!')
print(chute, NUMERO_SECRETO)
