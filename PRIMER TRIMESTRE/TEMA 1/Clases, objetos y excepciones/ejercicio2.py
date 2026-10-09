# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        if precio < 0 or cantidad < 0:
            raise ValueError("Precio o cantidad no pueden ser negativos.")
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print("Producto:", self.nombre)
        print("Precio:", self.precio, "€")
        print("Cantidad:", self.cantidad)

productos = [
    Producto("Portátil", 799.99, 5),
    Producto("Ratón", 15.50, 40),
    Producto("Teclado", 29.90, 25),
]

print("Lista de productos:")
for producto in productos:
    producto.mostrar_info()
    print()

print("Producto con datos negativos:")
try:
    producto_malo = Producto("Monitor", -100, 3)
    producto_malo.mostrar_info()
except ValueError as error:
    print("Error:", error)