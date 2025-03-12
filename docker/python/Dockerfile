# Usa la última versión oficial de Python como imagen base
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos
COPY docker/python/requirements.txt ./

# Actualizamos los paquetes del sistema e instalamos dependencias de compilación
RUN apt-get update && apt-get install -y build-essential

# Limpiamos la caché de pip
RUN pip cache purge

# Actualizamos pip y setuptools e instalamos las dependencias de Python
RUN pip install --upgrade pip setuptools && pip install -r requirements.txt

# Descargamos el modelo de spaCy en español
#recurso small
# RUN python -m spacy download es_core_news_sm 

#recurso medium 
# RUN python -m spacy download es_core_news_md 

#recurso large
RUN python -m spacy download es_core_news_lg 

# Expone el puerto 5000 para que Flask pueda atender las peticiones
EXPOSE 5000

# Al iniciar, abriremos una terminal (bash) para trabajar de forma interactiva
CMD ["bash"]

# Iniciar la aplicación Flask en el puerto 5000, escuchando en 0.0.0.0
# CMD ["python", "gestion_de_citas_inteligente_ui.py"]