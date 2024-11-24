import random

def adivinhe():

    numero_aleatorio = random.randint(1,100)

    print("tente adivinhar o numero, voce tem 3 tentativas")
    print("-----")
    print(numero_aleatorio)
    print("-----")

    for i in range(1,4):
        numero = int(input(f"tentativa {i}: "))


    if numero == numero_aleatorio:
        print(f"Parabens o numero escolhido foi {numero_aleatorio}")
    else: 
        print(f"Desculpa voce errou, o numero escolhido foi {numero_aleatorio}")

adivinhe()


