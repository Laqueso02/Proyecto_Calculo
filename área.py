#Karen Vanessa Bautista Joaqui
#Cálculo de integrales
#Área
import numpy as np
from scipy.integrate import quad

# Definir la función g(x)
# Esta función está definida en el intervalo [0, 40] y devuelve la expresión de g(x)
def g(x):
    if 0 <= x <= 40:  # Condición para asegurarnos de que solo calcule dentro del intervalo válido
        return -0.16 * x**2 + 2.69 * x  # Expresión de la función g(x)
    return np.nan  # Fuera del intervalo, devuelve NaN para evitar cálculos indebidos

# Definir la función f(x)
# Representa la función f(x) dada en el intervalo [17.15, 23.98]
def f(x):
    return -0.12 * x**2 + 4.74 * x - 27.12  # Expresión cuadrática de f(x)

# Definir la función e(x)
# Representa la función e(x) dada en el intervalo [17.15, 23.98]
def e(x):
    return -2.57 * x**2 + 105.52 * x - 1035.01  # Expresión cuadrática de e(x)

# Intervalos de integración
interval_g = (0, 40)  # Intervalo para la función g(x)
interval_ef = (17.15, 23.98)  # Intervalo común para las funciones e(x) y f(x)

# Fórmula para calcular el área bajo la curva de g(x)
def area_g(x):
    return g(x)  # Simplemente devuelve g(x), ya que estamos calculando el área bajo su curva

# Fórmula para calcular el área entre e(x) y f(x)
def area_ef(x):
    return abs(e(x) - f(x))  # Calcula el valor absoluto de la diferencia entre e(x) y f(x)

# Calcular las áreas
# Para g(x): Se usa quad para calcular la integral definida en el intervalo correspondiente
area_g_value, _ = quad(area_g, *interval_g)  # *interval_g descompone (0, 40) en a=0, b=40
# Para e(x) y f(x): Calcula la integral de la función |e(x) - f(x)| en su intervalo
area_ef_value, _ = quad(area_ef, *interval_ef)  # *interval_ef descompone (17.15, 23.98)

# Mostrar resultados
print(f"Área bajo la curva g(x) en el intervalo {interval_g}: {area_g_value:.4f} unidades cuadradas")
# Imprime el área calculada bajo g(x), con 4 decimales

print(f"Área entre las curvas e(x) y f(x) en el intervalo {interval_ef}: {area_ef_value:.4f} unidades cuadradas")
# Imprime el área entre las curvas e(x) y f(x), con 4 decimales

# Área total combinada
# Calcula la suma de las áreas, si se desea mostrar como un total general
total_area = area_g_value + area_ef_value
print(f"Área total combinada: {total_area:.4f} unidades cuadradas")
# Imprime el área total combinada de g(x) y el área entre e(x) y f(x)
