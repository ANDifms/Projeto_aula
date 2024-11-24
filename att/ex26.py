def uni_dicionarios(dicionario1, dicionario2):
    dicionarioMesclado = dicionario1.copy()

    for chave, valor in dicionario2.items():
        if chave in dicionarioMesclado:

            dicionarioMesclado[chave] += valor
        else:
            dicionarioMesclado[chave] = valor

    return dicionarioMesclado

dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 3, 'c': 4, 'd': 5}

dicionarioUnido = uni_dicionarios(dicionario1, dicionario2)

print(f"Dicionário mesclado: {dicionarioUnido}")