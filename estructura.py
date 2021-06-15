# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

"""taller en clases, ejercicios hechos por el maestro
Replica realizada por el estudiante"""

# num=20
# nombre="ana"
# print(num,type(num))
# print(nombre,type(nombre))
# def mensaje(msg):
#     print(msg)

# mensaje("mi primer programa")
# mensaje("mi segundo programa")

class sintaxis:
    instancia=0
    #__init__ metodoconstructor que se ejecuta cuando se intancia la clase cuyo onjetivo es  
    # crear e instanciar los atributos de la clase. self es un objeto que representa la clase creada.

    def __init__(self,dato="llamando al constructor1" ):
        self.frase=dato   #-------> #atributos de instancia
        sintaxis.instancia=sintaxis.instancia+1


    def usovariables(self):
        edad,peso=20,70,5
        nombres:"Josue Quijije"
        tipo_de_sexo: "M"
        civil:True
           #print("civil={}y su tipo es:{}",format(civil,type(civil)))
        usuario=()
        usuario=("jquijije2001","1234","jquijije2001@gmail.com",True)
        #             0      1      2             3 
        x=usuario[0]
        materia=["programacion web","php","poo"]
        materia.append("go")

        estudiante={}
        estudiante={"nombre":"Josue","edad":20,"fac":"faci",}
        estudiante["edad"]=20
        #print(materia,materia[2:],materia[:2],mateia[:-1],materia[-2:])
        print("x,y")
        print(estudiante,estudiante["nombre"])
    def mostrar(self):
        print("mostrar")
        print(self.frase)



ejer1=sintaxis()
ejer1.usovariables()

