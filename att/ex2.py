def parImpar():
    num = int(input("Digite Numero: "))

    print("calculando...")

    calc = num % 2 

    if (calc == 0 ):
        print("numero par")
    else:
        print("numero imper")

parImpar()