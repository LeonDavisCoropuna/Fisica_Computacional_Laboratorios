import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Función para calcular velocidad y órbita
def calcular_orbita():
    try:
        d = float(entry_distancia.get())
        t = float(entry_tiempo.get())
        velocidad = d / t
        messagebox.showinfo("Resultado", f"Velocidad: {velocidad:.2f} m/s")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

# Función para calcular fuerza y graficar
def calcular_fuerza():
    try:
        m = float(entry_masa.get())
        vi = float(entry_velocidad_inicial.get())
        vf = float(entry_velocidad_final.get())
        t = float(entry_tiempo_fuerza.get())
        
        a = (vf - vi) / t
        fuerza = m * a
        
        messagebox.showinfo("Resultado", f"Fuerza: {fuerza:.2f} N")
        
        # Graficar el cambio de velocidad
        tiempos = np.linspace(0, t, 100)
        velocidades = vi + a * tiempos
        
        plt.figure()
        plt.plot(tiempos, velocidades, label='Cambio de velocidad')
        plt.axhline(y=vi, color='r', linestyle='--', label='Velocidad inicial')
        plt.axhline(y=vf, color='g', linestyle='--', label='Velocidad final')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Velocidad (m/s)')
        plt.title('Cambio de Velocidad')
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Cálculos de Física")

# Entradas para MRU
tk.Label(root, text="Distancia (m):").grid(row=0, column=0)
entry_distancia = tk.Entry(root)
entry_distancia.grid(row=0, column=1)

tk.Label(root, text="Tiempo (s):").grid(row=1, column=0)
entry_tiempo = tk.Entry(root)
entry_tiempo.grid(row=1, column=1)

tk.Button(root, text="Calcular Velocidad Orbital", command=calcular_orbita).grid(row=2, columnspan=2)

# Entradas para cálculo de fuerza
tk.Label(root, text="Masa (kg):").grid(row=3, column=0)
entry_masa = tk.Entry(root)
entry_masa.grid(row=3, column=1)

tk.Label(root, text="Velocidad Inicial (m/s):").grid(row=4, column=0)
entry_velocidad_inicial = tk.Entry(root)
entry_velocidad_inicial.grid(row=4, column=1)

tk.Label(root, text="Velocidad Final (m/s):").grid(row=5, column=0)
entry_velocidad_final = tk.Entry(root)
entry_velocidad_final.grid(row=5, column=1)

tk.Label(root, text="Tiempo (s):").grid(row=6, column=0)
entry_tiempo_fuerza = tk.Entry(root)
entry_tiempo_fuerza.grid(row=6, column=1)

tk.Button(root, text="Calcular Fuerza", command=calcular_fuerza).grid(row=7, columnspan=2)

# Ejecutar la interfaz
root.mainloop()
