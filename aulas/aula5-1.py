# jogo da forca ------------
from random import choice

# ATIVIDADE
# colocar quantidade de chances 
# colocar mais palavras 

# DESAFIO morse code decrypter 


acertos = 0
palavra_secreta = "BANANA"
lista_frutas = ('maça', 'goiaba', 'Uva')
# print(palavra_secreta.upper()) # transforma em maiusculo so quando imprime uma vez
# print(palavra_secreta.lower()) # transforma em minusculo so quando imprime uma vez


# lista_secreta = ['-', '-', '-', '-', '-', '-']
lista_sectrta = ['_' for _ in palavra_secreta]


print(len(palavra_secreta)) # len conta a quantidade de elemento em uma lista

# os dois começam como falso
acertou = enforcou = False

while not acertou and not enforcou:
    print(lista_sectrta)
    chute = input("Digite uma letra: ") 

    for index, letra in enumerate(palavra_secreta):
        if chute.lower() == letra.lower():
            lista_sectrta[index] = chute
            acertos += 1
            print(acertos)

        if acertos == len(palavra_secreta ):
            print("parabens voce acertou")
            print(lista_secreta)
            acertou = True

            
        
            



        
        

