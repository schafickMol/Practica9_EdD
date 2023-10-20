class CuentaUsuario:
    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad} realizado con éxito.")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado con éxito.")
        elif cantidad > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")

    def obtener_saldo(self):
        return f"Saldo actual en la cuenta de {self.nombre}: ${self.saldo}"

if __name__ == "__main__":
    cuenta = CuentaUsuario("Juan Pérez", 1000)
    print(cuenta.obtener_saldo())

    cuenta.depositar(500)
    print(cuenta.obtener_saldo())

    cuenta.retirar(200)
    print(cuenta.obtener_saldo())

    cuenta.retirar(2000)