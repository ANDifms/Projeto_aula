def remover_dupli_lista_aninhada(lista_aninhada):
    nova_lista = []
    
    for sublista in lista_aninhada:
        sublista_unica = list(dict.fromkeys(sublista))
        nova_lista.append(sublista_unica)
    
    return nova_lista

lista_aninhada = [
    [1, 2, 3, 4, 4, 5],
    [6, 7, 8, 8, 9],
    [10, 11, 12, 10, 13]
]

lista_sem_duplicados = remover_dupli_lista_aninhada(lista_aninhada)

print(f"Lista sem duplicados: {lista_sem_duplicados}")