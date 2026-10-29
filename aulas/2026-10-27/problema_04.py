estoque_inicial = [0] * 5
recebido = [0] * 5
estoque_atualizado = [0] * 5

for i in range(len(estoque_inicial)):
    estoque_inicial[i] = int(input('Quantidade: '))

for i in range(len(recebido)):
    recebido[i] = int(input('Quantidade adquirida: '))

for i in range(len(estoque_atualizado)):
    estoque_atualizado[i] = estoque_inicial[i] + recebido[i]

for i in range(len(estoque_atualizado)):
    print(estoque_atualizado[i])
