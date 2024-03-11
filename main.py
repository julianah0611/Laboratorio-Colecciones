import tkinter as tk

from laboratorioColecciones.vista.Gui_Menu import MenuPrincipal

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


class App:

    def __init__(self, master):
        self.master = master
        master.title("Menú Principal")

        self.menu = MenuPrincipal(master)
        master.config(menu=self.menu)


if __name__ == "__main__":
    main()
