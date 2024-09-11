resto = 0
def check(numero):
    
    resto = numero % 2
    if resto == 0:
        print("O número",numero,"é par")
    else:
        print("O número",numero,"é ímpar")


check(int(input("Digite um número:")))
