#Mini ejercicio 1.
#Crea una clase Sensor con los atributos públicos: id (str), unidad (str) y valor (float). Incluye el método mostrar_info().
#Crear dos sensores y mostrar su información llamando a mostrar_info().

class Sensor:
    def __init__(self, id, unidad, valor):
        self.id = id
        self.unidad = unidad
        self.valor = valor

    def mostrar_info(self):
        print(self.id, self.valor, self.unidad)

sensor1 = Sensor("S1", "ºC", 16)
sensor2 = Sensor("S2", "ºC", 42)

sensor1.mostrar_info()
sensor2.mostrar_info()