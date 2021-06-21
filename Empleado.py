from Cargo2 import Cargo

class Empleado:
    secuencia=0
    def __init__(self,nom="",sue="",car=None):

        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.sueldo=sue
        self.cargoEmp=car

    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia

    def mostrar(self):
        print("codigo;{} Nombre:{} Cargo({}):{}".format(self.codigo,self.nombre,self.cargoEmp.codigo,self.cargoEmp.descripcion))

cargo1=Cargo("Docente")
emp1=Empleado("Daniel",1000,cargo1)
emp1.mostrar()
emp2=Empleado("Josue",1000,cargo1)
emp2.mostrar()