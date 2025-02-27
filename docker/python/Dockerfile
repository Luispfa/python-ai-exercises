# Usa la última versión oficial de Python como imagen base
FROM python:latest

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos
COPY docker/python/requirements.txt ./

# Actualizamos pip e instalamos las dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expone el puerto 5000 para que Flask pueda atender las peticiones
EXPOSE 5000

# Al iniciar, abriremos una terminal (bash) para trabajar de forma interactiva
CMD ["bash"]

# Iniciar la aplicación Flask en el puerto 5000, escuchando en 0.0.0.0
# CMD ["python", "gestion_de_citas_inteligente_ui.py"]