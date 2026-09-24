categoria = input('Categoria: ')
altura = int(input('Altura: '))
largura = int(input('Largura: '))
profundidade = int(input('Profundidade: '))
peso = int(input('Peso: '))


if categoria == 'vip':
    limite_peso = 23
else:
    limite_peso = 10


if altura <= 55 and largura <= 35 and profundidade <= 25 and peso <= limite_peso:
    print('S')
else:
    print('N')
