a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a < b and a < c:
    if b < c:
        print("A ordem crescente dos números digitados é:", a,"->", b,"->", c)
    else:
        print("A ordem crescente dos números digitados é:", a,"->", c,"->", b)

elif b < a and b < c:
    if a < c:
        print("A ordem crescente dos números digitados é:", b,"->", a,"->", c)
    else:
        print("A ordem crescente dos números digitados é:", b,"->", c,"->", a)

elif c < a and c < b:
    if a < b:
        print("A ordem crescente dos números digitados é:", c,"->", a,"->", b)
    else:
        print("A ordem crescente dos números digitados é:", c,"->", b,"->", a)
