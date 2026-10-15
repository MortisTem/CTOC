#1. Crea una tupla con los días de la semana.  
#2. Muestra el tercer día de la semana accediendo por índice.  
#3. Intenta modificar un elemento de la tupla y explica qué ocurre.  
#4. Convierte la tupla en una lista y añade un día extra.  
#5. Recorre la tupla con un `for` y muestra todos sus elementos.

diasSemana1 = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

print(diasSemana1[2])

#Da error porque una tupla no se puede modificar.
#diasSemana1.remove("Jueves")

diasSemana2 = list(diasSemana1)

diasSemana2.append("Otro")

print(diasSemana2)

for diasSemana in diasSemana1:
    print(diasSemana)