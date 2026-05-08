class Computador:
    def __init__(self):
        self.procesador = None
        self.ram = None
        self.almacenamiento = None
        self.tarjeta_grafica = None

    def __str__(self):
        return f"Computador(procesador={self.procesador}, ram={self.ram}, almacenamiento={self.almacenamiento}, tarjeta_grafica={self.tarjeta_grafica})"