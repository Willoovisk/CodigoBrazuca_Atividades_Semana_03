numero = int(input("Digite um número: "))
fat = numero

while numero > 1:
    fat = fat * (numero -1)
    numero = numero -1
    
print("O fatorial do número digitado é:", fat)