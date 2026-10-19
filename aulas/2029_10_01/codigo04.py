# obter a quantidade de valores e ler os respectivos números
# exibir a soma dos números lidos
# exibir a média dos números lidos

soma = 0
qtd = int(input('Quantidade: '))

for i in range(qtd):
    num = int(input(f'Número {i + 1}º: '))
    soma = soma + num

media = soma / qtd
#media = soma / (i + 1)

print(soma)
print(media)
