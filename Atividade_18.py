frase = input("Digite uma frase: ")
palavras = 1

for espaco in frase:
    if espaco == " ":
        palavras = palavras + 1

print(palavras)