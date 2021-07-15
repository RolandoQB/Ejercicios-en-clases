class Ordenar:
    def __init__(self,lista):
        self.lista=lista
        
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
            
    def recorrerPosicion(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
    
    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])
            
    def buscar (self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele == buscado:
                enc=True
                break
        if enc == True:
            return pos
        else:
            return -1
    
    def ordenarAsce(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista [pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]= self.lista[sig]
                    self.lista[sig]= aux

    def ordenarDesc(self):
        for pos, ele in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if ele < self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
        


          
lista = [2,3,1,5,8,10]
ord1 = Ordenar(lista)

print(ord1.lista)
ord1.ordenarDesc()
print(ord1.lista)