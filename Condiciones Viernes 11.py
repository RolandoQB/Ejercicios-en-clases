# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Viernes 11/06/2021
class condicion:

        def __init__(self,num1,num2):
            self.numero1=num1
            self.numero2=num2
            numero = self.numero1+self.numero2
            self.numero3=numero

        def condicion(self):
            if self.numero1==self.numero2:
                 print("numero1:{} y numero2:{} son iguales".format(self.numero1,self.numero2))
            elif self.numero1 < self.numero3:
                print("numero1:{} es menor numero3:{}".format(self.numero1,self.numero3))
            else:
                print("no son iguales")
            print("fin del metodo")

condi1 = condicion(8,18)
print(condi1.numero3)
print(condi1.condicion())
class ciclo:

    def __init__(self,num=10):
        self.numero=num


    def usowhile (self):
        print("dentro de la clase",self.numero)
        LETRA=""
        while LETRA not in ("a","e","i","o","u"):
            LETRA =input("ingrese vocal: ").lower()
            #caracter= caracter.lower()

        print("si es la letra correcta:{} si es vocal".format(LETRA))

ciclo1= ciclo()
print("fuera de la clase",ciclo1.numero)
print(ciclo1.usowhile())