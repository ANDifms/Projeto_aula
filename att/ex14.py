
def comparador():

    palavra = input("vamos comparar a sua palavra: ")

    arvalaq = palavra[::-1]

    if arvalaq == palavra:
        print(f"sim {arvalaq} é palíndromo de {palavra}")
    else: 
        print(f"nao {arvalaq} nao é palíndromo de {palavra}")
    
comparador()