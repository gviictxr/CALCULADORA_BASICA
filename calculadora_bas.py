def calculadora():
    
    num1 = int(input("Digite o PRIMEIRO NÚMERO: "))
    num2 = int(input("Digite o SEGUNDO NÚMERO: "))
    
    operador = input("DIGITE UM OPERADOR (+, -, *, /): ")
    
    if operador == "+":
        result = num1 + num2
    elif operador == "-":
        result = num1 - num2
    elif operador == "*":
        result = num1 * num2
    elif operador == "/":
        result = num1 / num2
    print("The result is:", result)
if __name__ == "__main__":
    calculadora()