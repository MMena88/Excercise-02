import math

listaTransacciones = []
class Finanzas:
    def __init__(self, balance):
        self.balance = balance

    def ingreso(self, monto):
        self.balance += monto

    def egreso(self, monto):
        self.balance -= monto

    def get_balance(self):
        return self.balance   
cuenta = 0
opcion = 0

while opcion <=6:
    print("\t.:MENU:.")
    print("1. Ingresar dinero a la cuenta")
    print("2. Egresar dinero de la cuenta")
    print("3. Verificar ingresos")
    print("4. verificar egresos")
    print("5. Mostrar dinero disponible")
    print("6. Salir")
    opcion = int(input("Digite una opcion del menu: "))
    if opcion==1:
       ingreso = float(input("Cuanto dinero desea ingresar?-"))
       cuenta += ingreso
       print(f"Dinero en la cuenta: {cuenta}")
    elif opcion==2:
       egreso = float(input("Cuanto dinero desea egresar?-"))
       cuenta -= egreso
       print(f"Dinero en la cuenta: {cuenta}")
    elif opcion==3:
       conteo = {"Su lista de ingresos es":ingreso}
       listaTransacciones.append(conteo)
       for egreso in listaTransacciones:
            print(conteo)
    elif opcion==4:
        conteo2 = {"Su lista de egresos es":egreso} 
        listaTransacciones.append(conteo2)   
        for conteo2 in listaTransacciones:
            print(conteo2)    
    elif opcion==5:
       print(f"Dinero en la cuenta: {cuenta}")
    elif opcion==6:
       print("Gracias por utilizar nuestra red de finanzas! tenga un feliz dia")
    if opcion == 6:
        break   





