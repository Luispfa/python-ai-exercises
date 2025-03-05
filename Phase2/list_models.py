import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configurar la API de Gemini
genai.configure(api_key=GEMINI_API_KEY)

def list_available_models():
    try:
        for model in genai.list_models():
            print(f"Modelo: {model.name}")
            print(f"Descripción: {model.description}")
            print(f"Versiones soportadas: {model.supported_generation_methods}")
            print("-" * 20)
    except Exception as e:
        print(f"Error al listar modelos: {e}")

if __name__ == "__main__":
    list_available_models()