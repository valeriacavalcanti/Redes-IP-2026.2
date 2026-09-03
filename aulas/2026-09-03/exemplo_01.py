# FUNÇÕES
def encontrar_maior_valor(valor1:int, valor2:int, valor3:int) -> int:
    if (valor1 > valor2) and (valor1 > valor3):
        maior = valor1
    else:
        if (valor2 > valor3):
            maior = valor2
        else:
            maior = valor3

    return maior
            


# PROGRAMA PRINCIPAL

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

maior_valor = encontrar_maior_valor(num1, num2)

print(maior_valor)
