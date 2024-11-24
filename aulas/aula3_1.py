from random import randint
#Ex criar um laco para imprimir somente os numeros divisiveis por 4, de 1 ate um numero 

sorteio = randint(10, 50)

i = 1 
while i <= sorteio:
    if i % 4 ==0:
        print(i) 
    i += 1 
