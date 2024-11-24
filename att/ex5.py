def tabuada():
    num = int(input("qual tabuada voce quer?: "))
    cont = 0

    while (cont < 11):
        tabu = num * cont
        print(f"{num}X{cont}= {tabu}")
        cont +=1
    print("Ta Na Mão")

tabuada()
