#Mini ejercicio 1.
#Crea una clase Sensor con los atributos públicos: id (str), unidad (str) y valor (float). Incluye el método mostrar_info().
#Crear dos sensores y mostrar su información llamando a mostrar_info().

class Sensor:
    def __init__(self, id, unidad, valor):
        self.id = id
        self.unidad = unidad
        self.valor = valor

    def mostrar_info(self):
        print(f"ID: {self.id}, Unidad: {self.unidad}, Valor: {self.valor}")