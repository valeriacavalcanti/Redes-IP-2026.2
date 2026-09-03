num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

if (num1 > num2) and (num1 > num3):
    maior = num1
else:
    if (num2 > num3):
        maior = num2
    else:
        maior = num3

print(maior)
