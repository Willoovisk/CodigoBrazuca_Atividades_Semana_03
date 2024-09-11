
def media(nota):
  soma = 0
  cont = 0

  while nota != -1:
    soma = soma + nota
    cont = cont + 1
    nota = int(input("Digite o valor da nota, para encerrrar digite -1 "))

  media = soma / cont

  print("A média das notas é:", media)

media(int(input("Digite o valor da nota ")))