def fatorial():
    num = int(input("Digite um número: "))

    # Verifica se o número é válido para fatorial
    if num < 0:
        print("Fatorial não é definido para números negativos.")
    else:
        fatorial = 1  # Começamos com 1, pois é o elemento neutro da multiplicação
        cont = num  # Inicializamos o contador com o valor do número

        while cont > 1:  # Continuar enquanto o contador for maior que 1
            fatorial *= cont  # Multiplicamos o fatorial pelo contador
            cont -= 1  # Decrementamos o contador

        print(f"O fatorial de {num} é {fatorial}.")
fatorial()