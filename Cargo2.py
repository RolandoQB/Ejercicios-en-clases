# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Clases del dia Lunes 21/06/2021

class Cargo:
    secuencia=0
    def __init__(self,des="sin cargo"):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia 
        self.descripcion=des
    
cargo1= Cargo ()
print("cargo1",cargo1.codigo,cargo1.descripcion)

cargo2=Cargo("docente")
print("cargo2",cargo2.codigo,cargo2.descripcion)

cargo3 = Cargo(101)
print("cargo3",cargo3.codigo,cargo3.descripcion)
print(Cargo.secuencia)