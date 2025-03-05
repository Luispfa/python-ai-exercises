import os
from dotenv import load_dotenv
import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pyngrok import ngrok
import subprocess

app = Flask(__name__)

# Cargar variables de entorno
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("Error: OPENAI_API_KEY no está definido. Verifica las variables de entorno.")

def get_ai_response(user_message):
    try:
        client = openai.OpenAI(api_key=openai_api_key)  # Crear cliente correctamente

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente virtual para una clínica dental."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error con OpenAI:", e)
        return "Lo siento, ha ocurrido un error al procesar tu consulta."

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.form.get('Body', '')
    response_text = get_ai_response(incoming_msg)
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

if __name__ == '__main__':
    # Inicia un túnel ngrok en el puerto 5000
    subprocess.run(["pkill", "-f", "ngrok"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    authtoken = os.getenv("NGROK_AUTHTOKEN")

    if not authtoken:
        raise ValueError("Error: NGROK_AUTHTOKEN no está definido. Verifica las variables de entorno.")

    ngrok.set_auth_token(authtoken)
    tunnel = ngrok.connect(5000)
    print(f"Ngrok tunnel \"{tunnel.public_url}\" -> \"http://127.0.0.1:5000\"")

    app.run(host="0.0.0.0", port=5000, debug=False)
