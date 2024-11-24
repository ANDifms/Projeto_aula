frase = input("digite uma frase: ")

def contador_caract(frase):
    contagem = {}

    for char in frase:
        if char in contagem:
            contagem[char] += 1
        else:
            contagem[char] = 1
        
    return contagem

res = contador_caract(frase)

print(res)