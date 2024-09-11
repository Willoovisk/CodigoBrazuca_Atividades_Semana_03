def palindromo(texto):

    check = texto[::-1]
    if check == texto:
        print("O texto digitado é umm palíndromo")
    else:
        print("O texto digitado não é umm palíndromo")
    
palindromo(input("Digite seu texto aqui: "))