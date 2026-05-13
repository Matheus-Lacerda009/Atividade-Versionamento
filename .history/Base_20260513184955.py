op = input("Insira a operação desejada:\n")
num1 = int(input("Insira o primeiro número da operação:\n"))
num2 = int(input("Insira o segundo número da operação:\n"))
match op:
    case "+":
        print("Resultado:", num1 + num2)
    case "-":
        print("Resultado:", num1 - num2)
    case "/":
        print("Resultado: ", num1 / num2)
    case "*":
        print("Resultado: ", num1 * num2)
    case _:
        print("Operação não encontrada!")