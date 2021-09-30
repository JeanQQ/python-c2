import random
lista=[]

for indice in range(1,10):
    lista.append(random.randint(1,10))

for numero in lista :
        print(numero,"",numero**2,"",numero**3) 