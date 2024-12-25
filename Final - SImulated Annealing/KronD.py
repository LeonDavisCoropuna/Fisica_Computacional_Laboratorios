import numpy as np
def KronD(E, k):
    # Asegurarse de que E y k sean escalares
    if isinstance(E, np.ndarray):
        # Si E es un arreglo, manejarlo de alguna manera (por ejemplo, seleccionar un valor específico)
        E = E[0]  # O ajusta esto según tu lógica
    if isinstance(k, np.ndarray):
        # Si k es un arreglo, tomar el primer valor (o ajustar según lo que desees hacer)
        k = k[0]

    # Luego realiza la comparación
    d = int(E == k)  # Esto ahora funcionará correctamente si E y k son escalares
    return d
