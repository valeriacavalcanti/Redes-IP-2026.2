# Esse programa serve para obter o valor unitário de
# um produto e a respectiva quantidade comprada
# calcular o valor devido

valor_unitario = input('Digite valor unitário: ')
valor_unitario = float(valor_unitario)

quantidade_comprada = input('Digite a quantidade: ')
quantidade_comprada = int(quantidade_comprada)

total_devido = valor_unitario * quantidade_comprada

print(total_devido)
