n = int(input("Digite o numero da sequencia de fibonacci que voce quer: "))
def gerar_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return[0]
    elif n == 2:
        return[0, 1]
    
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)

    return fibonacci
res = gerar_fibonacci(n)
print(f"Os Primeiros numeros da sequencia sao: {res}")

