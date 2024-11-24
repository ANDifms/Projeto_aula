palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")

def verificarAnagrama(palavra1, palavra2):
    palavra1 = palavra1.replace("", "").lower()
    palavra2 = palavra2.replace("", "").lower()

    if sorted(palavra1) == sorted(palavra2):
        print(f"A palavra {palavra1} e {palavra2} SÃO anagramas")
    else: 
        print(f"A palavra {palavra1} e {palavra2} NÃO anagramas")
    
saida = verificarAnagrama(palavra1, palavra2)
print(saida)

