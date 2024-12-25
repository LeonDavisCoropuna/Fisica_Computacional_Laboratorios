import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def RPS(Eo, dE, Ef, Energia, um, de, T, nomect, nomesp):
    # Parámetros iniciales
    d = 2.7 * 0.1 * de
    El = np.log10(Energia)
    uml = np.log10(um)
    
    # Ajuste de la parametrización del coeficiente de atenuación másico
    def fit_func(x, E):
        return x[0] + x[1] * np.log10(E) + x[2] * np.log10(E)**2 + x[3] * np.log10(E)**3 + x[4] * np.log10(E)**4 + x[5] * np.log10(E)**5
    
    # Ajuste no lineal utilizando optimización de mínimos cuadrados
    def residuals(params, E, um):
        return np.sum((fit_func(params, E) - um)**2)
    
    initial_guess = np.zeros(6)  # Suposición inicial para los parámetros
    params_opt = opt.minimize(residuals, initial_guess, args=(El, uml), method='Nelder-Mead')
    c = params_opt.x

    # Inicialización de variables
    Er = 10
    if Ef == 80:
        um0 = 0.20
    elif Ef == 120:
        um0 = 0.15
    r = 1
    er = 2
    pe = 2

    # Bucle de ajuste
    while Er > 1 or pe > 1:
        # Función objetivo para la optimización
        def fun(x):
            return np.linalg.norm(T - (x[3] * (((x[0] * x[1]) / ((d + x[0]) * (d + x[1]))))**x[2] * np.exp(-um0 * d) +
                                  (1 - x[3]) * (0.2880 * np.exp(-0.2897 * d) + 0.5000 * np.exp(-0.2807 * d) +
                                                0.1690 * np.exp(-0.2417 * d) + 0.0430 * np.exp(-0.2342 * d))))**2
        
        # Solucionador
        x0 = np.random.rand(4)
        bounds = [(0, 10), (0, 10), (0, 10), (0, 1)]
        res = opt.minimize(fun, x0, bounds=bounds, method='Nelder-Mead')
        x = res.x

        # Ajuste de la curva por la ecuación de transmisión
        d1 = 2.7 * 0.1 * np.arange(0, np.max(de), 0.001)
        T1 = x[3] * (((x[0] * x[1]) / ((d1 + x[0]) * (d1 + x[1]))))**x[2] * np.exp(-um0 * d1) + (1 - x[3]) * (
                    0.2880 * np.exp(-0.2897 * d1) + 0.5000 * np.exp(-0.2807 * d1) + 0.1690 * np.exp(-0.2417 * d1) + 0.0430 * np.exp(-0.2342 * d1))

        # Ajuste opcional
        popt, _ = np.polyfit(d, T, 2, full=True)
        E = popt[0] + popt[1] * np.exp(-popt[2] * d1)

        # Capa semirreductora de la curva de transmisión
        CSRct = d1[np.argmin(np.abs(T1 - 0.5))]

        # Vector de energía
        E = np.arange(Eo, Ef, dE)

        # Coeficientes másicos de atenuación
        um = 10**(c[0] + c[1] * np.log10(E) + c[2] * np.log10(E)**2 + c[3] * np.log10(E)**3 +
                 c[4] * np.log10(E)**4 + c[5] * np.log10(E)**5)

        # Espectro de energía
        Fb = (r * (np.sqrt(np.pi) * (a * b)**2) / np.math.gamma(v)) * (
                    ((um - um0) / (a - b))**(v - 0.5)) * np.exp(-0.5 * (a + b) * (um - um0)) * \
             np.i0((0.5 * (a - b) * (um - um0))) * (0.5 * (a - b) * (um - um0)) * (-dUmdE)
        Fc = (1 - r) * (0.2880 * KronD(E, 58) + 0.5 * KronD(E, 59.5) + 0.1690 * KronD(E, 67.0) + 0.0430 * KronD(E, 69.0))

        F = Fb + Fc
        F = F / np.max(F)  # Normalización
        F[np.isnan(F)] = 0  # Sustituir NaN por 0

        # Cálculo de la capa semirreductora del espectro
        if Ef == 80:
            K0 = np.sum(396.2 * dE * F * np.exp(-um.T * 0))
            K2 = np.sum(396.2 * dE * F * np.exp(-um.T * 0.74))
            K1 = np.sum(396.2 * dE * F * np.exp(-um.T * 0.58))
            CSR = (0.58 * np.log(2 * K2 / K0) - 0.74 * np.log(2 * K1 / K0)) / np.log(K2 / K1)

        elif Ef == 120:
            K0 = np.sum(629.2 * dE * F * np.exp(-um.T * 0))
            K2 = np.sum(629.2 * dE * F * np.exp(-um.T * 1.63))
            K1 = np.sum(629.2 * dE * F * np.exp(-um.T * 1.35))
            CSR = (1.35 * np.log(2 * K2 / K0) - 1.63 * np.log(2 * K1 / K0)) / np.log(K2 / K1)

        # Capa semirreductora del espectro
        Er = np.abs(100 * (CSRct - CSR) / CSRct)

        # Gráficas
        plt.figure()
        plt.plot(d, T, 'ok', label='Experimental Data')
        plt.plot(d1, T1, '-k', label='Fitted Curve')
        plt.xlabel('Thickness (g/cm^2)')
        plt.ylabel('Transmission Curve')
        plt.legend()
        plt.savefig(nomect, dpi=300)

        plt.figure()
        plt.plot(E, F, 'k')
        plt.xlabel('Energy (kV)')
        plt.ylabel('Energy Spectrum')
        plt.savefig(nomesp, dpi=300)

        break  # Salir del bucle, ya que hemos terminado el ajuste

    return E, F, Er


# Ejemplo de llamada a la función
Eo = 10
dE = 0.5
Ef = 80
Energia = np.array([10, 20, 30, 40, 50, 60, 70, 80])  # Ejemplo de vector de energía
um = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])  # Ejemplo de coeficientes de atenuación
de = np.array([0.1, 0.2, 0.3, 0.4])  # Ejemplo de espesor
T = np.array([1, 0.9, 0.8, 0.7])  # Ejemplo de transmisión
nomect = 'transmission_curve.jpg'
nomesp = 'energy_spectrum.jpg'

E, F, Er = RPS(Eo, dE, Ef, Energia, um, de, T, nomect, nomesp)
