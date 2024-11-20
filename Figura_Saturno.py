import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las funciones del anillo
def g(x):
    return -0.16 * x**2 + 2.69 * x  # Esfera

def f(x):
    return -0.12 * x**2 + 4.74 * x - 27.12  # Parte inferior del anillo

def e(x):
    return -2.57 * x**2 + 105.52 * x - 1035.01  # Parte superior del anillo

# Crear datos para la esfera (Saturno)
def sphere(radius, center=(0, 0, 0), resolution=200):
    """
    Genera coordenadas para una esfera.
    radius: Radio de la esfera.
    center: Centro de la esfera (x, y, z).
    resolution: Número de divisiones para generar la esfera.
    """
    u = np.linspace(0, 2 * np.pi, resolution)  # Coordenadas angulares
    v = np.linspace(0, np.pi, resolution)
    x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
    return x, y, z

# Crear la figura
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d', azim=120, elev=30)

# Graficar la esfera (Saturno)
x_sphere, y_sphere, z_sphere = sphere(radius=10, center=(0, 0, 0))
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='saddlebrown', alpha=0.9, edgecolor='none')

# Crear el anillo como un área sólida
theta = np.linspace(0, 2 * np.pi, 500)  # Ángulo para generar un anillo circular
r_outer = 15  # Radio exterior del anillo
r_inner = 12  # Radio interior del anillo

# Coordenadas del anillo
x_outer = r_outer * np.cos(theta)
y_outer = r_outer * np.sin(theta)
x_inner = r_inner * np.cos(theta)
y_inner = r_inner * np.sin(theta)
z_ring = np.zeros_like(theta)  # Anillo plano en z=0

# Dibujar el anillo como un parche sólido en color café
ax.plot_trisurf(np.concatenate([x_outer, x_inner]),
                np.concatenate([y_outer, y_inner]),
                np.concatenate([z_ring, z_ring]),
                color='Yellow', alpha=0.5)  

# Configuración de la gráfica
ax.set_title("Saturno 3D", fontsize=16)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

# Configuración de límites para visualizar bien la figura
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_zlim(-12, 12)

# Ocultar cuadrícula para una mejor visualización
ax.grid(False)
plt.show()
