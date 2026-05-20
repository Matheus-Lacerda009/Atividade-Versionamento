sair = False
op = ""
def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por 0!"
    return a / b
def multiplicacao(a, b):
    return a * b
def exponencial(a, b):
    return a ** b
def porcentagem(a, b):
    return a * (b / 100)
while sair == False:
    num1 = float(input("Insira o primeiro número da operação:\n"))
    num2 = float(input("Insira o segundo número da operação:\n"))
    while op not in ["+", "-", "/", "*"]:
        op = input("Insira a operação desejada:\nSoma: +\nSubtração: -\nDivisão: /\nMultiplicação: *\nExponencial: ^\nPorcentagem: %\n")
        match op:
            case "+":
                print("Resultado:", soma(num1, num2))
                break
            case "-":
                print("Resultado:", subtracao(num1, num2))
                break
            case "/":
                print("Resultado:", divisao(num1, num2))
                break
            case "*":
                print("Resultado:", multiplicacao(num1, num2))
                break
            case "^":
                print("Resultado:", exponencial(num1, num2))
                break
            case "%":
                print("Resultado:", porcentagem(num1, num2))
                break
        print("Operação não encontrada!")
    sair = bool(input("Digite 0 para sair: "))