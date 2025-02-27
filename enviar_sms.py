from twilio.rest import Client
import os
from dotenv import load_dotenv

def enviar_recordatorio_sms(cita, numero_destino):
    """
    Envía un recordatorio de cita por SMS utilizando Twilio.
    
    'cita' es una tupla con (id, fecha, hora, paciente, doctor)
    'numero_destino' es el número de teléfono del paciente en formato internacional (ej. "+1234567890").
    """
    
    # Acceder a las variables de entorno
    load_dotenv()
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE = os.getenv("TWILIO_PHONE")
    
    account_sid = TWILIO_ACCOUNT_SID  # Reemplaza con tu Account SID de Twilio
    auth_token = TWILIO_AUTH_TOKEN      # Reemplaza con tu Auth Token de Twilio
    client = Client(account_sid, auth_token)
    
    mensaje = client.messages.create(
        body=f"Recordatorio: Cita para {cita[3]} con el Dr. {cita[4]} el {cita[1]} a las {cita[2]}.",
        from_=TWILIO_PHONE,  # Tu número de teléfono asignado por Twilio
        to=numero_destino
    )
    
    print(f"Recordatorio SMS enviado exitosamente. SID: {mensaje.sid}")

# Ejemplo de uso:
# Supongamos que tenemos una cita:
cita_ejemplo = (1, "2023-08-15", "10:00", "Juan Pérez", "García")
# Y el número de teléfono del paciente es:
numero_paciente = "+34644254451"
# Para enviar el recordatorio, simplemente llamamos:
enviar_recordatorio_sms(cita_ejemplo, numero_paciente)
