import tkinter as tk
from tkinter import messagebox

# Función para calcular la fuerza
def calcular_fuerza():
    try:
        # Obtener los valores de entrada
        masa = float(entry_masa.get())
        aceleracion = float(entry_aceleracion.get())
        
        # Calcular la fuerza
        fuerza = masa * aceleracion
        
        # Mostrar el resultado en la etiqueta
        label_resultado.config(text=f"La fuerza es: {fuerza:.2f} N")
    except ValueError:
        # Si hay un error en la conversión de números, mostrar un mensaje de error
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Fuerza (Segunda Ley de Newton)")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Crear el marco principal
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Etiqueta y entrada para la masa
label_masa = tk.Label(frame, text="Masa (kg):", font=("Arial", 12), bg="#f0f0f0")
label_masa.grid(row=0, column=0, padx=10, pady=10)

entry_masa = tk.Entry(frame, font=("Arial", 12), width=10)
entry_masa.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y entrada para la aceleración
label_aceleracion = tk.Label(frame, text="Aceleración (m/s²):", font=("Arial", 12), bg="#f0f0f0")
label_aceleracion.grid(row=1, column=0, padx=10, pady=10)

entry_aceleracion = tk.Entry(frame, font=("Arial", 12), width=10)
entry_aceleracion.grid(row=1, column=1, padx=10, pady=10)

# Botón para calcular la fuerza
boton_calcular = tk.Button(frame, text="Calcular Fuerza", font=("Arial", 12), bg="#4CAF50", fg="white", command=calcular_fuerza)
boton_calcular.grid(row=2, column=0, columnspan=2, pady=20)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="La fuerza es: -- N", font=("Arial", 14), bg="#f0f0f0", fg="blue")
label_resultado.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
