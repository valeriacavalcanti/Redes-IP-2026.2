def maior_valor(valor1, valor2) -> float:
    if valor1 > valor2:
        return valor1
    else:
        return valor2


# Main

idade1 = int(input("Idade:"))
altura1 = float(input("Altura: "))
peso1 = float(input("Peso: "))

idade2 = int(input("Idade:"))
altura2 = float(input("Altura: "))
peso2 = float(input("Peso: "))

maior_idade = maior_valor(idade1, idade2)
maior_altura = maior_valor(altura1, altura2)
maior_peso = maior_valor(peso1, peso2)

print('Maior Idade:', maior_idade)
print('Maior Altura:', maior_altura)
print('Maior Peso:', maior_peso)