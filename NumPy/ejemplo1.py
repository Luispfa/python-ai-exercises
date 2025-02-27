import numpy as np

# Supongamos que estos son los tiempos de consulta en minutos
tiempos_consultas = np.array([30, 45, 50, 35, 40, 55, 60])

# Calcular el tiempo promedio
promedio = np.mean(tiempos_consultas)
print("Tiempo promedio de consulta:", promedio, "minutos")

# Calcular la desviación estándar (variabilidad)
desviacion = np.std(tiempos_consultas)
print("Desviación estándar:", desviacion)
