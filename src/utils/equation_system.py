import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir la función que representa el sistema de ecuaciones diferenciales
def f(u, t, params):
    """
    Representa el sistema de ecuaciones diferenciales para un péndulo simple.

    El sistema se define como:
        dθ/dt = ω
        dω/dt = -(g/l) * sin(θ)

    Parámetros:
        u (list): Estado actual del sistema, donde
                  u[0] = θ (ángulo en radianes) y
                  u[1] = ω (velocidad angular).
        t (float): Tiempo actual (no se usa directamente en este caso, pero es necesario para odeint).
        params (list): Parámetros físicos del sistema, donde
                       params[0] = g (aceleración gravitatoria) y
                       params[1] = l (longitud del péndulo).

    Retorna:
        list: Derivadas del estado actual del sistema, [dθ/dt, dω/dt].
    """
    theta, omega = u  # Descomponer el estado actual
    g, l = params     # Descomponer los parámetros físicos
    dudt = [omega, -(g / l) * np.sin(theta)]  # Ecuaciones diferenciales
    return dudt

# Condiciones iniciales
theta0 = np.pi / 4  # Ángulo inicial en radianes
omega0 = 0.0        # Velocidad angular inicial (rad/s)
u0 = [theta0, omega0]  # Estado inicial del sistema [θ, ω]

# Parámetros físicos del péndulo
g = 9.81  # Aceleración de la gravedad (m/s^2)
l = 1.0   # Longitud del péndulo (m)
params = [g, l]  # Lista de parámetros del sistema

# Definir el intervalo de tiempo para la simulación
t = np.linspace(0, 10, 500)  # 500 puntos entre 0 y 10 segundos

# Resolver el sistema de ecuaciones diferenciales
sol = odeint(f, u0, t, args=(params,))

# Graficar los resultados
plt.plot(t, sol[:, 0], label='Theta(t)')  # Ángulo θ en función del tiempo
plt.plot(t, sol[:, 1], label='Omega(t)')  # Velocidad angular ω en función del tiempo
plt.xlabel('Tiempo (s)')  # Etiqueta del eje x
plt.ylabel('Solución')  # Etiqueta del eje y
plt.title('--Movimiento Armónico Simple de un Péndulo--')  # Título del gráfico
plt.legend(loc='best')  # Mostrar leyenda con la mejor ubicación automática
plt.grid()  # Añadir una cuadrícula para facilitar la lectura del gráfico
plt.show()  # Mostrar el gráfico
