import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def monte_carlo_integration(func, a, b, num_points=10000, visualize=False):
    """
    Aproximación de una integral definida usando el método de Monte Carlo.

    Parameters:
        func (callable): La función a integrar.
        a (float): Límite inferior de la integral.
        b (float): Límite superior de la integral.
        num_points (int): Número de puntos aleatorios a generar.
        visualize (bool): Si True, genera un gráfico mostrando los puntos generados.

    Returns:
        float: Aproximación de la integral.
    """
    # Generar puntos aleatorios en el rango [a, b]
    x_random = np.random.uniform(a, b, num_points)
    y_max = max(func(x) for x in np.linspace(a, b, 1000))
    y_random = np.random.uniform(0, y_max, num_points)

    # Identificar puntos que están debajo de la curva
    under_curve = y_random <= func(x_random)

    # Calcular el área bajo la curva
    area_rectangle = (b - a) * y_max
    integral = (under_curve.sum() / num_points) * area_rectangle

    if visualize:
        # Configurar estilo de gráficos
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))

        # Graficar la curva de la función
        x = np.linspace(a, b, 1000)
        y = func(x)
        sns.lineplot(x=x, y=y, label='Función', color='blue', linewidth=2.5)

        # Graficar puntos bajo la curva
        sns.scatterplot(x=x_random[under_curve], y=y_random[under_curve],
                        color='green', s=5, label='Puntos bajo la curva', alpha=0.6)

        # Graficar puntos sobre la curva
        sns.scatterplot(x=x_random[~under_curve], y=y_random[~under_curve],
                        color='red', s=5, label='Puntos sobre la curva', alpha=0.6)

        # Configuración del gráfico
        plt.title('Integración Monte Carlo', fontsize=14)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

    return integral

def function_1(x):
    return np.exp(x**2)

# Parámetros de la integral
a = 0  # Límite inferior
b = 1  # Límite superior

# Calcular la integral con visualización
result_1 = monte_carlo_integration(function_1, a, b, num_points=5000, visualize=True)
print(f"Resultado de la primera integral: {result_1}")
