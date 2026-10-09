class Persona:
    def __init__(self, nombre, edad):
        if edad < 0:
            raise ValueError("Edad no puede ser negativa.")
        self.nombre = nombre
        self.edad = edad     

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Trabajador(Persona):
    def __init__(self, nombre: str, edad: int, salario: float):
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario} €")

persona1 = Persona("Leo Messi", 39)
persona1.mostrar_info()

try:
    personaErronea = Persona("Cristiano Ronaldo", -41)
    personaErronea.mostrar_info()
except ValueError as e:
    print("Excepción capturada:", e)

trabajador1 = Trabajador("Neymar", 40, 2500.0)
trabajador1.mostrar_info()