import spacy
import pandas as pd
from docker.python.Database.table_data import load_table_data
import os
from dotenv import load_dotenv

load_dotenv()

# Cargar el modelo de lenguaje en español
# nlp = spacy.load("es_core_news_sm")
# nlp = spacy.load("es_core_news_md")
nlp = spacy.load("es_core_news_lg")

# Cargar datos de las tablas usando table_data.py
notas_df = load_table_data("notas_clinicas")
correos_df = load_table_data("correos_pacientes")
faq_df = load_table_data("faq")

if notas_df is not None:
    # Procesar notas clínicas
    print("Procesando notas clínicas:")
    for index, row in notas_df.iterrows():
        nota = row['texto']
        doc = nlp(nota)
        paciente = None
        fecha = None
        hora = None

        for ent in doc.ents:
            if ent.label_ == "PER":
                paciente = ent.text
            elif ent.label_ == "DATE":
                fecha = ent.text
            elif ent.label_ == "TIME":
                hora = ent.text

        if paciente and fecha:
            print(f"  Paciente: {paciente}, Fecha: {fecha}, Hora: {hora}")
        elif paciente:
            print(f"  Paciente: {paciente}")

if correos_df is not None:
    # Procesar correos electrónicos de pacientes
    print("\nProcesando correos electrónicos de pacientes:")
    for index, row in correos_df.iterrows():
        asunto = row['asunto']
        cuerpo = row['cuerpo']
        doc = nlp(cuerpo)
        paciente = None

        for ent in doc.ents:
            if ent.label_ == "PER":
                paciente = ent.text

        if paciente:
            print(f"  Asunto: {asunto}, Paciente: {paciente}")
        else:
            print(f"  Asunto: {asunto}, Paciente: No detectado")

if faq_df is not None:
    # Procesar preguntas frecuentes (FAQ)
    print("\nProcesando preguntas frecuentes (FAQ):")
    for index, row in faq_df.iterrows():
        pregunta = row['pregunta']
        respuesta = row['respuesta']
        doc = nlp(pregunta)
        entidades = [ent.text for ent in doc.ents]

        print(f"  Pregunta: {pregunta}, Entidades: {entidades}")