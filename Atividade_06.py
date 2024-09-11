def check(texto):
    vogal = ["a", "e", "i","o","u","A", "E", "I","O","U"]
    cont = 0

    for i in texto:
        if i in vogal:
            cont = cont + 1

    print(cont)

check(input("Digite um texto: "))