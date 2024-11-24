
def pares():
    numIni = int(input("digite o numero inicial"))
    numFim = int(input("digite o numero final"))

    for i in range(numIni, numFim): # pega as duas variaveis e faz um laço de repeticao
        # if numIni < numFim:
        resul = i % 2 # pega a variavel atual "I" e divite ela por 2
        if resul == 0: # se o resultado for igual a 0 ela é par
            print(i) # imprime o numero atual que foi dividido por 0 

pares()

