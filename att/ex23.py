def calculadora():
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    operacao = input("digite sua operacao (+, -, *, /) ")

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else: 
            return "desculpe no momento estamos com erro \n volte mais tarde!!"
    else:
        return "essa operacao nao existe o Orelhudo"
    
    return f"Sua resposta {num1} {operacao} {num2}: {resultado}"

res = calculadora()
print(res)