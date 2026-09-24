categoria = input('Categoria: ')
altura = int(input('Altura: '))
largura = int(input('Largura: '))
profundidade = int(input('Profundidade: '))
peso = int(input('Peso: '))


if categoria == 'vip':
    if altura <= 55 and largura <= 35 and profundidade <= 25 and peso <= 23:
        print('S')
    else:
        print('N')
else:
    if altura <= 55 and largura <= 35 and profundidade <= 25 and peso <= 10:
        print('S')
    else:
        print('N')


