lista = []

def tabuada(numero):

    cont = 1
      
    while cont <= 10:
        lista.append(numero*cont)
        cont += 1
        
          
tabuada(int(input("Digite um número:")))
print("A tabuada de é:", lista)
   



