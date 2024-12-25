import numpy as np
from scipy.optimize import curve_fit
from scipy.special import iv as besseli
import matplotlib.pyplot as plt

# Datos iniciales (equivalente a `dx` y `N` en MATLAB)
dx = 0.1
x = np.arange(0, 2 + dx, dx)  # Vector x desde 0 hasta 2 con incrementos de dx
N = len(x)

data = [
    [1.21, 0.837, 0.557, 0.363, 0.249, 0.186, 0.146, 0.115, 0.091, 0.074, 0.061, 0.051, 0.043, 0.037, 0.031, 0.026, 0.021, 0.017, 0.012, 0.007, 0.002],
    [1.375, 0.957, 0.656, 0.45, 0.317, 0.238, 0.182, 0.141, 0.111, 0.089, 0.072, 0.059, 0.049, 0.041, 0.034, 0.029, 0.024, 0.02, 0.015, 0.01, 0.004],
    [1.54, 1.072, 0.742, 0.512, 0.359, 0.268, 0.206, 0.159, 0.126, 0.101, 0.082, 0.067, 0.056, 0.047, 0.04, 0.034, 0.028, 0.024, 0.018, 0.012, 0.006]
]

# Conversión de MATLAB a numpy array
data = np.array(data)

# Promedio
mean_data = np.mean(data, axis=0)

# Función objetivo para el ajuste
def fit_function(x, C):
    return C * besseli(0, C * x) * np.exp(-C * x)

# Ajuste de curvas
initial_guess = [1]  # Suposición inicial para C
params, _ = curve_fit(fit_function, x, mean_data, p0=initial_guess)
C_fit = params[0]

# Generar los valores ajustados
fitted_values = fit_function(x, C_fit)

# Gráfica
plt.plot(x, mean_data, 'o', label='Datos promedio')
plt.plot(x, fitted_values, '-', label=f'Ajuste (C = {C_fit:.4f})')
plt.xlabel('x')
plt.ylabel('Mean Data / Fitted Data')
plt.legend()
plt.title('Ajuste de datos usando función de Bessel modificada')
plt.show()
