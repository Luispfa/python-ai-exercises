import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

def enviar_recordatorio_email(cita, destinatario):
    """
    Envía un recordatorio de cita por email.
    
    'cita' es una tupla con (id, fecha, hora, paciente, doctor)
    'destinatario' es el email del paciente.
    """
    subject = "Recordatorio de Cita - Clínica Dental"
    body = (
        f"Estimado/a {cita[3]},\n\n"
        f"Le recordamos su cita programada con el Dr. {cita[4]} el {cita[1]} a las {cita[2]}.\n\n"
        "Saludos cordiales,\nClínica Dental"
    )

    # Acceder a las variables de entorno
    load_dotenv()
    EMAIL = os.getenv("EMAIL")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    
    remitente = EMAIL  # Tu email
    password = EMAIL_PASSWORD # Tu contraseña (considera usar variables de entorno)
    
    # Crear el mensaje de correo
    msg = MIMEMultipart()
    msg["From"] = remitente
    msg["To"] = destinatario
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    try:
        # Conectar al servidor SMTP de Gmail (puedes usar otro servidor si lo prefieres)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Iniciar conexión segura
        server.login(remitente, password)
        server.sendmail(remitente, destinatario, msg.as_string())
        server.quit()
        print(f"Recordatorio enviado exitosamente a {destinatario}")
    except Exception as e:
        print("Error al enviar el recordatorio por email:", e)

# Ejemplo de uso:
# Supongamos que tenemos una cita:
cita_ejemplo = (1, "2023-08-15", "10:00", "Juan Pérez", "García")
# Y el email del paciente es:
email_paciente = "luispfa@gmail.com"
# Para enviar el recordatorio, simplemente llamamos:
enviar_recordatorio_email(cita_ejemplo, email_paciente)
