class Tarea:

    def __init__(self, nombre):
        self.nombre = nombre
        self.completada = False

    def completar(self):
        self.completada = True
