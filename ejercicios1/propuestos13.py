from re import match
import math

print("\nIngresar valores del primer grupo: \n")
x1=int(input("x1: "))
y1=int(input("y1: "))
z1=int(input("z1: "))
print("Ingresar valores del segundo grupo: \n")
x2=int(input("x2: "))
y2=int(input("y2: "))
z2=int(input("z2: "))

s1=(math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
print("La distancia entre dos puntos es : ",s1)