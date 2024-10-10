import tkinter as tk
from tkinter import ttk

class PhysicsCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Física")
        self.root.geometry("400x400")

        self.style = ttk.Style()
        self.style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        self.style.map("TButton", background=[("active", "#45a049")])
        
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TEntry", font=("Helvetica", 12))

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.mru_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.mru_tab, text="Calculadora MRU")
        self.create_mru_widgets()

        self.mruv_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.mruv_tab, text="Calculadora MRUV")
        self.create_mruv_widgets()

    def create_mru_widgets(self):
        self.variable_to_find_mru = tk.StringVar(value="distance")
        self.velocity = tk.DoubleVar()
        self.time = tk.DoubleVar()
        self.distance = tk.DoubleVar()
        self.result_mru = None

        # Título
        title_label = tk.Label(self.mru_tab, text="Calculadora MRU", font=("Helvetica", 16), bg="#2E2E2E", fg="white")
        title_label.pack(pady=10, fill=tk.X)

        # Selección de variable
        variable_label = tk.Label(self.mru_tab, text="¿Qué variable quieres calcular?", bg="#2E2E2E", fg="white")
        variable_label.pack()

        variable_menu = ttk.Combobox(self.mru_tab, textvariable=self.variable_to_find_mru, state="readonly")
        variable_menu['values'] = ["distance", "velocity", "time"]
        variable_menu.pack(pady=5)
        variable_menu.bind("<<ComboboxSelected>>", self.update_mru_fields)

        # Frame para entradas
        frame = tk.Frame(self.mru_tab, bg="#2E2E2E")
        frame.pack(pady=10)

        self.distance_entry = self.create_entry(frame, "Distancia (m):", self.distance, 0)
        self.velocity_entry = self.create_entry(frame, "Velocidad (m/s):", self.velocity, 1)
        self.time_entry = self.create_entry(frame, "Tiempo (s):", self.time, 2)

        calculate_button = ttk.Button(self.mru_tab, text="Calcular", command=self.calculate_mru)
        calculate_button.pack(pady=10)

        self.result_label_mru = tk.Label(self.mru_tab, text="", bg="#2E2E2E", fg="white")
        self.result_label_mru.pack(pady=10)

        self.update_mru_fields()

    def create_mruv_widgets(self):
        self.variable_to_find_mruv = tk.StringVar(value="distance")
        self.initial_velocity = tk.DoubleVar()
        self.acceleration = tk.DoubleVar()
        self.time_mruv = tk.DoubleVar()
        self.final_velocity = tk.DoubleVar()
        self.result_mruv = None

        # Título
        title_label = tk.Label(self.mruv_tab, text="Calculadora MRUV", font=("Helvetica", 16), bg="#2E2E2E", fg="white")
        title_label.pack(pady=10, fill=tk.X)

        # Selección de variable
        variable_label = tk.Label(self.mruv_tab, text="¿Qué variable quieres calcular?", bg="#2E2E2E", fg="white")
        variable_label.pack()

        variable_menu = ttk.Combobox(self.mruv_tab, textvariable=self.variable_to_find_mruv, state="readonly")
        variable_menu['values'] = ["distance", "finalVelocity", "time", "acceleration", "initialVelocity"]
        variable_menu.pack(pady=5)
        variable_menu.bind("<<ComboboxSelected>>", self.update_mruv_fields)

        # Frame para entradas
        frame = tk.Frame(self.mruv_tab, bg="#2E2E2E")
        frame.pack(pady=10)

        # Campos de entrada
        self.initial_velocity_entry = self.create_entry(frame, "Velocidad Inicial (m/s):", self.initial_velocity, 0)
        self.acceleration_entry = self.create_entry(frame, "Aceleración (m/s²):", self.acceleration, 1)
        self.time_entry_mruv = self.create_entry(frame, "Tiempo (s):", self.time_mruv, 2)
        self.final_velocity_entry = self.create_entry(frame, "Velocidad Final (m/s):", self.final_velocity, 3)

        # Botón de calcular
        calculate_button = ttk.Button(self.mruv_tab, text="Calcular", command=self.calculate_mruv)
        calculate_button.pack(pady=10)

        # Etiqueta de resultado
        self.result_label_mruv = tk.Label(self.mruv_tab, text="", bg="#2E2E2E", fg="white")
        self.result_label_mruv.pack(pady=10)

        # Configuración inicial
        self.update_mruv_fields()

    def create_entry(self, frame, label_text, variable, row):
        label = tk.Label(frame, text=label_text, bg="#2E2E2E", fg="white")
        entry = ttk.Entry(frame, textvariable=variable)

        label.grid(row=row, column=0, padx=5, pady=5, sticky=tk.W)
        entry.grid(row=row, column=1, padx=5, pady=5)

        return entry

    def update_mru_fields(self, event=None):
        selected = self.variable_to_find_mru.get()
        for entry in [self.distance_entry, self.velocity_entry, self.time_entry]:
            entry.config(state='normal')

        if selected == "distance":
            self.distance_entry.config(state='disabled')
        elif selected == "velocity":
            self.velocity_entry.config(state='disabled')
        elif selected == "time":
            self.time_entry.config(state='disabled')

    def calculate_mru(self):
        var = self.variable_to_find_mru.get()
        try:
            if var == "distance":
                if self.velocity.get() is not None and self.time.get() is not None:
                    # Fórmula: d = v * t
                    self.result_mru = self.velocity.get() * self.time.get()
                    formula = f"d = {self.velocity.get()} * {self.time.get()}"
            
            elif var == "velocity":
                if self.distance.get() is not None and self.time.get() is not None:
                    # Fórmula: v = d / t
                    self.result_mru = self.distance.get() / self.time.get()
                    formula = f"v = {self.distance.get()} / {self.time.get()}"
            
            elif var == "time":
                if self.distance.get() is not None and self.velocity.get() is not None:
                    # Fórmula: t = d / v
                    self.result_mru = self.distance.get() / self.velocity.get()
                    formula = f"t = {self.distance.get()} / {self.velocity.get()}"

            # Mostrar resultado y fórmula utilizada
            if self.result_mru is not None:
                self.result_label_mru.config(text=f"Resultado: {self.result_mru:.2f}\nFórmula utilizada: {formula}")
            else:
                self.result_label_mru.config(text="Error en el cálculo")
        except Exception as e:
            self.result_label_mru.config(text=f"Error: {str(e)}")


    def update_mruv_fields(self, event=None):
        selected = self.variable_to_find_mruv.get()
        for entry in [self.initial_velocity_entry, self.acceleration_entry, self.time_entry_mruv, self.final_velocity_entry]:
            entry.config(state='normal')

        if selected == "initialVelocity":
            self.initial_velocity_entry.config(state='disabled')
        elif selected == "acceleration":
            self.acceleration_entry.config(state='disabled')
        elif selected == "time":
            self.time_entry_mruv.config(state='disabled')
        elif selected == "finalVelocity":
            self.final_velocity_entry.config(state='disabled')
        elif selected == "distance":
            self.final_velocity_entry.config(state='disabled')

    def calculate_mruv(self):
        var = self.variable_to_find_mruv.get()
        try:
            if var == "distance":
                if self.initial_velocity.get() is not None and self.time_mruv.get() is not None and self.acceleration.get() is not None:
                    # Fórmula: x = x0 + v0*t + 0.5*a*t^2
                    self.result_mruv = self.initial_velocity.get() * self.time_mruv.get() + 0.5 * self.acceleration.get() * self.time_mruv.get() ** 2
                    formula = f"x = {self.initial_velocity.get()} * {self.time_mruv.get()} + 0.5 * {self.acceleration.get()} * ({self.time_mruv.get()} ^ 2)"
            
            elif var == "finalVelocity":
                if self.initial_velocity.get() is not None and self.time_mruv.get() is not None and self.acceleration.get() is not None:
                    # Fórmula: v = v0 + a*t
                    self.result_mruv = self.initial_velocity.get() + self.acceleration.get() * self.time_mruv.get()
                    formula = f"v = {self.initial_velocity.get()} + {self.acceleration.get()} * {self.time_mruv.get()}"
            
            elif var == "time":
                if self.initial_velocity.get() is not None and self.final_velocity.get() is not None and self.acceleration.get() is not None:
                    # Fórmula: t = (v - v0) / a
                    self.result_mruv = (self.final_velocity.get() - self.initial_velocity.get()) / self.acceleration.get()
                    formula = f"t = ({self.final_velocity.get()} - {self.initial_velocity.get()}) / {self.acceleration.get()}"
            
            elif var == "acceleration":
                if self.final_velocity.get() is not None and self.initial_velocity.get() is not None and self.time_mruv.get() is not None:
                    # Fórmula: a = (v - v0) / t
                    self.result_mruv = (self.final_velocity.get() - self.initial_velocity.get()) / self.time_mruv.get()
                    formula = f"a = ({self.final_velocity.get()} - {self.initial_velocity.get()}) / {self.time_mruv.get()}"

            # Mostrar resultado y fórmula utilizada
            if self.result_mruv is not None:
                self.result_label_mruv.config(text=f"Resultado: {self.result_mruv:.2f}\nFórmula utilizada: {formula}")
            else:
                self.result_label_mruv.config(text="Error en el cálculo")
        except Exception as e:
            self.result_label_mruv.config(text=f"Error: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PhysicsCalculator(root)
    root.mainloop()
