import pandas as pd
import matplotlib.pyplot as plt
import os

# root_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio donde está el script
# matplotlib_dir = os.path.join(root_dir)  # Asegura que apunta a Matplotlib
# # Ruta del archivo CSV en Matplotlib
# csv_path = os.path.join(matplotlib_dir, "citas.csv")

# Leer datos desde un archivo CSV
df = pd.read_csv("Matplotlib/citas.csv")

# Convertir la columna 'Fecha' a tipo datetime (importante para ordenar correctamente)
df["Fecha"] = pd.to_datetime(df["Fecha"], format="%Y-%m-%d")  # Ajusta el formato según tu CSV

# Contar citas por día
citas_por_dia = df["Fecha"].value_counts()

# Crear un gráfico de barras
citas_por_dia.sort_index(inplace=True)  # Ordenar por fecha para una mejor visualización
citas_por_dia.plot(kind='bar', color='skyblue', edgecolor='black')

# Personalizar el gráfico
plt.xlabel("Fecha")
plt.ylabel("Número de Citas")
plt.title("Citas Diarias en la Clínica Dental")
plt.xticks(rotation=45)  # Rotar etiquetas para mejor legibilidad
plt.tight_layout()  # Ajustar el layout para que no se solapen elementos
# plt.show()
plt.savefig("Matplotlib/citas_diarias.png", dpi=300, bbox_inches="tight")
# Cerrar la figura para liberar memoria
plt.close()