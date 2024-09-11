def fibo(numero):
    lista = []
    atual = 0
    seguinte = 1
    novo = 0

    for i in range(numero):
        lista.append(atual)
        novo = atual + seguinte
        atual = seguinte
        seguinte = novo
    
    print("A sequência gerada é: ", lista)

fibo(int(input("Digite o número de elementos: ")))  
