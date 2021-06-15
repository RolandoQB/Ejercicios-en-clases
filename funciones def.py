# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

def vocales(frase):
    for car in frase:
        if car in ('a', 'e', 'i', 'o', 'u'):
            print(car)
oracion = input('Ingrese una oracion: ')
vocales(oracion.lower())
