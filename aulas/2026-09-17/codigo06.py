qtd = 0
soma = 0

num = int(input('Número: '))

while num != 0:
    qtd = qtd + 1
    soma = soma + num
    num = int(input('Número: '))

print('saiu')

if qtd > 0:
    media = soma / qtd
    print(num, qtd, soma, media)
else:
    print('Não tem média')
    print(num, qtd, soma)



