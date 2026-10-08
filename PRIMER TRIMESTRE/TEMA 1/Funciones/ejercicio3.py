#Función que recibe un diccionario y una clave, y devuelve su valor.

def obtenerValor(diccionario, clave):
    return diccionario.get(clave)

alumno = {"nombre": "Leo Messi", "curso": "DAW", "edad": 39}

#Aquí pongo una clave que sí existe y otra que no existe.
print(obtenerValor(alumno, "curso"))
print(obtenerValor(alumno, "telefono"))