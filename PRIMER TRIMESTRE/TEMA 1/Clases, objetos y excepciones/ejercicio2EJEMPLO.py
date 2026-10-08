# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        # Si el precio o la cantidad son negativos, lanzamos el error
        if precio < 0 or cantidad < 0:
            raise ValueError("Precio o cantidad no pueden ser negativos")
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print("Producto:", self.nombre)
        print("Precio:", self.precio, "€")
        print("Cantidad:", self.cantidad)


# Lista con 3 productos distintos
productos = [
    Producto("Portátil", 799.99, 5),
    Producto("Ratón", 15.50, 40),
    Producto("Teclado", 29.90, 25),
]

# Recorremos la lista y mostramos la info de cada uno
print("--- Lista de productos ---")
for producto in productos:
    producto.mostrar_info()
    print()

# Probamos con un precio negativo y capturamos el error
print("--- Producto con datos negativos ---")
try:
    producto_malo = Producto("Monitor", -100, 3)
    producto_malo.mostrar_info()
except ValueError as error:
    print("Error:", error)