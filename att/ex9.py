def idades():

    idade = int(input("qual sua idade?: "))

    if(idade >= 80):
        print(f"voce nao pode dirigir, voce esta quase dirigindo uma caixa grande")
    elif( idade >= 18):
        print(f"ja que voce tem {idade} anos entao pode dirigir")
    else:
        print(f"ok voce ainda nao pode dirigir, voce tem apenas {idade} anos")

idades()