

# def menu():
#     print("         Menu Principal")
#     print("1) Calculadora")
#     print("2) Numeros")
#     print("3) Listas")
#     print("4) Calculos")
#     print("5) Salir")
#     opc=input("Elija opcion[1....5]: ")
#     if opc == "1":
#         print("calculadora")


#     elif opc=="2":
#         print("Operaciones con Numeros")
#         print("   Menu Principal")
#         print("1) perfecto")
#         print("2) primo")
#         print("3) salir")
#         opc2=input("Elija opcion[1....3]: ")
#         if opc2 == "1":
#             print("numeros perfecto")
#             num= int(input("Ingrese numero"))
#             #llamar el metodo perfecto
#             print("el numero es perfecto")

#     elif opc=="3":
#         print("Listas")

#     elif opc=="4":
#         print("Cadenas")

#     elif opc=="5":
#         print("Cadenas")

#     else:
#         print("opcion no valida")
# menu()



class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc= input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc

men=Menu("Menu Principal",["1) Calculadora","2) Numeros","3) Listas","4) Calculos","5) Salir"])
opc=men.menu()
elif opc =="2":
        print("Operaciones con Numeros")
        print("   Menu Principal")
        print("1) perfecto")
        print("2) primo")
        print("3) salir")
        opc2=input("Elija opcion[1....3]: ")
        if opc2 == "1":
            print("numeros perfecto")
            num= int(input("Ingrese numero"))
            #llamar el metodo perfecto
            print("el numero es perfecto")

    elif opc=="3":
        print("Listas")

    elif opc=="4":
        print("Cadenas")

    elif opc=="5":
        print("Cadenas")

    else:
        print("opcion no valida")
men1=Menu("Menu Listas",["1) Recorrido","2) Buscar","3) Salir"])
opc1=men.menu()