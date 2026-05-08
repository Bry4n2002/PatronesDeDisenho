# Cliente es el que utiliza el director para construir el objeto
from emsamblador import Ensamblador
from builder_computador import BuilderComputadorGaming,BuilderComputadorOficina

# El cliente utiliza el director para construir el objeto utilizando el builder
em =Ensamblador()
builder_gaming = BuilderComputadorGaming()
computador_gaming = em.contruct_computador(builder_gaming)
print(computador_gaming)

# El cliente puede utilizar el mismo director para construir diferentes objetos utilizando diferentes builders
builder_oficina = BuilderComputadorOficina()
computador_oficina = em.contruct_computador(builder_oficina)
print(computador_oficina)