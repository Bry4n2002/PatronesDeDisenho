from emsamblador import Ensamblador
from builder_computador import BuilderComputadorGaming,BuilderComputadorOficina
from patrones.builder.emsamblador import Ensamblador

em =Ensamblador()
builder_gaming = BuilderComputadorGaming()
computador_gaming = em.contruct_computador(builder_gaming)
print(computador_gaming)

builder_oficina = BuilderComputadorOficina()
computador_oficina = em.contruct_computador(builder_oficina)
print(computador_oficina)