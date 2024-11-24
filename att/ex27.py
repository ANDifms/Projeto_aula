from collections import Counter

texto = input("Escreva um texto: ")

def palavra_frequentes(texto):
    palavra = texto.lower().split()

    contador = Counter(palavra)
    palavra_comuns = contador.most_common(3)
    return palavra_comuns

res = palavra_frequentes(texto)

print("AS 3 palavras mais frequentes sao: ")
for palavra, frequencia in res:
    print(f"{palavra}: {frequencia}")


