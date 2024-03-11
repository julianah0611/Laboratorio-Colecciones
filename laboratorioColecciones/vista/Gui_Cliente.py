from tkinter import ttk

from laboratorioColecciones.modelo.Cliente import Cliente
from laboratorioColecciones.utils.PersistenciaUtils import Persistencia

class ClienteGUI:
    def __init__(self, master, empresa):

        self.master = master
        self.empresa = empresa

        master.title("Registro de Clientes")

        # Crear un marco con bordes y estilos similares al menú principal
        self.marco = ttk.Frame(master, padding="20")
        self.marco.configure(relief="raised", borderwidth=2)
        self.marco.grid(row=0, column=0, padx=50, pady=50)

        style = ttk.Style()
        style.configure('Titulo.TLabel', font=('Arial', 12,), background="#f0f0f0")
        style.configure('Boton.TButton', font=('Arial', 13), background="#cccccc", width=20)

        self.label_nIdent = ttk.Label(self.marco, text="Número de Identificación:", style='Titulo.TLabel')
        self.entry_nIdent = ttk.Entry(self.marco)

        self.label_nombre = ttk.Label(self.marco, text="Nombre:", style='Titulo.TLabel')
        self.entry_nombre = ttk.Entry(self.marco)

        self.label_direccion = ttk.Label(self.marco, text="Dirección:", style='Titulo.TLabel')
        self.entry_direccion = ttk.Entry(self.marco)

        self.submit_button = ttk.Button(self.marco, text="Registrar Cliente", style='Boton.TButton', command=self.registrar_cliente)
        style.configure('FondoAzul.TButton', background='#87CEEB')
        self.submit_button.configure(style='FondoAzul.TButton',)

        self.result_label = ttk.Label(self.marco, text="", wraplength=400)

        # Organizando widgets en el marco
        self.label_nIdent.grid(row=0, column=0, sticky="W", pady=2)
        self.entry_nIdent.grid(row=0, column=1, pady=2)

        self.label_nombre.grid(row=1, column=0, sticky="W", pady=2)
        self.entry_nombre.grid(row=1, column=1, pady=2)

        self.label_direccion.grid(row=2, column=0, sticky="W", pady=2)
        self.entry_direccion.grid(row=2, column=1, pady=2)

        self.submit_button.grid(row=3, column=0, columnspan=2, pady=5)
        self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

    def registrar_cliente(self):

        nIdent = self.entry_nIdent.get()
        nombre = self.entry_nombre.get()
        direccion = self.entry_direccion.get()

        cliente = Cliente(nIdent, nombre, direccion)
        resultado = self.empresa.agregarCliente(cliente)
        self.result_label.config(text=resultado)

        print(self.empresa.clientes)
        Persistencia.guardar(self.empresa)

