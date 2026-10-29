nomes = [0] * 8

for i in range(8):
    nomes[i] = input('Nome: ')

for i in range(len(nomes) - 1, -1, -1):
    print(nomes[i])
