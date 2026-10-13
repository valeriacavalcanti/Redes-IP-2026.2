# problema_01_2v com a declaração de variável

numero = int(input('Dia da Semana: '))

if numero == 0:
    dia_semana = "Domingo"
elif numero == 1:
    dia_semana = "Segunda-feira"
elif numero == 2:
    dia_semana = "Terça-feira"
elif numero == 3:
    dia_semana = "Quarta-feira"
elif numero == 4:
    dia_semana = "Quinta-feira"
elif numero == 5:
    dia_semana = "Sexta-feira"
elif numero == 6:
    dia_semana = "Sábado"

print(dia_semana)