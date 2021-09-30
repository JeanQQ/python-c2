print("Ingrese los siguientes datos :  \n")

tipoc=int(input("Tipo de cambio : \n S/"))
PrecioC=int(input("Precio de compra : \n S/"))
margen=int(input("Margen : \n"))

precion = (PrecioC*(100+margen)/100)

result=precion/tipoc

print("Resultado: \n",result)