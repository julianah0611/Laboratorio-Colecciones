class DetallesVenta:
  def __init__(self, cantidad, subtotal, producto):
    self.cantidad = cantidad
    self.subtotal = subtotal
    self.producto = producto

  def __str__(self):
    return f"Cantidad: {self.cantidad} - Subtotal: {self.subtotal} - Producto: {self.producto}"