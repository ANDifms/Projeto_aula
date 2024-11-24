
def medias():
    notas = list(map(float, input("Digite as notas separadas por espaço: ").split()))

    media = sum(notas) / len(notas)


    notas_acima_da_media = [nota for nota in notas if nota > media]


    print(f"Média das notas: {media:.2f}")
    print(f"Notas maiores que a média: {notas_acima_da_media}")

medias()