from datetime import datetime

class Venta:

  seq = 0

  def __init__(self, codigo, cliente, total, detalles):
    self.codigo = codigo
    self.fecha = datetime.now()
    self.total = total
    self.detalles = detalles
    self.cliente = cliente
    Venta.seq = Venta.seq + 1

  def __str__(self):
      return f"Codigo: {self.codigo} - {self.cliente} - Fecha: {self.fecha} -  Total: {self.total}"
