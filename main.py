# Programacion orientada a objetos
# Implica crear entidades (involucrados en el programa) que va a "esconder" las complejidades del codigo
# Su objetivo es organizar la información de forma que quienes están impplicados en el desarrollo entiendan mucho mejor como trabajar

# Los diccionarios. Los diccionarios es una forma de organizar la información
# Carro de compras

#             caracteristicas/atributos
# Usuario ->  nombre completo
#             email
#             tarjeta credito
#
#             acciones/metodos
#             comprar  
#             
# 
#             caracteristicas/atributos
# Producto -> nombre_producto
#             precio
#             cantidad  
#             marca
#             categoria
#
#             acciones/metodos
#               
#
#
# Carro   -> guarda una lista Productos
#            se relaciona a un Usuario
#           
#            acciones/metodos
#            agregar producto
#            quitar producto
#            vaciar carro

from shopping_cart.user import Usuario
from shopping_cart.product import Producto
from shopping_cart.cart import Carro

carro_compras = Carro()
user = Usuario("Gonzalo Pincheira", "gonzalo.pincheira@soymas.cl", "11223334")

producto1 = Producto("mantequilla", 1450, 2, "colun", "lacteos")
producto2 = Producto("manjar", 1500, 1, "soprole", "lacteos")
producto3 = Producto("naranjas", 850, 2, "frutos del maipo", "frutas")

carro_compras.agregar_producto(producto2)
carro_compras.agregar_producto(producto1)
carro_compras.agregar_producto(producto3)

carro_compras.mostrar_carro()