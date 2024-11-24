def soma_dig(matriz):
    n = len(matriz) # le o tamanho da matriz
    soma_principal = 0
    soma_segundaria = 0

    i = 0
    while i < n:
        soma_principal += matriz[i][i]
        soma_segundaria += matriz[i][n - 1 - i] #faz a soma da diagnal secundaria
        i += 1  # só intrementa mesmo kkk

    return soma_principal + soma_segundaria

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res = soma_dig(matriz)
print(f"a soma é igual a: {res}")