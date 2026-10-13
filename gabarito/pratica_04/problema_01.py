def somar_notas(nota1: int, nota2: int, nota3: int) -> int:
    return nota1 + nota2 + nota3


def calcular_media_aritmetica(nota1: int, nota2: int, nota3: int) -> int:
    soma_total = somar_notas(nota1, nota2, nota3)
    return int(soma_total / 3)


def calcular_media_ponderada(nota1: int, nota2: int, nota3: int) -> int:
    soma_ponderada = somar_notas(nota1 * 2, nota2 * 3, nota3 * 5)
    return int(soma_ponderada / 10)


def obter_maior_media(nota1: int, nota2: int, nota3: int) -> int:
    media_aritmetica = calcular_media_aritmetica(nota1, nota2, nota3)
    media_ponderada = calcular_media_ponderada(nota1, nota2, nota3)

    if media_aritmetica > media_ponderada:
        return media_aritmetica
    else:
        return media_ponderada


def verificar_aprovacao(nota1: int, nota2: int, nota3: int) -> bool:
    maior_media = obter_maior_media(nota1, nota2, nota3)
    if maior_media >= 70:
        return True
    else:
        if maior_media >= 40:
            return True
        else:
            return False


# Main

nota_1 = int(input("Informe o valor da nota 1: "))
nota_2 = int(input("Informe o valor da nota 2: "))
nota_3 = int(input("Informe o valor da nota 3: "))

maior_media_aluno = obter_maior_media(nota_1, nota_2, nota_3)
status_aprovado = verificar_aprovacao(nota_1, nota_2, nota_3)

print(
    f"Maior média obtida: {maior_media_aluno} | Aprovado/Em Exame: {status_aprovado}"
)