#1. Pide una nota y clasifícala en:  
#- Suspenso (<5)  
#- Aprobado (5-6)  
#- Notable (7-8)  
#- Sobresaliente (9-10)  
#2. Pide al usuario un número del 1 al 7 y muestra el día de la semana correspondiente.  
#3. Pide una temperatura y muestra:  
#- `"Frío"` si es menor de 15.  
#- `"Templado"` si está entre 15 y 25.  
#- `"Caluroso"` si es mayor de 25.  

#5.1
nota = float(input("Introduce una nota:"))

if nota < 5:
    print("Suspenso.")
elif nota <= 6:
    print("Aprobado.")
elif nota <= 8:
    print("Notable.")
else:
    print("Sobresaliente.")

#5.2
numSemana = int(input("Introduce un número de la semana (del 1 - 7):"))

if numSemana == 1:
    print("Lunes.")
elif numSemana == 2:
    print("Martes.")
elif numSemana == 3:
    print("Miércoles.")
elif numSemana == 4:
    print("Jueves.")
elif numSemana == 5:
    print("Viernes.")
elif numSemana == 6:
    print("Sábado.")
else:
    print("Domingo.")

#5.3
temperatura = float(input("Introduce una temperatura:"))

if temperatura < 15:
    print("Frío.")
elif temperatura <= 25:
    print("Templado.")
else:
    print("Caluroso.")