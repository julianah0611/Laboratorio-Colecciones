class Cliente:
  def __init__(self, nIdent, nombre, direccion):
    self.nIdent = nIdent
    self.nombre = nombre
    self.direccion = direccion

  def __str__(self):
      return f"Cliente: {self.nombre} - Identificación: {self.nIdent} - Dirección: {self.direccion}"
