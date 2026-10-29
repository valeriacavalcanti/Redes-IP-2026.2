precos = [0] * 6

for i in range(6):
    precos[i] = float(input('Preço: '))

for i in range(6):
    precos[i] = precos[i] * 1.2

for i in range(6):
    print(i, precos[i])
