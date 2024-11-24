entrada = input("digite uma sequencia de numeros separados por esapaços: \n")

lis_num = list(map(int, entrada.split()))

def remova(lista):

    resultado = []
    for numero in lista:
        if numero not in resultado:
            resultado.append(numero) # add num se nao estiver na lista
    return resultado
    
lista_nova = remova(lis_num)
print(f"lista sem duplicatas: {lista_nova}")