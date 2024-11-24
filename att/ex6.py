def notas():
    print("vamos calcular umas notas \nMe de 3 notas por favor")
    nota1 = float(input("nota1: ")) 
    nota2 = float(input("nota2: ")) 
    nota3 = float(input("nota3: ")) 

    somar = (nota1 + nota2 + nota3)/3

    if somar > 6:
        print(f"Aluno Aprovado com nota{somar}")
    else:
        print(f"Aluno reprovado com nota{somar}")
notas()