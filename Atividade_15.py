def soma(numero):
    
    resultado = 0
    proximo = 1
    cont = 0

    while cont < numero:

        resultado = resultado + proximo
        proximo = proximo + 1
        cont = cont + 1
    print("O Resultado da soma é: ",resultado)

soma(int(input("Digite um número ")))