import tkinter as tk
from tkinter import ttk
from laboratorioColecciones.vista.Gui_Venta import VentaGUI
from laboratorioColecciones.vista.Gui_Cliente import ClienteGUI
from laboratorioColecciones.utils.PersistenciaUtils import Persistencia
from laboratorioColecciones.modelo.Empresa import Empresa
from laboratorioColecciones.modelo.Producto import Producto

class MenuPrincipal(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.empresa = Persistencia.cargar()

        if  self.empresa != None:
            print("Estado inicial de la empresa cargada.")
        else:
            self.empresa = Empresa()

        self.master = master

        #Ruta del archivo donde se encuentran los productos
        archivo_productos = 'productos.txt'

        #Cargar masiva de productos
        self.cargar_productos(archivo_productos)

        self.configure(background="#f0f0f0")  # Color de fondo
        self.grid(row=0, column=0)

        self.marco = ttk.Frame(self, padding="20")  # Agregar bordes y espaciado interno al marco
        self.marco.configure(relief="raised", borderwidth=2)  # Estilo del borde
        self.marco.grid(row=0, column=0, padx=50, pady=50)

        style = ttk.Style()
        style.configure('Titulo.TLabel', font=('Arial', 15, 'bold'), background="#f0f0f0")  # Estilo para el título
        style.configure('Boton.TButton', font=('Arial', 12), background="#cccccc", width=20)  # Estilo para los botones, con ancho fijo de 20

        self.titulo_label = ttk.Label(self.marco, text="Menú Principal", style='Titulo.TLabel')
        self.titulo_label.grid(row=0, columnspan=2, pady=10)

        self.cliente_button = ttk.Button(self.marco, text="Agregar Clientes", style='Boton.TButton',
                                         command=self.abrir_cliente_gui)
        self.cliente_button.grid(row=1, column=0, padx=10, pady=5)

        self.venta_button = ttk.Button(self.marco, text="Agregar Ventas", style='Boton.TButton',
                                       command=self.abrir_venta_gui)
        self.venta_button.grid(row=2, column=0, padx=10, pady=5)

        self.venta_button = ttk.Button(self.marco, text="Visualizar Clientes", style='Boton.TButton',
                                       command=self.visualizar_clientes)
        self.venta_button.grid(row=3, column=0, padx=10, pady=5)

        self.venta_button = ttk.Button(self.marco, text="Visualizar Ventas", style='Boton.TButton',
                                       command=self.visualizar_ventas)
        self.venta_button.grid(row=4, column=0, padx=10, pady=5)

        self.visualizar_productos_button = ttk.Button(self.marco, text="Visualizar Productos", style='Boton.TButton',
                                                      command=self.visualizar_productos)
        self.visualizar_productos_button.grid(row=5, column=0, padx=10, pady=5)

        self.visualizar_inventario_button = ttk.Button(self.marco, text="Visualizar Inventario", style='Boton.TButton',
                                                      command=self.visualizar_inventario)
        self.visualizar_inventario_button.grid(row=6, column=0, padx=10, pady=5)

    def abrir_cliente_gui(self):
        top = tk.Toplevel(self.master)
        cliente_app = ClienteGUI(top, self.empresa)

    def abrir_venta_gui(self):
        top = tk.Toplevel(self.master)
        venta_app = VentaGUI(top, self.empresa)

    def visualizar_productos(self):
        # Crear una nueva ventana para mostrar los productos

        top = tk.Toplevel(self.master)
        top.title("Productos")

        # Crear un marco para mostrar los productos
        marco_productos = ttk.Frame(top, padding="20")
        marco_productos.grid(row=0, column=0)

        # Mostrar los productos cargados
        for i, producto in enumerate(self.empresa.productos.values()):
            label_producto = ttk.Label(marco_productos, text=str(producto))
            label_producto.grid(row=i, column=0, sticky="w", padx=10, pady=5)

    def visualizar_inventario(self):
        # Crear una nueva ventana para mostrar el inventario

        top = tk.Toplevel(self.master)
        top.title("Inventario")

        # Crear un marco para mostrar el inventario
        marco_inventario = ttk.Frame(top, padding="20")
        marco_inventario.grid(row=0, column=0)

        # Mostrar los productos cargados
        for i, producto in enumerate(self.empresa.productos.values()):
            label_inventario = ttk.Label(marco_inventario, text=f"{str(producto)} - Cantidad: {self.empresa.inventario.get(producto.codigo)}")
            label_inventario.grid(row=i, column=0, sticky="w", padx=10, pady=5)

    def visualizar_clientes(self):
        top = tk.Toplevel(self.master)
        top.title("Listado de Clientes")

        # Creando un marco dentro de la ventana emergente
        marco_clientes = ttk.Frame(top, padding="20")
        marco_clientes.grid(row=0, column=0, padx=10, pady=10)

        # Configuración del Treeview en la ventana emergente
        tree = ttk.Treeview(marco_clientes, columns=('nIdent', 'Nombre', 'Dirección'), show='headings')
        tree.heading('nIdent', text='Número de Identificación')
        tree.heading('Nombre', text='Nombre')
        tree.heading('Dirección', text='Dirección')
        tree.grid(row=0, column=0, sticky='nsew', pady=5)

        # Llenando el Treeview con los clientes actuales de la empresa
        for nIdent, cliente in self.empresa.clientes.items():
            tree.insert('', 'end', values=(cliente.nIdent, cliente.nombre, cliente.direccion))
    def visualizar_ventas(self):
        # Crear una nueva ventana para mostrar el inventario

        top = tk.Toplevel(self.master)
        top.title("Lista de ventas")

        # Crear un marco para mostrar el inventario
        marco_ventas = ttk.Frame(top, padding="20")
        marco_ventas.grid(row=0, column=0)

        # Mostrar los productos cargados
        for i, venta in enumerate(self.empresa.ventas.values()):
            label_ventas = ttk.Label(marco_ventas, text=str(venta))
            label_ventas.grid(row=i, column=0, sticky="w", padx=10, pady=5)

    def cargar_productos(self, archivo):
        with open(archivo, 'r') as file:
            for linea in file:
                partes = linea.strip().split(',')  # Dividir cada línea por coma y quitar espacios
                if len(partes) == 3:  # Asegurar que cada línea tenga exactamente 3 partes
                    producto = Producto(partes[0], partes[1], partes[2])
                    self.empresa.agregarProducto(producto)
