qtd_positivo = 0
soma = 0
for i in range(6):
    valor = float(input(f'Valor {i+1}: '))
    if (valor > 0):
        qtd_positivo += 1
        soma += valor
media = soma / qtd_positivo
print(f'{qtd_positivo} valores positivos')
print(f'{media:.1f}')