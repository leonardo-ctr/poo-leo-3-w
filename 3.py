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


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def esTitularValido(self, edad):
        return 18 <= edad < 25

    def mostrar(self):
        print(f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad}€, Bonificación: {self.bonificacion}%")

    def retirar(self, cantidad, edad):
        if self.esTitularValido(edad):
            super().retirar(cantidad)
        else:
            print("Titular no válido para retiro.")


# Ejemplo de uso
cuenta_joven = CuentaJoven("piratita de culiacan", 1000.0, 5.0)
cuenta_joven.mostrar()
cuenta_joven.retirar(100, 20)
cuenta_joven.mostrar()
cuenta_joven.retirar(100, 26)
cuenta_joven.mostrar()
