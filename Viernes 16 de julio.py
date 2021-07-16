# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#clase Viernes 16 de julio 

def __init__(self):
    pass
class ejercicios:
    def __init__(self):
        pass

    def parimpar(self,numero):
        if numero % 2 == 0:
            print("{} es par".format(numero))
        else:
            print("{} es inpar".format(numero))

    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+1
        if numero == acu:
                print("{} es perfecto".format(numero))
        else:
                print("{} no es perfecto".format(numero))
    
    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+i
        return acu

class Programacion(ejercicios):
    def __init__(self):
        pass
prog1= Programacion()
num=6
if prog1.perfecto2(num)== num:
    print(num,"es perfecto")
else:
    print(num,"no es perfecto")