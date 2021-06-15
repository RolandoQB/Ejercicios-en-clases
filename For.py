# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Clases del dia Lunes 14/06/2021

class For:
    def __init__ (self):
        pass
    def usoFor(self):
        #ciclo repetitivo de incremento o decremento se ejecuta por verdadero
        true=0
        nombre= "Josue"
        datos=["Josue",20,true]
        numeros=(2,5.6,4,1)
        docente={'nombre':'Josue','edad':20,'fac':'faci'}
        listanotas=[(30,40),(20,40),(50,40)]
        listaalumnos=[{"nombre":"erick","final":70},{"nombre":"Yandy","final":60},{"nombre":"danny","final":90}]
        j=0
        while j<5:
            print("while",j)
            j=j+1
        print()
        for i in range(5):
            print("for",i,end=" ")
        print()
        for i in range(1,5):
            print("for",i,end=" ")
        print()
        for i in range(2,10,2):
            print("for",i,end=" ")
        print()
        for i in range(12,3,-3):
            print("for",i,end=" ")
        print()
        print()
        print()
        lon=len(datos)
        for pos in range(lon):
            print(pos,datos[pos])
        print()
        print()
        lon=len(numeros)
        for pos in range(lon):
            print(pos,numeros[pos])
        print()
        print()
        for elem in nombre:
            print(elem,end=" ")

bucle=For()
bucle.usoFor()
