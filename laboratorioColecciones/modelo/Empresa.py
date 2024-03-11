#importaciones

from laboratorioColecciones.modelo.Venta import Venta


class Empresa:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Empresa, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self, nombre="MiEmpresa", nit="123456789"):
        self.nombre = nombre
        self.nit = nit
        self.clientes = {} #Diccionario de clientes equivalente al hashmap de JAVA (Colecion de clave-valor)
        self.productos = {} #Diccionario de productos equivalente al hashmap de JAVA (Colecion de clave-valor)
        self.carritosCompra = {} #Diccionario de carritos equivalente al hashmap de JAVA (Colecion de clave-valor)
        self.inventario = {}  #Diccionario de inventario equivalente al hashmap de JAVA (Colecion de clave-valor)  manejando una funcion de sort para que se asemeje a la forma de un Treeset, sin tener un funcionamiento tal a  este item
        self.ventas = {}


  #Funcion para agregar un cliente a la empresa
    def agregarCliente(self, cliente):
        if self.clientes.get(cliente.nIdent) != None:
            return "Error: El Cliente ya se encuentra registrado"
        else:
            self.clientes[cliente.nIdent] = cliente
            return "Cliente agregado exitosamente"

  #Funcion para remover un cliente de la empresa
    def removerCliente(self, nIdent):
        self.clientes.pop(nIdent)

  #Funcion para buscar un cliente en la empresa por medio del número de documento
    def buscarCliente(self, nIdent):
        return self.clientes.get(nIdent)

  #Funcion para agregar un producto a la empresa
    def agregarProducto(self, producto, cantidad=1):

        #Verificar si existe el codigo del producto
        if producto.codigo not in self.productos:
            #Si no existe agregar con cantidad 1 al inventario
            self.productos[producto.codigo] = producto
            self.inventario[producto.codigo] = cantidad
            return "Producto agregado exitosamente"
        else:
            #Si existe agregar una cantidad al inventario
            self.inventario[producto.codigo] += cantidad
            return "El producto ya se encuentra registrado, aumentar cantidad en 1"

  #Funcion para remover un producto de la empreas
    def removerProducto(self, codigo):
        self.productos.pop(codigo)
        self.inventario.pop(codigo)
        self.ordenarInventario()

  #Funcion para buscar un producto en la empresa por medio del código
    def buscarProducto(self, codigo):
        return self.productos.get(codigo)

  #Funcion que actualiza la cantidad de un producto en el inventario
    def actualizarInventario(self, codigo, cantidad):
        self.inventario[codigo] = cantidad
        self.ordenarInventario()

  #Funcion que aumenta la cantidad del inventario de un producto
    def entradasInventario(self, producto, cantidad):
        self.inventario[producto.codigo] += cantidad
        self.ordenarInventario()

  #Funcion que reduce la cantidad del inventario de un producto
    def salidasInventario(self, producto, cantidad):
        if  self.inventario[producto.codigo] - cantidad < 0:
            self.inventario[producto.codigo] = 0
        else:
            self.inventario[producto.codigo] -= cantidad
            self.ordenarInventario()

  #Funcion para ordenar el inventario de forma ascendente de tal manera que asemeje el funcionamiento de un setTree
    def ordenarInventario(self):
        self.inventario = dict(sorted(self.inventario.items(), key=lambda inve: inve[1]))

  #Funcion para agregar un carrito de compra a la empresa
    def agregarCarrito(self, carrito):
        if self.carritosCompra.get(carrito.codigo) != None:
            self.carritosCompra[carrito.codigo] = carrito

  #Funcion para remover un carrito de la empresa
    def removerCarrito(self, codigo):
        if self.carritosCompra.get(codigo) != None:
            self.carritosCompra.pop(codigo)

  #Funcion para buscar un carrito de la empresa por medio del código
    def buscarCarrito(self, codigo):
        return self.carritosCompra.get(codigo)

  #Funcion para agregar una venta
    def agregarVenta(self, venta):
        self.ventas[Venta.seq] = venta
        self.ordenarVentaCronologicamente()

  #función que busca ordenar cronologicamente las ventas, simulando un linkedlist de java mediante un diccionario, poniendo el uimo elemento como la raiz o cabeza de la lista
    def ordenarVentaCronologicamente(self):
        self.ventas = dict(sorted(self.ventas.items(), key=lambda venta: venta, reverse= True ))
