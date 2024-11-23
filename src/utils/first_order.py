import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir la función que representa la ecuación diferencial
def f(y, t):
    """
    Define la ecuación diferencial de primer orden en la forma:
        dy/dt = k * y

    Este modelo representa un decaimiento exponencial, donde la constante k
    determina la tasa de cambio.

    Parámetros:
        y (float): Valor actual de la variable dependiente.
        t (float): Tiempo actual (no se usa directamente, pero es requerido por odeint).

    Retorna:
        float: Derivada dy/dt en el punto dado.
    """
    k = -0.3  # Constante de decaimiento (negativa para representar una disminución)
    dydt = k * y  # Ecuación diferencial
    return dydt

# Condición inicial
y0 = 5  # Valor inicial de y en t = 0

# Intervalo de tiempo para la simulación
t = np.linspace(0, 20, 100)  # 100 puntos uniformemente distribuidos entre t = 0 y t = 20

# Resolver la ecuación diferencial usando odeint
y = odeint(f, y0, t)  # Calcula la solución para cada punto de tiempo en t

# Graficar la solución
plt.plot(t, y, label='y(t)')
plt.xlabel('Tiempo (s)')  # Etiqueta para el eje x
plt.ylabel('y(t)')  # Etiqueta para el eje y
plt.title('Solución de la Ecuación Diferencial: Decaimiento Exponencial')  # Título del gráfico
plt.legend()  # Añadir leyenda
plt.grid()  # Mostrar cuadrícula para facilitar la lectura del gráfico
plt.show()  # Mostrar el gráfico
