# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre


# funciones de fecha
from datetime import datetime,timedelta,date
hoy, fdia = datetime.now(), date.today()
futuro = hoy + timedelta(days=30)
dif, aa, mm, dd = futuro, hoy.year, hoy.month, hoy.day
fecha = date(aa, mm, dd+2)
print(hoy)
print(fdia)
print(futuro)
print(dif)
print(fecha)