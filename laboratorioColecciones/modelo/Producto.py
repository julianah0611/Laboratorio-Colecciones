class Producto:
  def __init__(self, codigo, nombre, precio):
    self.codigo = codigo
    self.nombre = nombre
    self.precio = float(precio)  # Convertir a float para manejar el precio como número

  def __str__(self):
    return f"Producto: {self.nombre} - {self.codigo} - {self.precio}"
