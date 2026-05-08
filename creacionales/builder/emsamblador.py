# Director es el encargado de construir el objeto utilizando el builder
from builder_computador import BuilderComputadorGaming,BuilderComputadorOficina


class Ensamblador:
    def construct_computador(self, builder):
        builder.set_procesador()
        builder.set_ram()
        builder.set_almacenamiento()
        builder.set_tarjeta_grafica()
        return builder.get_result()
