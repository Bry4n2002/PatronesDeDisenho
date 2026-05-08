from computador import Computador

class BuilderComputador:
    def __init__(self):
        self.computador = Computador()
    def get_result(self):
        return self.computador
    def set_procesador(self):
        raise NotImplementedError

    def set_ram(self):
        raise NotImplementedError

    def set_almacenamiento(self):
        raise NotImplementedError

    # opcional
    def set_tarjeta_grafica(self):
        pass
class BuilderComputadorGaming(BuilderComputador):
    def set_procesador(self):
        self.computador.procesador = 'Intel Core i9'
    def set_ram(self):
        self.computador.ram = '32GB'
    def set_almacenamiento(self):
        self.computador.almacenamiento = '1TB SSD'
    def set_tarjeta_grafica(self):
        self.computador.tarjeta_grafica = 'NVIDIA GeForce RTX 3080'

class BuilderComputadorOficina(BuilderComputador):
    def set_procesador(self):
        self.computador.procesador = 'Intel Core i5'
    def set_ram(self):
        self.computador.ram = '16GB'
    def set_almacenamiento(self ):
        self.computador.almacenamiento = '512GB SSD'
