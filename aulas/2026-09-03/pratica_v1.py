num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

if (num1 > num2):
    maior = num1
else:
    maior = num2

if (num3 > maior):
    maior = num3

print(maior)
