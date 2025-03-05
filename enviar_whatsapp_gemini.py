import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pyngrok import ngrok

# Cargar variables de entorno
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NGROK_AUTHTOKEN = os.getenv("NGROK_AUTHTOKEN")

# Configurar la API de Gemini
genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

def get_ai_response(user_message):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest") # Usando el modelo recomendado
        response = model.generate_content(user_message)
        return response.text.strip()
    except Exception as e:
        print(f"Error con Gemini: {e}")
        return "Lo siento, ha ocurrido un error al procesar tu consulta. Por favor, inténtalo de nuevo más tarde."

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.form.get('Body')
    response_text = get_ai_response(incoming_msg)
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

def start_ngrok():
    if not NGROK_AUTHTOKEN:
        raise ValueError("Error: NGROK_AUTHTOKEN no está definido. Verifica las variables de entorno.")

    ngrok.set_auth_token(NGROK_AUTHTOKEN)
    tunnel = ngrok.connect(5000)
    print(f"Ngrok tunnel {tunnel.public_url} -> http://127.0.0.1:5000")
    return tunnel

def stop_ngrok(tunnel):
    if tunnel:
        ngrok.disconnect(tunnel.public_url)
        print("Ngrok tunnel disconnected.")

if __name__ == '__main__':
    try:
        tunnel = start_ngrok()
        app.run(host="0.0.0.0", port=5000, debug=False)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        stop_ngrok(tunnel)