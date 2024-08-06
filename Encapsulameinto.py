class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: {self.__saldo}"
        return "Cantidad no válida para depósito."

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: {self.__saldo}"
        return "Cantidad no válida para retiro."

    def obtener_saldo(self):
        return f"El saldo actual es: {self.__saldo}"


cuenta = CuentaBancaria("Juanpi", 1000)


print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.obtener_saldo())
