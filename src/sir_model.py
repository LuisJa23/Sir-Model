# sir_model.py
import matplotlib.pyplot as plt
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from utils.differential_equation import dudt, create_time_array

def sir_eq(u, t, params):
    """
    Define el sistema de ecuaciones diferenciales para el modelo SIR.

    El modelo SIR se describe mediante tres ecuaciones:
        dS/dt = -β * S * I   (Cambio en la población susceptible)
        dI/dt = β * S * I - γ * I   (Cambio en la población infectada)
        dR/dt = γ * I   (Cambio en la población recuperada)

    Donde:
        S: Población susceptible
        I: Población infectada
        R: Población recuperada
        β: Tasa de infección
        γ: Tasa de recuperación

    Parámetros:
        u (list): Estado actual del sistema, donde
                  u[0] = S (susceptibles),
                  u[1] = I (infectados),
                  u[2] = R (recuperados).
        t (float): Tiempo actual (requerido por odeint, pero no se usa directamente).
        params (list): Parámetros del modelo, donde
                       params[0] = β (tasa de infección) y
                       params[1] = γ (tasa de recuperación).

    Retorna:
        list: Derivadas del estado actual del sistema, [dS/dt, dI/dt, dR/dt].
    """
    S, I, R = u  # Desempaquetar el estado actual
    beta, gamma = params  # Desempaquetar los parámetros del modelo
    dSdt = -beta * S * I  # Ecuación para la tasa de cambio de los susceptibles
    dIdt = beta * S * I - gamma * I  # Ecuación para la tasa de cambio de los infectados
    dRdt = gamma * I  # Ecuación para la tasa de cambio de los recuperados
    return [dSdt, dIdt, dRdt]  # Retornar las derivadas

# Condiciones iniciales
S0 = 0.99  # Porcentaje inicial de susceptibles
I0 = 0.01  # Porcentaje inicial de infectados
R0 = 0.0   # Porcentaje inicial de recuperados
u0 = [S0, I0, R0]  # Estado inicial del sistema [S, I, R]

# Parámetros del modelo SIR
beta = 0.4  # Tasa de infección (probabilidad de transmisión)
gamma = 0.1  # Tasa de recuperación (probabilidad de pasar de infectado a recuperado)
params = [beta, gamma]  # Lista de parámetros

# Definir el intervalo de tiempo para la simulación
t = create_time_array(0, 100, 1000)  # Crear un array de tiempo desde 0 hasta 100 días con 1000 puntos

# Resolver el sistema de ecuaciones diferenciales utilizando la función dudt
sol = dudt(sir_eq, u0, t, params)  # Resolver el sistema para obtener las poblaciones en cada tiempo t

# Graficar los resultados
plt.plot(t, sol[:, 0], label='Susceptibles')  # Graficar la población susceptible
plt.plot(t, sol[:, 1], label='Infectados')   # Graficar la población infectada
plt.plot(t, sol[:, 2], label='Recuperados')  # Graficar la población recuperada
plt.xlabel('Tiempo (días)')  # Etiqueta para el eje x
plt.ylabel('Fracción de la población')  # Etiqueta para el eje y
plt.title('Modelo SIR de Enfermedad Infecciosa')  # Título del gráfico
plt.legend(loc='best')  # Mostrar leyenda en la mejor ubicación
plt.show()  # Mostrar el gráfico
