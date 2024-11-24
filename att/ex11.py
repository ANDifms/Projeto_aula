
def contarPalavra():

    frase = input("escreva uma frase: ")

    palavraAjustada = frase.lower().split() # diminui as letras e trasforma elas em lista
    palavra_unica = set(palavraAjustada) # o set ve se existe alguma palavra repetida e retira
    cont_palavra = len(palavra_unica) # conta as palavras que foram mandadas pelo "palavra_unica"

    print(f"o numero de palavras que tem em {frase} é {cont_palavra}")



contarPalavra()