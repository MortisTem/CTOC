#1. Pide un número y muestra si es positivo.  
#2. Pide una contraseña y comprueba si coincide con `"admin"`.  
#3. Pide una nota y muestra `"Has aprobado"` si es mayor o igual a 5.  
#4. Escribe un programa que compruebe si un número es par o impar.  
#5. Pide al usuario su edad e imprima si está en el rango de 18 a 65 años.

#3.1
num = int(input("Introduce un número:"))

if num > 0:
    print("El número introducido es positivo.")
else:
    print("El número introducido es negativo.")

#3.2
contraseña = input("Introduce una contraseña:")

if contraseña == "admin":
    print("Bien, la contraseña coincide con admin.")
else:
    print("La contraseña introducida no coincide con admin.")

#3.3
nota = float(input("Introduce una nota:"))

if nota >= 5:
    print("Has aprobado.")
else:
    print("Has suspendido.")

#3.4
num = int(input("Introduce un número:"))

if num % 2 == 0:
    print("Es número par.")
else:
    ("Es impar.")

#3.5
edad = int(input("Indique su edad:"))

if edad >= 18 and edad <= 65:
    print("Usted está en el rango correcto.")
else:
    print("No está en el rango de edad.")