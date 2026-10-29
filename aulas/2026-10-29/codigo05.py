# alunos: 3
# nota: 4

notas = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]


# ler todas as notas de todos os alunos
for i in range(3):
    for j in range(4):
        notas[i][j] = input(f'Aluno {i + 1} Nota {j + 1}: ')

# exibir todas as notas de todos os alunos
for i in range(3):
    print(f'Aluno {i + 1}')
    for j in range(4):
        print(f'Nota {j + 1} = {notas[i][j]}')
