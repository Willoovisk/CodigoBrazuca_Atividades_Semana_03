lista = []
check = 0

while check != "N":
    lista.append(int(input("Digite um número: ")))
    check = input("Deseja incluir mais número na lista? Digite: S ou N ")

maior = max(lista)
menor = min(lista)
media = sum(lista) / len(lista)

print("O maior valor da lista é:",maior,"o menor valor da lista é:",menor,"e a média dos valores é:", media)