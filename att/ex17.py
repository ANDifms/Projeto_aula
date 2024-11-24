def juntaNumeros():
    
    entrada = input("digite uma sequencia de numeros positivos e negativos separados por espaço: ")

    num_str = entrada.split() # divide os numeros em partes

    negativos = [int(n) for n in num_str if int(n) < 0] # transforma texto em numero e filtra os valores que sao negativos 
    positivo = [int(n) for n in num_str if int(n) > 0]

    juntaTudo = negativos + positivo # junta tudo né kkk

    print(juntaTudo)

juntaNumeros()