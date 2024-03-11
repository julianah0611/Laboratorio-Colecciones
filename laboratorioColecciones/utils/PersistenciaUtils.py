import pickle

class Persistencia:

    def cargar():
        try:
            with open('persistencia/inventario.pkl', 'rb') as file:
                if file.readable() and not file.read(1):
                    return None
                file.seek(0)
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return None

    def guardar(clase):
        with open('persistencia/inventario.pkl', 'wb') as file:
            return pickle.dump(clase, file)
