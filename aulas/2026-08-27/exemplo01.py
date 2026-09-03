nota1 = input('Nota 1: ')
nota1 = int(nota1)

nota2 = int(input('Nota 2: '))

nota3 = int(input('Nota 3: '))

media = (nota1 + nota2 + nota3) / 3

situacao = media >= 70

print(f'A média é {media:.2f}')

print(f'Sua situação é {situacao}')
