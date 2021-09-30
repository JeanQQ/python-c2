lista = []
numero = int(input("Introduce un numero en la lista: \n"))
while numero>=0:
    lista.append(numero)
    numero = int(input("Introduce un numero en la lista: \n"))

for numero in lista:
    print(numero,"",end="")