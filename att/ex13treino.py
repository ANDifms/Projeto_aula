
def mediaTreino():
    notas = input("digite as notas do aluno, seguidas por espaço: ")

    numeros = list(map(int, notas.split()))
    cont_numero = len(numeros)

    divi = sum(numeros) / cont_numero

    num_mais_media = [num for num in numeros if num > 6]
    print(f"notas maiores que a media: {num_mais_media}, sua media é: {divi}")

mediaTreino()
