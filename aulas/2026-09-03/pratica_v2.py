num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

maior = num1

if (num2 > maior):
    maior = num2

if (num3 > maior):
    maior = num3

print(maior)
