import tkinter as tk
from tkinter import messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Cálculo del Trabajo - Fuerza Variable")
root.geometry("500x600")
root.configure(bg="#f0f0f0")  

x = sp.symbols('x')
def calcular_trabajo():
    try:
        funcion_str = entry_funcion.get()
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get()) 

        F = sp.sympify(funcion_str)

        a_ceiled = np.ceil(a)
        b_ceiled = np.floor(b)

        integral_F = sp.integrate(F, (x, a, b))

        def discrete_sum(F, a, b, n):
            dx = (b - a) / n  # Tamaño de los intervalos
            x_vals = np.linspace(a, b, n + 1) 
            sum_result = sum([F.subs(x, xi) * dx for xi in x_vals[:-1]]) 
            return sum_result, x_vals[:-1], [F.subs(x, xi) for xi in x_vals[:-1]]  

        discrete_result, x_rect, y_rect = discrete_sum(F, a_ceiled, b_ceiled, n)

        label_result_integral.config(text=f"Resultado Integral: {integral_F}")
        label_result_sumatoria.config(text=f"Resultado Sumatoria: {discrete_result}")

        desviacion_porcentual = abs((integral_F - discrete_result) / integral_F) * 100
        label_result_desviacion.config(text=f"Desviación Porcentual: {desviacion_porcentual:.4f}%")

        f_lambdified = sp.lambdify(x, F, modules='numpy')
        x_vals = np.linspace(a, b, 1000)
        y_vals = f_lambdified(x_vals)

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label='Fuerza F(x)', color='blue')
        plt.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)

        for i in range(n):
            plt.bar(x_rect[i], y_rect[i], width=(b - a) / n, alpha=0.5, color='red', edgecolor='black', align='edge')

        plt.title(f'Gráfica de la fuerza F(x) y particiones en el intervalo [{a}, {b}]')
        plt.xlabel('Posición x')
        plt.ylabel('F(x)')
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Error en los cálculos: {e}")


titulo = tk.Label(root, text="Cálculo del Trabajo con Fuerza Variable", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=10)

instruccion = tk.Label(root, text="Ingrese la función en términos de x. Ejemplos: x**2, sin(x), cos(x)", bg="#f0f0f0", fg="#555555")
instruccion.pack(pady=5)

label_funcion = tk.Label(root, text="Función de la fuerza F(x):", bg="#f0f0f0", font=("Arial", 12))
label_funcion.pack(pady=5)

entry_funcion = tk.Entry(root, width=30, font=("Arial", 12))
entry_funcion.pack(pady=5)

label_a = tk.Label(root, text="Valor inicial del intervalo (a):", bg="#f0f0f0", font=("Arial", 12))
label_a.pack(pady=5)

entry_a = tk.Entry(root, width=10, font=("Arial", 12))
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Valor final del intervalo (b):", bg="#f0f0f0", font=("Arial", 12))
label_b.pack(pady=5)

entry_b = tk.Entry(root, width=10, font=("Arial", 12))
entry_b.pack(pady=5)

label_n = tk.Label(root, text="Número de particiones (n):", bg="#f0f0f0", font=("Arial", 12))
label_n.pack(pady=5)

entry_n = tk.Entry(root, width=10, font=("Arial", 12))
entry_n.pack(pady=5)

boton_calcular = tk.Button(root, text="Calcular Trabajo", command=calcular_trabajo, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=20)
boton_calcular.pack(pady=20)

label_result_integral = tk.Label(root, text="Resultado Integral:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_result_integral.pack(pady=10)

label_result_sumatoria = tk.Label(root, text="Resultado Sumatoria:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_result_sumatoria.pack(pady=10)

label_result_desviacion = tk.Label(root, text="Desviación Porcentual:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_result_desviacion.pack(pady=10)

root.mainloop()
