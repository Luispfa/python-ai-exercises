import spacy
import pandas as pd
from docker.python.Database.table_data import load_table_data
from sklearn.metrics.pairwise import cosine_similarity # Importar cosine_similarity


# Cargar modelo de spaCy
nlp = spacy.load("es_core_news_lg")

# Cargar datos de la base de datos
faq_df = load_table_data("faq")
citas_df = load_table_data("citas")

def obtener_respuesta_faq(pregunta):
    """Obtiene la respuesta de la FAQ basada en la pregunta."""
    doc = nlp(pregunta)
    pregunta_vector = doc.vector.reshape(1, -1)  # Obtener el vector de la pregunta

    mejor_similitud = -1
    mejor_respuesta = "Lo siento, no tengo información sobre eso."

    for index, row in faq_df.iterrows():
        pregunta_faq = row["pregunta"]
        doc_faq = nlp(pregunta_faq)
        faq_vector = doc_faq.vector.reshape(1, -1)  # Obtener el vector de la pregunta de la FAQ

        similitud = cosine_similarity(pregunta_vector, faq_vector)[0][0]  # Calcular la similitud del coseno

        if similitud > mejor_similitud:
            mejor_similitud = similitud
            mejor_respuesta = row["respuesta"]

    if mejor_similitud > 0.7:  # Umbral de similitud
        return mejor_respuesta
    else:
        return "Lo siento, no tengo información sobre eso."

def reservar_cita(pregunta):
    """Intenta reservar una cita basada en la pregunta."""
    doc = nlp(pregunta)
    fecha = None
    hora = None
    for ent in doc.ents:
        if ent.label_ == "DATE":
            fecha = ent.text
        elif ent.label_ == "TIME":
            hora = ent.text
    if fecha and hora:
        # Aquí iría la lógica para verificar disponibilidad y reservar la cita
        return f"Cita reservada para el {fecha} a las {hora}."
    else:
        return "No pude entender la fecha y hora de tu cita."

def chatbot():
    """Función principal del chatbot."""
    print("¡Hola! Soy el asistente virtual de la clínica dental. ¿En qué puedo ayudarte?")
    while True:
        pregunta = input("> ")
        if pregunta.lower() in ["adiós", "salir", "fin"]:
            print("¡Hasta luego!")
            break
        if "cita" in pregunta.lower():
            respuesta = reservar_cita(pregunta)
        else:
            respuesta = obtener_respuesta_faq(pregunta)
        print(respuesta)

if __name__ == "__main__":
    chatbot()