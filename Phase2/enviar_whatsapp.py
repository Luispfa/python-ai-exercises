from twilio.rest import Client
import os
from dotenv import load_dotenv

# Reemplaza con tus credenciales de Twilio
load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP = os.getenv("TWILIO_WHATSAPP")
# TWILIO_WHATSAPP_CODE=graph-wolf

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    from_=f"whatsapp:{TWILIO_WHATSAPP}",  # Número de la Sandbox de Twilio
    body="Hola, este es un mensaje de prueba desde Twilio Sandbox.",
    to="whatsapp:+34644254451"       # Tu número que ya se unió a la Sandbox
)

print("Mensaje enviado, SID:", message.sid)
