# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#clase Lunes 5 de julio 
class ordenar:
    def __init__(self,lista):
         self.lista=lista
    
    def recorrerelemento(self):
        for ele in self.lista:
            print(ele)

    def recorrerenumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
    
    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])
    
    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:
           return pos
        else:
            return -1
    
    def ordenarasc(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos]> self.lista[sig]:
                    aux=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def ordenardes(self):
        for pos,ele in enumerate(self.lista):
            #ele=2 pos=0
            for sig in range(pos+1,len(self.lista)):
                #3,1,5,8,10  #sig=3
                if ele< self.lista[sig]:
                    aux=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def primer(self):
        return self.lista[0]

    def primereliminado(self):
        primer=self.lista[0]
        auxlista=[]
        for pos in range(1,len(self.lista)):
            auxlista.append(self.lista(pos))
        self.lista=auxlista
        return primer
    
    def primereliminado2(self):
        primer=self.lista[0]
        self.lista=self.lista[1:]
        return primer


    def ultimo(self):
        return self.lista[-1]

    def ultimoeliminado(self):
        ultimo=self.lista[-1]
        auxlista=[]
        for pos in range(0,len(self.lista)-1):
            auxlista.append(self.lista(pos))
        self.lista=auxlista
        return ultimo

    def ultimoeliminado2(self):
        ultimo = self.lista[-1]
        self.lista=self.lista[0:-1]
        return ultimo


lista=[2,3,1,5,8,10]
ord1= ordenar(lista)
print(ord1.lista)
print(ord1.ultimoeliminado())
print(ord1.lista)
####################################################################################################
class ordenar:
    def __init__(self,lista):
         self.lista=lista
    
    def recorrerelemento(self):
        for ele in self.lista:
            print(ele)

    def recorrerenumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
    
    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])
    
    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:
           return pos
        else:
            return -1
    
    def ordenarasc(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos]> self.lista[sig]:
                    aux=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def ordenardes(self):
        for pos,ele in enumerate(self.lista):
            #ele=2 pos=0
            for sig in range(pos+1,len(self.lista)):
                #3,1,5,8,10  #sig=3
                if ele< self.lista[sig]:
                    aux=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def primer(self):
        return self.lista[0]

    def primereliminado(self):
        primer=self.lista[0]
        auxlista=[]
        for pos in range(1,len(self.lista)):
            auxlista.append(self.lista(pos))
        self.lista=auxlista
        return primer
    
    def primereliminado2(self):
        primer=self.lista[0]
        self.lista=self.lista[1:]
        return primer


    def ultimo(self):
        return self.lista[-1]

    def ultimoeliminado2(self):
        ultimo = self.lista[-1]
        self.lista=self.lista[0:-1]
        return ultimo


lista=[2,3,1,5,8,10]
ord1= ordenar(lista)
print(ord1.lista)
print(ord1.ultimoeliminado2())
print(ord1.lista)

##################################################################################
class ordenar:
    def __init__(self,lista):
         self.lista=lista
    
    def recorrerelemento(self):
        for ele in self.lista:
            print(ele)

    def recorrerenumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
    
    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])
    
    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:
           return pos
        else:
            return -1
    
    def ordenarasc(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos]> self.lista[sig]:
                    aux=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def ordenardes(self):
        for pos,ele in enumerate(self.lista):
            #ele=2 pos=0
            for sig in range(pos+1,len(self.lista)):
                #3,1,5,8,10  #sig=3
                if ele< self.lista[sig]:
                    aux=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def primer(self):
        return self.lista[0]

    def primereliminado(self):
        primer=self.lista[0]
        auxlista=[]
        for pos in range(1,len(self.lista)):
            auxlista.append(self.lista(pos))
        self.lista=auxlista
        return primer
    
    def primereliminado2(self):
        primer=self.lista[0]
        self.lista=self.lista[1:]
        return primer


    def ultimo(self):
        return self.lista[-1]

    def ultimoeliminado(self):
        ultimo=self.lista[-1]
        auxlista=[]
        for pos in range(0,len(self.lista)-1):
            auxlista.append(self.lista(pos))
        self.lista=auxlista
        return ultimo

    def ultimoeliminado2(self):
        ultimo = self.lista[-1]
        self.lista=self.lista[0:-1]
        return ultimo

    def insert(self):
        self.ordenarasc()


lista=[2,3,1,5,8,10]
ord1= ordenar(lista)
print(ord1.lista)
print(ord1.ultimoeliminado())
print(ord1.lista)