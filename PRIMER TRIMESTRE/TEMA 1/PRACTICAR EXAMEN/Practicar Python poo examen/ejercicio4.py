#Mini ejercicio 4.
#Crear clase Operaciones con un método dividir(a, b) que gestione ZeroDivisionError.
#Realizar una división válida y otra con divisor cero usando try-except.

class Operaciones:
    def dividir(self, z, k):
        try:
            resultado = z / k
            print(f"{z} / {k} = {resultado}")
        except ZeroDivisionError:
            print("No se puede dividir entre cero.")

operacion1 = Operaciones()

operacion1.dividir(10, 2)

operacion1.dividir(10, 0)