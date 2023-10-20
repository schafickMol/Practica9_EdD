class Articulo:
    def __init__(self, articulo, cantidad, precio):
        self.nombre = articulo
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            print(f"Se han vendido {cantidad_vendida} unidades de {self.nombre}.")
        else:
            print(f"No hay suficiente stock de {self.nombre} para la venta.")

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

if __name__ == "__main__":
    articulo1 = Articulo("Camiseta", 50, 15.99)
    print(articulo1.obtener_informacion())

    articulo1.vender(10)
    print(articulo1.obtener_informacion())

    articulo1.vender(60)