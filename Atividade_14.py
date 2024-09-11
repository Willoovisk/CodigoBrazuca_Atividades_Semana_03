a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação que deseja realizar:")

if op == "+":
    resultado = a + b

elif op == "-":
    resultado = a - b

elif op == "*":
    resultado = a * b

elif op == "/":
    resultado = a / b

print(" O resultado da operação escolhida é:", resultado)