# Patrones de Diseño en Python 🎨

Un repositorio educativo que implementa y explica los principales patrones de diseño de software utilizando Python.

## Descripción

Este proyecto contiene ejemplos prácticos de los **patrones de diseño más utilizados y relevantes** en la industria del software. Cada patrón incluye su implementación en Python, explicaciones claras y casos de uso prácticos.

> **Nota**: Este repositorio se enfoca en los patrones de diseño más comúnmente usados en proyectos reales. Se omiten patrones menos frecuentes o situaciones muy específicas para mantener el contenido didáctico y aplicable.

## Patrones Incluidos

### Patrones Creacionales
- **Singleton**: Garantiza una única instancia de una clase
- **Factory Method**: Crea objetos sin especificar sus clases concretas
- **Builder**: Construye objetos complejos paso a paso

### Patrones Estructurales
- **Adapter**: Adapta interfaces incompatibles
- **Decorator**: Añade comportamiento dinámicamente
- **Facade**: Proporciona una interfaz simplificada
- **Proxy**: Proporciona un sustituto de otro objeto

### Patrones de Comportamiento
- **Observer**: Notifica a múltiples objetos sobre cambios de estado
- **Strategy**: Define una familia de algoritmos intercambiables
- **Command**: Encapsula solicitudes como objetos
- **State**: Permite cambiar el comportamiento según el estado
- **Template Method**: Define el esqueleto de un algoritmo

## Requisitos

- Python 3.7 o superior
- Ninguna dependencia externa (solo librerías estándar)

## Instalación

```bash
git clone https://github.com/Bry4n2002/PatronesDeDisenho.git
cd PatronesDeDisenho
```

## Estructura del Proyecto

```
PatronesDeDisenho/
├── creacionales/
│   ├── singleton
│   ├── factory
│   └── builder
├── estructurales/
│   ├── adapter
│   ├── decorator
│   ├── facade
│   └── proxy
├── comportamiento/
│   ├── observer
│   ├── strategy
│   ├── command
│   ├── state
│   ├── template_method
└── README.md
```

## Uso

Cada archivo de patrón contiene:
1. **Explicación del patrón**: Qué es y cuándo usarlo
2. **Implementación**: Código de ejemplo en Python
3. **Caso de uso**: Un ejemplo práctico de cómo utilizarlo

```python
# Ejemplo de uso
from creacionales.singleton import Singleton

# Primera instancia
app1 = Singleton()

# Segunda instancia (es la misma)
app2 = Singleton()

assert app1 is app2  # True
```

## Recursos Adicionales

- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) - Gang of Four
- [Refactoring.Guru - Design Patterns](https://refactoring.guru/design-patterns)
- [Real Python - Design Patterns](https://realpython.com/design-patterns-python/)

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes una mejora:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/mi-mejora`)
3. Commit tus cambios (`git commit -m 'Añado: mi mejora'`)
4. Push a la rama (`git push origin feature/mi-mejora`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

**Bryan** - [GitHub](https://github.com/Bry4n2002)

---

⭐ Si este repositorio te ha sido útil, considera darle una estrella!
