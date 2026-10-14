#1. Declara variables de tipo entero, decimal, cadena y booleano. Muéstralas por pantalla.  
#2. Pide al usuario su nombre y edad con `input()` y muestra un mensaje:  
#3. Convierte un número decimal introducido por el usuario en entero y muéstralo.  
#4. Declara dos variables numéricas y muestra su suma, resta, multiplicación y división. 

#1.1
entero = 10
decimal = 7.2
cadena = "Pereira"
booleano = True

print(entero)
print(decimal)
print(cadena)
print(booleano)

#1.2
nombre = input("Introduce tu nombre:")
edad = input("Introduce tu edad:")

print(f"Mi nombre es {nombre} y tengo {edad} años.")

#1.3
numDecimnal = float(input("Introduce un número decimal:"))

numEntero = int(numDecimnal)

print(f"El número decimal introducido es {numDecimnal}, pero se ha convertido en entero y ahora es {numEntero}.")

#1.4
num1 = 2
num2 = 4

print(f"Suma = {num1 + num2}")
print(f"Resta = {num1 - num2}")
print(f"Multiplicación = {num1 * num2}")
print(f"División = {num1 / num2}")