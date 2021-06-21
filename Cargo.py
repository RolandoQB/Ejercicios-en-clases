# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#Clases del dia Lunes 21/06/2021
class Cargo:
    def __init__(self):
        self.codigo=99 
        self.descripcion="sin cargo"
    
cargo1= Cargo ()
print("cargo1",cargo1.codigo,cargo1.descripcion)

cargo2=Cargo()
cargo2.codigo=1
cargo2.descripcion="docente"
print("cargo2",cargo2.codigo,cargo2.descripcion)

cargo3 = Cargo()
cargo3.descripcion="conserje"
print("cargo3",cargo3.codigo,cargo3.descripcion)