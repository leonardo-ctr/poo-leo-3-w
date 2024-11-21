class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad}€")

    def ingresar(self, cantidad):
        if cantidad > 0: self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0: self.cantidad -= cantidad


# Ejemplo de uso
persona = "pirata de culiacan"
cuenta = Cuenta(persona, 7877.0)

cuenta.mostrar()
cuenta.ingresar(523)
cuenta.mostrar()
cuenta.retirar(879)
cuenta.mostrar()
