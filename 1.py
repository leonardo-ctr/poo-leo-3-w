class Persona:
    def __init__(self, nombre="", edad=None, DNI=""):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def set_nombre(self, nombre):
        if nombre: self.nombre = nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0: self.edad = edad

    def set_DNI(self, DNI):
        if len(DNI) == 9: self.DNI = DNI

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.DNI}")

    def es_mayor_de_edad(self):
        return self.edad >= 19


# Ejemplo de uso
persona = Persona("Najera Bañuelos", 29, "23465456554546a5423")
persona.mostrar()
print("Mayor de edad:", persona.es_mayor_de_edad())
