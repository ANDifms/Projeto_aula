frase = input("digite uma frase para contas as avogais e consoantes: ")

def contar_letras(letras):
    vogais = "aeiouAEIOU"

    cont_vogais = 0
    cont_consoantes = 0

    # leitura da frase

    for char in letras:
        if char.isalpha(): # ele ve se é letra 
            if char in vogais:
                cont_vogais += 1
            else:
                cont_consoantes += 1
    total_letra = cont_vogais + cont_consoantes

    return cont_vogais, cont_consoantes, total_letra

vogais, consoantes, total_letra = contar_letras(frase)
print(f"A frase {frase} posui {total_letra} letras, contem: {vogais} vogais e {consoantes} consoantes")


