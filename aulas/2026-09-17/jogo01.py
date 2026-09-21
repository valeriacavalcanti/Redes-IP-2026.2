# Jogo 1.0

NUMERO_SECRETO = 83

chute = int(input('Chute: '))

while chute != NUMERO_SECRETO:
    print('Tente novamente')
    chute = int(input('Chute: '))

print('Acertou!')
print(chute, NUMERO_SECRETO)
