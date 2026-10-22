soma = 0
#numeros = [0,0,0,0]
qtd = 10
numeros = [0] * qtd

for i in range(len(numeros)):
    numeros[i] = int(input('Número: '))
    #print(numeros)
    soma = soma + numeros[i]

media = soma / (i + 1)

print(soma)
print(media)

for i in range(len(numeros)):
    if numeros[i] > media:
        print(i,numeros[i],'maior')
    else:
        print(i,numeros[i], 'nao maior')
