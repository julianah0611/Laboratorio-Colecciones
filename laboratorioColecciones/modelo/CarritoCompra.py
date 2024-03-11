from laboratorioColecciones.modelo.Cliente import Cliente
from laboratorioColecciones.modelo.Producto import Producto


class CarritoCompra:

  def __init__(self, codigo, cliente):
    self.codigo = codigo
    self.cliete = cliente
    self.productos = set()  # Coleccion en python equivalente al HashSet de JAVA
    self.detalles = {} # Diccionario para crear una implementación los detalles del carrito de compra
  
  def agregarActualizarProducto(self, producto):
    self.productos.add(producto)
    self.detalles[producto.codigo] = [1,producto.precio]
    #print(self.productos)

  def removerProducto(self, producto):
    self.productos.discard(producto)
    self.detalles.pop(producto.codigo)
    #print(self.productos)

  def actualizarDetalles(self, producto, cantidad):
    self.detalles[producto.codigo] = [cantidad, producto.precio*cantidad]
