diccionario = {"el:the","hola:hi","petter:petter","perro:dog"}
palabras = input("Introduce las listas de palabras y traducciones en formato palabra:traducción separadas por comas:  ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input("Introduce una frase en español: ")
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')