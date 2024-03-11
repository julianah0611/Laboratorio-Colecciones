import tkinter as tk
from tkinter import ttk, messagebox
from laboratorioColecciones.modelo.DetallesVenta import DetallesVenta
from laboratorioColecciones.modelo.Venta import Venta
from laboratorioColecciones.utils.PersistenciaUtils import Persistencia

class VentaGUI:
    def __init__(self, master, empresa):

        self.master = master
        self.empresa = empresa
        self.clientes = self.inicializar_clientes()
        self.productos = self.inicializar_producto()

        master.title("Registro de Ventas")

        # Creación de widgets
        self.label_codigo = ttk.Label(master, text="Código:")
        self.entry_codigo = ttk.Entry(master)

        self.label_cliente = ttk.Label(master, text="Cliente:")
        self.combo_cliente = ttk.Combobox(master, values=self.clientes, state="readonly")
        self.combo_cliente.bind("<<ComboboxSelected>>", self.seleccionar_cliente)

        self.label_total = ttk.Label(master, text="Total:")
        self.entry_total = ttk.Entry(master)

        self.submit_button = ttk.Button(master, text="Registrar Venta", command=self.registrar_venta)
        self.result_label = ttk.Label(master, text="", wraplength=400)

        # Marco para detalles
        self.frame_detalles = ttk.LabelFrame(master, text="Detalles")
        self.label_cantidad = ttk.Label(self.frame_detalles, text="Cantidad:")
        self.label_subtotal = ttk.Label(self.frame_detalles, text="Subtotal:")
        self.label_producto = ttk.Label(self.frame_detalles, text="Producto:")
        self.entry_cantidad = ttk.Entry(self.frame_detalles)
        self.entry_subtotal = ttk.Entry(self.frame_detalles)
        self.combo_producto = ttk.Combobox(self.frame_detalles, values=self.productos, state="readonly")
        self.combo_producto.bind("<<ComboboxSelected>>", self.seleccionar_producto)
        self.button_agregar_detalle = ttk.Button(self.frame_detalles, text="Agregar Detalle",
                                                 command=self.agregar_detalle)

        # Configuración de Treeview para los detalles
        self.tree = ttk.Treeview(master, columns=('Cantidad', 'Subtotal', 'Producto'), show='headings')
        self.tree.heading('Cantidad', text='Cantidad')
        self.tree.heading('Subtotal', text='Subtotal')
        self.tree.heading('Producto', text='Producto')

        # Scrollbar para el Treeview
        self.scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)

        # Organizando widgets en la ventana
        self.label_codigo.grid(row=0, column=0, sticky="W", pady=2)
        self.entry_codigo.grid(row=0, column=1, pady=2)

        self.label_cliente.grid(row=1, column=0, sticky="W", pady=2)
        self.combo_cliente.grid(row=1, column=1, pady=2)

        self.label_total.grid(row=2, column=0, sticky="W", pady=2)
        self.entry_total.grid(row=2, column=1, pady=2)

        self.frame_detalles.grid(row=3, column=0, columnspan=2, pady=5, sticky='ew')
        self.label_cantidad.grid(row=0, column=0, sticky="W", pady=2)
        self.label_subtotal.grid(row=1, column=0, sticky="W", pady=2)
        self.label_producto.grid(row=2, column=0, sticky="W", pady=2)
        self.entry_cantidad.grid(row=0, column=1, pady=2)
        self.entry_subtotal.grid(row=1, column=1, pady=2)
        self.combo_producto.grid(row=2, column=1, pady=2)
        self.button_agregar_detalle.grid(row=3, column=0, columnspan=2, pady=2)

        self.tree.grid(row=4, column=0, columnspan=2, sticky='nsew')
        self.scrollbar.grid(row=4, column=2, sticky='ns')

        self.submit_button.grid(row=5, column=0, columnspan=2, pady=5)
        self.result_label.grid(row=6, column=0, columnspan=2, pady=5)

        # Lista para almacenar objetos DetallesVenta
        self.detalles_ventas = []

    def inicializar_clientes(self):
        clientes = [f"{cliente.nIdent} - {cliente.nombre}" for cliente in self.empresa.clientes.values()]
        return clientes

    def inicializar_producto(self):
        productos = [f"{producto.codigo} - {producto.nombre}" for producto in self.empresa.productos.values()]
        return productos

    def agregar_detalle(self):
        try:
            cantidad = int(self.entry_cantidad.get())
            subtotal = float(self.entry_subtotal.get())
            producto = self.combo_producto.get()
            detalle = DetallesVenta(cantidad, subtotal, self.producto_seleccionado)
            self.detalles_ventas.append(detalle)

            # Actualizar el Treeview con el nuevo detalle
            self.tree.insert('', 'end', values=(detalle.cantidad, detalle.subtotal, detalle.producto))

            # Limpiar campos después de agregar
            self.entry_cantidad.delete(0, tk.END)
            self.entry_subtotal.delete(0, tk.END)
            self.combo_producto.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Cantidad y subtotal deben ser numéricos.")

    def registrar_venta(self):

        codigo = self.entry_codigo.get()
        cliente = self.combo_cliente.get()
        try:
            total = float(self.entry_total.get())
        except ValueError:
            self.result_label.config(text="El total debe ser un número.")
            return

        detalles = self.detalles_ventas

        venta = Venta(codigo, self.cliente_seleccionado, total, detalles)

        self.empresa.agregarVenta(venta)

        self.result_label.config(text=str(venta))

        Persistencia.guardar(self.empresa)

    def seleccionar_cliente(self, event):
        seleccion = self.combo_cliente.get()
        clave_seleccionada = seleccion.split(" - ",1)[0]
        self.cliente_seleccionado = self.empresa.clientes.get(clave_seleccionada)

    def seleccionar_producto(self, event):
        seleccion = self.combo_producto.get()
        clave_seleccionada = seleccion.split(" - ",1)[0]
        self.producto_seleccionado = self.empresa.productos.get(clave_seleccionada)
