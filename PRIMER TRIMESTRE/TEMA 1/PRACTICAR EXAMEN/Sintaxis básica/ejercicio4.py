#1. Pide un número y muestra si es positivo, negativo o 0.  
#2. Pide la edad de una persona y muestra:  
#- `"Eres mayor de edad"` si es mayor o igual a 18.  
#- `"Eres menor de edad"` en caso contrario.  

#4.1
num = int(input("Introduce un número:"))

if num > 0:
    print("Positivo.")
elif num < 0:
    print("Negativo.")
else:
    print("Es 0.")

#4.2
edad = int(input("Introduce tu edad:"))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")