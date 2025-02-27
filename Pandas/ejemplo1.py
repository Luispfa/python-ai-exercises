import pandas as pd
import os

# Obtener la ruta absoluta del directorio actual
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "citas.csv")

# Cargar datos desde un archivo CSV
# Suponiendo que tienes un archivo "citas.csv" en tu directorio actual
citas = pd.read_csv(csv_path)

# Mostrar las primeras 5 filas del DataFrame
print("Datos de citas:")
print(citas.head())

# Calcular cuántas citas hay por día
citas_por_dia = citas['Fecha'].value_counts()
print("\nCitas por día:")
print(citas_por_dia)
