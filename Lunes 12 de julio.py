# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#clase Lunes 12 de julio 

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

ejer=ejercicios()
num=int(input("ingrese un numero: "))
print("llamada 1")
ejer.perfecto(num)
input()
lista = [3,5,6,8,28]
print("llamada 2")
for num in lista:
     ejer.perfecto(num)
input()
print("llamada 3")
ejer.perfecto(23)



#####################################################
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
                acu=acu+1
        return acu


ejer=ejercicios()
num=int(input("ingrese un numero: "))
print("llamada 1")
resp = ejer.perfecto2(num)
if num == resp:
    print("{} es perfecto".format(numero))
else:
    print("{} no es perfecto".format(numero))
  
# input()
# lista = [3,5,6,8,28]
# print("llamada 2")
# for num in lista:
#      ejer.perfecto(num)
# input()
# print("llamada 3")
# ejer.perfecto(23)



#####################################################
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
                acu=acu+1
        return acu


ejer=ejercicios()
lista = [3,5,6,8,28]
print("llamada 2")
perfectos=[]
for num in lista:
    if ejer.perfecto2(num) == num:
       perfecto.append (num)
print(perfectos)