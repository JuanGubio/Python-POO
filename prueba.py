class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def describir(self):
        print(f"Este coche es un {self.marca} {self.modelo}.")

    def arrancar(self):
        self.encendido = True
        print("El coche está encendido.")

    def apagar(self):
        self.encendido = False
        print("El coche está apagado.")


mi_coche = Coche("Toyota", "Corolla")
mi_coche.describir()
mi_coche.arrancar()
mi_coche.apagar()
