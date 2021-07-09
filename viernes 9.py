# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#clase viernes 9 de julio 
class ordenar:
    def _init_(self,lista):
        self.lista=lista

    def ordenarAsc(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista [pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]= self.lista[sig]
                    self.lista[sig]= aux

    def insertar (self,num):
        self.ordenarAsc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break
        self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]
        return pos





lista=[2,3,8,10]
ord1 = ordenar(lista)
print(ord1.insertar(5))
print(ord1.list)
