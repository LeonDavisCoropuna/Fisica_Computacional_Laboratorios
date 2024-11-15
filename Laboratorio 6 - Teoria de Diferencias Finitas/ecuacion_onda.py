import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import ttk

def ejecutar_simulacion_onda():
    # Obtener los valores de los campos de entrada
    n = int(entry_n.get())
    m = int(entry_m.get())
    r = float(entry_r.get())
    tiempo = int(entry_tiempo.get())
    x_centro = int(entry_x_centro.get())
    y_centro = int(entry_y_centro.get())

    # Inicialización de las matrices de la onda
    u = np.zeros((n, m))       # Estado actual
    u_prev = np.zeros((n, m))  # Estado en el tiempo anterior

    # Condición inicial: perturbación en la posición especificada
    u[x_centro, y_centro] = 10  # Desplazamiento inicial

    # Lista para almacenar los estados en el tiempo
    frames = []

    # Simulación de la ecuación de onda
    for t in range(tiempo):
        u_new = np.zeros((n, m))
        for i in range(1, n-1):
            for j in range(1, m-1):
                u_new[i, j] = 2 * (1 - r**2) * u[i, j] + r**2 * (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1]) - u_prev[i, j]

        # Actualizar los estados
        u_prev = np.copy(u)
        u = np.copy(u_new)

        # Guardar el estado actual para la animación
        frames.append(np.copy(u))

    # Crear una animación para visualizar la propagación de la onda en 3D
    fig, ax = plt.subplots()
    cax = ax.imshow(frames[0], cmap='viridis', vmin=-1, vmax=1)
    fig.colorbar(cax)

    def update(frame):
        cax.set_data(frame)
        return cax,

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, repeat=False)
    plt.title("Propagación de la onda")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# Crear la ventana de la aplicación
root = tk.Tk()
root.title("Simulación de Ecuación de Onda")

# Crear los campos de entrada
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

ttk.Label(frame, text="Tamaño de la superficie (n):").grid(row=0, column=0)
entry_n = ttk.Entry(frame)
entry_n.insert(0, "100")
entry_n.grid(row=0, column=1)

ttk.Label(frame, text="Tamaño de la superficie (m):").grid(row=1, column=0)
entry_m = ttk.Entry(frame)
entry_m.insert(0, "100")
entry_m.grid(row=1, column=1)

ttk.Label(frame, text="Valor de r:").grid(row=2, column=0)
entry_r = ttk.Entry(frame)
entry_r.insert(0, "0.1")
entry_r.grid(row=2, column=1)

ttk.Label(frame, text="Número de iteraciones de tiempo:").grid(row=3, column=0)
entry_tiempo = ttk.Entry(frame)
entry_tiempo.insert(0, "200")
entry_tiempo.grid(row=3, column=1)

ttk.Label(frame, text="Posición inicial de la onda (x):").grid(row=4, column=0)
entry_x_centro = ttk.Entry(frame)
entry_x_centro.insert(0, "50")
entry_x_centro.grid(row=4, column=1)

ttk.Label(frame, text="Posición inicial de la onda (y):").grid(row=5, column=0)
entry_y_centro = ttk.Entry(frame)
entry_y_centro.insert(0, "50")
entry_y_centro.grid(row=5, column=1)

# Botón para ejecutar la simulación
boton_simulacion = ttk.Button(frame, text="Ejecutar Simulación", command=ejecutar_simulacion_onda)
boton_simulacion.grid(row=6, columnspan=2)

# Iniciar la ventana de Tkinter
root.mainloop()
