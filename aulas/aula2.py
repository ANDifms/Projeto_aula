import random

num = int(input("Digite um numero de 1 - 10: "))

sorteio = random.randint(1, 10)

if num == sorteio:
    print("voce acertou")
else:
    sorteio = random.randint(1, 5)
    print("voce errou, tente de novo\n")

