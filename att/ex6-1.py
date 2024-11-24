def notas():
    print("vamos calcular umas notas \nMe de 3 notas por favor")
    nome = input("Nome do Aluno-a: " )
    cont = 1
    soma = 0

    while(cont < 4):
        nota = float(input(f"digite nota{cont}: "))
        soma = soma + nota
        cont += 1

    total = soma/3
    numeroredondo = round(total, 2)

    if total > 6:
        print(f"Aluno-a {nome} Aprovado com nota{numeroredondo}")
    else:
        print(f"Aluno-a {nome} reprovado com nota{numeroredondo}")

notas()


