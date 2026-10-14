#1. Pide dos números al usuario y muestra:  
#- Su suma  
#- Su división entera  
#- El resto de la división  
#- La potencia del primero elevado al segundo 

#2.1
num1 = int(input("Introduce un número:"))
num2 = int(input("Introduce un segundo número:"))

print(f"Suma: {num1 + num2}")
print(f"División entera: {num1 // num2}")
print(f"Resto: {num1 % num2}")
print(f"Potencia: {num1 ** num2}")