#Crear una función que reciba una lista de números decimales y devuelva su media.

def media(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma / len(lista)

numeros = [4.5, 7.0, 3.5, 9.0]

resultado = media(numeros)
print("La media es:", resultado)