import random
 
def jogo(numero):
    
    alvo = random.randrange(1,100)
    

    while numero != alvo:
        print("Tente novamente")
        numero = int(input("Digite um número de 1 a 100 "))
    
    print("Parabéns você acertou!!")


jogo(int(input("Digite um número de 1 a 100 ")))