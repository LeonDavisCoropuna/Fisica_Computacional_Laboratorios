import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox

# Constante de gravedad
g = 9.81  # Aceleración de la gravedad (m/s^2)

def calcular_y_graficar():
    try:
        # Obtener valores ingresados
        masa = float(entry_masa.get())
        h_inicial = float(entry_altura.get())
        v_inicial = float(entry_velocidad.get())
        
        # Validar que los valores sean positivos
        if masa <= 0 or h_inicial < 0:
            messagebox.showerror("Error", "La masa debe ser positiva y la altura no negativa.")
            return
        
        # Parámetros de tiempo
        tiempo_total = 5  # segundos
        pasos = 100
        t = np.linspace(0, tiempo_total, pasos)

        # Listas para almacenar valores de energía
        energia_cinetica = []
        energia_potencial = []
        energia_mecanica = []
        energia_potencial_vs_altura = []

        # Cálculos de la energía en cada instante de tiempo
        for i in range(pasos):
            # Calculamos la altura en cada instante
            altura = h_inicial - (1 / 2) * g * t[i] ** 2  # Ecuación de caída libre
            if altura < 0:  # Limitar la altura a 0 si pasa por debajo del suelo
                altura = 0
            velocidad = v_inicial - g * t[i]  # Velocidad en cada instante

            # Energía cinética y potencial
            EK = 0.5 * masa * velocidad ** 2
            EP = masa * g * altura  # Energía potencial con altura positiva

            # Energía mecánica
            em = EK + EP

            # Guardamos los valores en las listas
            energia_cinetica.append(EK)
            energia_potencial.append(EP)
            energia_mecanica.append(em)
            energia_potencial_vs_altura.append(EP)

        # Graficar los resultados
        plt.figure(figsize=(12, 6))

        # Energía en función del tiempo
        plt.subplot(1, 2, 1)
        plt.plot(t, energia_cinetica, label='Energía Cinética (EK)', color='blue')
        plt.plot(t, energia_potencial, label='Energía Potencial (EP)', color='red')
        plt.plot(t, energia_mecanica, label='Energía Mecánica Total (Em)', color='green', linestyle='--')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Energía (J)')
        plt.title('Conservación de la Energía Mecánica')
        plt.legend()
        plt.grid(True)

        # Energía potencial en función de la altura
        plt.subplot(1, 2, 2)
        plt.plot(t, energia_potencial_vs_altura, label='Energía Potencial vs Altura', color='purple')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Energía Potencial (J)')
        plt.title('Energía Potencial vs Altura')
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conservación de Energía Mecánica")
ventana.geometry("400x300")

# Etiquetas y campos de entrada
label_masa = ttk.Label(ventana, text="Masa (kg):")
label_masa.pack(pady=5)
entry_masa = ttk.Entry(ventana)
entry_masa.pack(pady=5)

label_altura = ttk.Label(ventana, text="Altura Inicial (m):")
label_altura.pack(pady=5)
entry_altura = ttk.Entry(ventana)
entry_altura.pack(pady=5)

label_velocidad = ttk.Label(ventana, text="Velocidad Inicial (m/s):")
label_velocidad.pack(pady=5)
entry_velocidad = ttk.Entry(ventana)
entry_velocidad.pack(pady=5)

# Botón para calcular y graficar
btn_calcular = ttk.Button(ventana, text="Calcular y Graficar", command=calcular_y_graficar)
btn_calcular.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
