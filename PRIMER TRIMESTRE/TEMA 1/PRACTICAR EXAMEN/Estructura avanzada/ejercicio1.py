#1. Crea una lista con los nombres de tus 5 asignaturas y muéstrala.  
#2. Accede al primer y último elemento de la lista.  
#3. Añade un elemento a la lista y elimina otro.  
#4. Ordena una lista de números `[5, 2, 9, 1, 7]`.  
#5. Recorre la lista de asignaturas con un `for` e imprímelas una a una.  

asignaturas = ["Lenguaje de marcas", "Bases de datos", "Programación", "Entornos de desarrollo", "Sistemas informáticos"]
print(asignaturas)

print(asignaturas[0])
print(asignaturas[4])

asignaturas.append("Inglés")
asignaturas.remove("Programación")

print(asignaturas)

numeros = [5, 2, 9, 1, 7]
numeros.sort()
print(numeros)

for asignatura in asignaturas:
    print(asignatura)