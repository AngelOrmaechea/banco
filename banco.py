class persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class cliente(persona):
    def __init__(self, nombre, apellido, num_cuenta, saldo = 0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def __str__(self):
        return f"Cliente:{self.nombre} {self.apellido}\nBalance de cuenta {self.num_cuenta}: ${self.saldo}"

    def depositar(self, ingreso):
        self.saldo += ingreso
        print("Deposito realizado.")

    def retirar(self, retiro):
       if self.saldo >= retiro:
           self.saldo -= retiro
           print(f"Has retirado con exito ${retiro}")
       else:
           print("Cantidad no valida.")



def crear_cliente():
    nombre_cl = input("ingrese su nombre: ")
    apellido_cl = input("ingrese su apellido: ")
    num_cuenta_cl = input("ingrese su numero de cuenta: ")
    Cliente = cliente(nombre_cl, apellido_cl, num_cuenta_cl)
    return Cliente


def inicio():
    mi_clie = crear_cliente()
    print(mi_clie)
    opcion = 0

    while opcion != "S":
        print("Elige una opcion: Depositar (D), Retirar (R), Salir (S)")
        opcion = input().upper()

        if opcion == "D":
            ingreso = int(input("ingrese la cantidad a depositar: "))
            mi_clie.depositar(ingreso)
        elif opcion == "R":
            reti = int(input("Ingrese cantidad a retirar: "))
            mi_clie.retirar(reti)
        print(mi_clie)
    print("Gracias, vuelva pronto.")


inicio()
