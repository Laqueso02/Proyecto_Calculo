import numpy as np
from scipy.integrate import quad

# Definir la función g(x)
def g(x):
    if 0 <= x <= 40:  # Intervalo de definición para g(x)
        return -0.16 * x**2 + 2.69 * x  # Expresión de g(x)
    return np.nan  # Fuera del intervalo, devuelve NaN

# Definir la función f(x)
def f(x):
    return -0.12 * x**2 + 4.74 * x - 27.12  # Expresión de f(x)

# Definir la función e(x)
def e(x):
    return -2.57 * x**2 + 105.52 * x - 1035.01  # Expresión de e(x)

# Intervalos de integración
interval_g = (0, 40)  # Intervalo para g(x)
interval_ef = (17.15, 23.98)  # Intervalo común para e(x) y f(x)

# Función para calcular el volumen de revolución de una función sobre un intervalo
def volume_of_revolution(func, a, b):
    """
    Calcula el volumen de revolución alrededor del eje X
    usando la fórmula de discos: π ∫[a, b] (func(x))^2 dx.
    """
    integral, _ = quad(lambda x: func(x) ** 2, a, b)  # Integral de func(x)^2
    return integral * np.pi  # Multiplica por π para obtener el volumen

# Función para calcular el volumen de revolución entre dos funciones
def volume_between_functions(func1, func2, a, b):
    """
    Calcula el volumen de revolución alrededor del eje X
    entre dos funciones, usando la fórmula de arandelas:
    π ∫[a, b] (func1(x)^2 - func2(x)^2) dx.
    """
    integral, _ = quad(lambda x: func1(x) ** 2 - func2(x) ** 2, a, b)
    return integral * np.pi  # Multiplica por π para obtener el volumen

# Calcular los volúmenes
# Volumen de revolución para g(x)
volume_g = volume_of_revolution(g, *interval_g)

# Volumen de revolución entre e(x) y f(x)
volume_ef = volume_between_functions(e, f, *interval_ef)

# Mostrar resultados
print(f"Volumen del sólido de revolución generado por g(x) en el intervalo {interval_g}: {volume_g:.4f} unidades cúbicas")
print(f"Volumen del sólido de revolución entre e(x) y f(x) en el intervalo {interval_ef}: {volume_ef:.4f} unidades cúbicas")

# Volumen total combinado
total_volume = volume_g + volume_ef
print(f"Volumen total combinado: {total_volume:.4f} unidades cúbicas")

