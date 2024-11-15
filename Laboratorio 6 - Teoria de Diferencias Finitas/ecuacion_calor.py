import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import ttk

# Función para actualizar la temperatura utilizando la ecuación de calor
def actualizar_temperatura(n, m, r, tiempo, x_inicial, y_inicial, temp_inicial):
    # Crear una malla inicial con temperaturas 0 en todos los puntos
    u = np.zeros((n, m))  # Temperatura inicial en todos los puntos es 0
    u_new = np.copy(u)  # Para almacenar la siguiente iteración

    # Establecer el punto inicial de calor en (x,y)
    u[x_inicial, y_inicial] = temp_inicial

    # Distribuir la temperatura de manera radial (cono invertido)
    for i in range(n):
        for j in range(m):
            distance = np.sqrt((i - x_inicial)**2 + (j - y_inicial)**2)
            u[i, j] = temp_inicial * np.exp(-distance/10.0)  # Decaimiento exponencial hacia los bordes

    # Iterar por el número de pasos de tiempo
    for t in range(tiempo):
        for i in range(1, n-1):
            for j in range(1, m-1):
                u_new[i, j] = (1 - 2*r) * u[i, j] + r * (u[i+1, j] - 2 * u[i, j] + u[i-1, j])
        u = np.copy(u_new)  # Actualizar u con los nuevos valores
    return u_new

# Función para graficar los resultados en 3D
def graficar_temperatura(u_final):
    n, m = u_final.shape
    X, Y = np.meshgrid(np.arange(m), np.arange(n))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Plotting the 3D surface
    ax.plot_surface(X, Y, u_final, cmap='hot', edgecolor='none')

    ax.set_xlabel('X (espacio)')
    ax.set_ylabel('Y (espacio)')
    ax.set_zlabel('Temperatura')
    ax.set_title('Distribución de Temperatura en 3D')

    plt.show()

# Función que se ejecuta cuando el botón es presionado
def ejecutar_simulacion():
    # Obtener los valores de los campos de entrada
    n = int(entry_n.get())
    m = int(entry_m.get())
    r = float(entry_r.get())
    tiempo = int(entry_tiempo.get())
    x_inicial = int(entry_x_inicial.get())
    y_inicial = int(entry_y_inicial.get())
    temp_inicial = float(entry_temp_inicial.get())

    # Simular la distribución de temperatura
    u_final = actualizar_temperatura(n, m, r, tiempo, x_inicial, y_inicial, temp_inicial)

    # Graficar el resultado en 3D
    graficar_temperatura(u_final)

# Crear la ventana de la aplicación
root = tk.Tk()
root.title("Simulación de Ecuación de Calor")

# Crear los campos de entrada
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Campos con valores iniciales predeterminados
ttk.Label(frame, text="Tamaño de la superficie (n):").grid(row=0, column=0)
entry_n = ttk.Entry(frame)
entry_n.insert(0, "50")  # Valor inicial
entry_n.grid(row=0, column=1)

ttk.Label(frame, text="Tamaño de la superficie (m):").grid(row=1, column=0)
entry_m = ttk.Entry(frame)
entry_m.insert(0, "50")  # Valor inicial
entry_m.grid(row=1, column=1)

ttk.Label(frame, text="Valor de r:").grid(row=2, column=0)
entry_r = ttk.Entry(frame)
entry_r.insert(0, "0.1")  # Valor inicial
entry_r.grid(row=2, column=1)

ttk.Label(frame, text="Número de pasos de tiempo:").grid(row=3, column=0)
entry_tiempo = ttk.Entry(frame)
entry_tiempo.insert(0, "50")  # Valor inicial
entry_tiempo.grid(row=3, column=1)

ttk.Label(frame, text="Posición inicial de calor (x):").grid(row=4, column=0)
entry_x_inicial = ttk.Entry(frame)
entry_x_inicial.insert(0, "25")  # Valor inicial
entry_x_inicial.grid(row=4, column=1)

ttk.Label(frame, text="Posición inicial de calor (y):").grid(row=5, column=0)
entry_y_inicial = ttk.Entry(frame)
entry_y_inicial.insert(0, "25")  # Valor inicial
entry_y_inicial.grid(row=5, column=1)

ttk.Label(frame, text="Temperatura inicial en (x, y):").grid(row=6, column=0)
entry_temp_inicial = ttk.Entry(frame)
entry_temp_inicial.insert(0, "100")  # Valor inicial
entry_temp_inicial.grid(row=6, column=1)

# Botón para ejecutar la simulación
boton_simulacion = ttk.Button(frame, text="Ejecutar Simulación", command=ejecutar_simulacion)
boton_simulacion.grid(row=7, columnspan=2)

# Iniciar la ventana de Tkinter
root.mainloop()
