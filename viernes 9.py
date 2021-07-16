# Rolando Josue Quijije Banchon
# Software
# #Tercer semestre

#clase viernes 9 de julio 
class ordenar:
    def _init_(self,lista):
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

    def insertar(self,num):
        self.ordenarasc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break

        self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]

    def insertarorden(self,num):
        self.lista.append(num)
        self.ordenarasc()

lista=[2,3,8,10]
ord1= ordenar(lista)
print(ord1.insertar(5))
print(ord1.lista)
##################################################
class ordenar:
    def _init_(self,lista):
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

    def insertar(self,num):
        self.ordenarasc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break

        self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]
    
    def insertar(self,num):
        self.ordenarasc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                break
        for i in range(pos):
            auxlista.append(self.lista[i])
        auxlista.append(num)

        for j in range(pos,len(self.lista)):
            auxlista.append(self.lista[j])
        self.lista=auxlista



    def insertarorden(self,num):
        self.lista.append(num)
        self.ordenarasc()


    def eliminar(self,num):
        for pos,ele in enumerate(self.lista):
            if num==ele:
                break
        self.lista=self.lista[0:pos]+self.lista[pos+1:]
lista=[2,3,8,10]
ord1= ordenar(lista)
print(ord1.insertar(5))
print(ord1.lista)

##################################################
class ordenar:
    def _init_(self,lista):
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

    def insertar(self,num):
        self.ordenarasc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break

        self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]
    
    def insertar(self,num):
        self.ordenarasc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                break
        for i in range(pos):
            auxlista.append(self.lista[i])
        auxlista.append(num)

        for j in range(pos,len(self.lista)):
            auxlista.append(self.lista[j])
        self.lista=auxlista



    def insertarorden(self,num):
        self.lista.append(num)
        self.ordenarasc()


    def eliminar(self,num):
        enc=False
        for pos,ele in enumerate(self.lista):
            if num==ele:
                enc=True
                break
        if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
        return enc

lista=[2,3,8,10]
ord1= ordenar(lista)
if ord1.eliminar(8)==True: print("el numero se elimino de la lista",ord1.lista)
else: print("el numero nose encuentra en la lista")