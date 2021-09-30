notas = []
for indice in range(1,6):
	while True:
		nota = int(input("Introduce la nota %d: " % indice))
		if nota>=0 and nota<=10: break
	notas.append(nota)


print("Notas: \n",end="")
for nota in notas:
	print(nota," ",end="")
print()
print("Nota media: \n",sum(notas)/len(notas))
print("Nota max: \n",max(notas))
print("Nota min: \n",min(notas))