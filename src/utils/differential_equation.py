import numpy as np
from scipy.integrate import odeint

# Resolver una ecuación diferencial ordinaria (EDO) de primer orden.
def dydt(f, y0, t, *args):
    """
    Resuelve una ecuación diferencial de primer orden.

    Parámetros:
        f (función): Función que describe la ecuación diferencial en forma y' = f(y, t, ...).
        y0 (float o array): Valor inicial o condición inicial de la solución.
        t (array): Array de puntos de tiempo donde se evaluará la solución.
        *args: Argumentos adicionales que se pasarán a la función f.

    Retorna:
        numpy.ndarray: Array que contiene la solución de la ecuación diferencial evaluada en los puntos de tiempo t.
    """
    return odeint(f, y0, t, args=args)

# Resolver un sistema de ecuaciones diferenciales.
def dudt(f, u0, t, params):
    """
    Resuelve un sistema de ecuaciones diferenciales ordinarias (EDOs).

    Parámetros:
        f (función): Función que describe el sistema de ecuaciones diferenciales en forma u' = f(u, t, params).
        u0 (array): Array que contiene las condiciones iniciales para cada variable del sistema.
        t (array): Array de puntos de tiempo donde se evaluará la solución.
        params: Parámetros adicionales que se pasarán a la función f.

    Retorna:
        numpy.ndarray: Array que contiene las soluciones de las variables del sistema en cada punto de tiempo t.
    """
    return odeint(f, u0, t, args=(params,))

# Generar un array de puntos de tiempo uniformemente distribuidos.
def create_time_array(start, stop, num_points):
    """
    Crea un array con valores de tiempo distribuidos uniformemente.

    Parámetros:
        start (float): Tiempo inicial del intervalo.
        stop (float): Tiempo final del intervalo.
        num_points (int): Número de puntos que se generarán entre start y stop.

    Retorna:
        numpy.ndarray: Array de puntos de tiempo con tamaño `num_points`.
    """
    return np.linspace(start, stop, num_points)
