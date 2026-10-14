#Mini ejercicio 3.
#Crear la clase Estudiante con nombre y edad. Si edad < 0, lanzar ValueError.
#Crear un estudiante válido y otro con edad negativa usando try-except.

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        if edad < 0:
            raise ValueError("Edad no puede ser negativa.")

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad}")

estudiante1 = Estudiante("Amaro", 23)
estudiante1.mostrarInfo()

try:
    estudiante2 = Estudiante("Rafael", -7)
    estudiante2.mostrarInfo()
except ValueError as z:
    print("Excepción detectada.", z)