lista1 = []
lista2 = []
lista3 = []

for indice in range(1,6):
    lista1.append(int(input("Introduce un número %d de la lista 1: \n"%indice)))
for indice in range(1,6):
    lista2.append(int(input("Introduce un número %d de la lista 2: \n"%indice)))
for indice in range(0,5):
	lista3.append(lista1[indice] + lista2[indice])

print("El total de las listas es: \n")
for numero in lista3:
	print(numero," ",end="")