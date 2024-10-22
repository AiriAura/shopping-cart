class Carro:
    #funcion contructora
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self,producto):
        self.lista_productos.append(producto)

    def quitar_producto(self, producto):
        self.lista_productos.remove(producto)

    def vaciar_carro(self):
        self.lista_productos = []

    def mostrar_carro(self):
        for producto in self.lista_productos:
            print(f"""
               Nombre: {producto.nombre_producto}
               Precio: {producto.precio}
               Cantidad: {producto.cantidad}
            """)