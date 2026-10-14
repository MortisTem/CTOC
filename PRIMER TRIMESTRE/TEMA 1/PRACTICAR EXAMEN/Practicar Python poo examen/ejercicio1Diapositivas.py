class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        if edad < 0:
            raise ValueError("Edad no puede ser negativa.")

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad}")
    
class Trabajador(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad} - Salario: {self.salario}€")

persona1 = Persona("Auron", 38)
persona1.mostrarInfo()

trabajador1 = Trabajador("Juan", 29, 3000.0)
trabajador1.mostrarInfo()

try:
    persona2 = Persona("Victor", -23)
    persona2.mostrarInfo()
except ValueError:
    print("Error, la edad no puede ser negativa.")