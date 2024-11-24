
entrada = input("Digite uma lista de numeros, nao pode ser negativos\n e tem que conter espaços: ")

def filtro_par(lista):
    return[numero for numero in lista if numero % 2 == 0]

trans_num = list(map(int, entrada.split()))
lista_par = filtro_par(trans_num)

print(f"sua Lista de numeros Pares {lista_par}")