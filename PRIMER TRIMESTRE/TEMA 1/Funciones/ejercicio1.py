#Crear una función que calcule el área de un triángulo.

def area_triangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado


#Se piden los datos al usuario.
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

#Con esto llamo a la función y muestro el resultado.
area = area_triangulo(base, altura)
print("El área del triángulo es:", area)
