nombres=[]
edades=[]
n = int(input("N° de Personas: "))
for i in range (n):
    nombre = input("Nombre: ")
    nombres.append(nombre)
    edad = int(input("Edad: "))
    edades.append(edad)
print(nombres)
print(edades)
for i in range(0,n):
    print(nombres[i],"-",edades[i])
