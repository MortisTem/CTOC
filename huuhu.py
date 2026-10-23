# 6. FECHA del día más caluroso
maximo = float(datos[0]["temperatura_max"])
fecha_max = datos[0]["fecha"]
for fila in datos:
    valor = float(fila["temperatura_max"])
    if valor > maximo:
        maximo = valor
        fecha_max = fila["fecha"]
print("Día más caluroso:", fecha_max, "con", maximo, "ºC")

# 7. CONTAR con DOS condiciones (calor y sin lluvia)
contador = 0
for fila in datos:
    if float(fila["temperatura_max"]) > 30 and float(fila["precipitacion_mm"]) == 0:
        contador += 1
print("Días con más de 30 ºC y sin lluvia:", contador)

# 8. PORCENTAJE de días con lluvia
dias_lluvia = 0
for fila in datos:
    if float(fila["precipitacion_mm"]) > 0:
        dias_lluvia += 1
porcentaje = dias_lluvia / len(datos) * 100
print("Días con lluvia:", dias_lluvia, "(", round(porcentaje, 1), "%)")

# 9. MEDIA POR MES
suma_mes = {}
dias_mes = {}
for fila in datos:
    mes = int(fila["fecha"].split("-")[1])
    media_dia = (float(fila["temperatura_max"]) + float(fila["temperatura_min"])) / 2
    if mes not in suma_mes:
        suma_mes[mes] = 0
        dias_mes[mes] = 0
    suma_mes[mes] += media_dia
    dias_mes[mes] += 1

for mes in suma_mes:
    print("Mes", mes, ":", round(suma_mes[mes] / dias_mes[mes], 2), "ºC")

# 10. MES CON MÁS LLUVIA
lluvia_mes = {}
for fila in datos:
    mes = int(fila["fecha"].split("-")[1])
    if mes not in lluvia_mes:
        lluvia_mes[mes] = 0
    lluvia_mes[mes] += float(fila["precipitacion_mm"])

mes_top = 1
for mes in lluvia_mes:
    if lluvia_mes[mes] > lluvia_mes[mes_top]:
        mes_top = mes
print("Mes más lluvioso:", mes_top, "con", round(lluvia_mes[mes_top], 1), "mm")

# 11. RACHA más larga sin lluvia
racha = 0
racha_max = 0
for fila in datos:
    if float(fila["precipitacion_mm"]) == 0:
        racha += 1
        if racha > racha_max:
            racha_max = racha
    else:
        racha = 0
print("Racha más larga sin lluvia:", racha_max, "días")

# 12. AMPLITUD TÉRMICA (día con más diferencia entre max y min)
amp_max = 0
fecha_amp = ""
for fila in datos:
    amp = float(fila["temperatura_max"]) - float(fila["temperatura_min"])
    if amp > amp_max:
        amp_max = amp
        fecha_amp = fila["fecha"]
print("Mayor amplitud:", round(amp_max, 1), "ºC el", fecha_amp)

# 13. SOLO UN MES CONCRETO (julio = 7)
suma = 0
for fila in datos:
    mes = int(fila["fecha"].split("-")[1])
    if mes == 7:
        suma += float(fila["precipitacion_mm"])
print("Lluvia en julio:", round(suma, 1), "mm")

# 14. VARIOS MESES (verano = junio, julio y agosto)
lluvia_verano = 0
for fila in datos:
    mes = int(fila["fecha"].split("-")[1])
    if mes == 6 or mes == 7 or mes == 8:
        lluvia_verano += float(fila["precipitacion_mm"])
print("Lluvia en verano:", round(lluvia_verano, 1), "mm")