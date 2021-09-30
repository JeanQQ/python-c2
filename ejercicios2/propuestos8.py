nombres = []
edades = []
 
while True:	
	nombre = input("Nombre de un alumno: ")
	if nombre != "*":
		nombres.append(nombre)
		edades.append(int(input("Escribir Edad: ")))
	if nombre == "*": break;	


edad_max = max(edades)

print("Alumnos mayores de edad: \t")
for nombre,edad in zip(nombres,edades):
	if edad >= 18:
		print(nombre)

print("Alumnos mayores: \t")
for nombre,edad in zip(nombres,edades):
	if edad == edad_max:
		print(nombre)