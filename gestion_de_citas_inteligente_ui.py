from flask import Flask, request, redirect, url_for, render_template_string
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
DATABASE = "clinica_dental_ia.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            hora TEXT,
            paciente TEXT,
            doctor TEXT,
            UNIQUE(doctor, fecha, hora)
        )
    """)
    conn.commit()
    conn.close()

# Inicializa la base de datos al iniciar la aplicación
init_db()

@app.route('/')
def index():
    return render_template_string("""
    <h1>Agenda Inteligente - Clínica Dental</h1>
    <ul>
      <li><a href="{{ url_for('ver_citas') }}">Ver Citas</a></li>
      <li><a href="{{ url_for('registrar_cita') }}">Registrar Cita</a></li>
      <li><a href="{{ url_for('consultar_disponibilidad') }}">Consultar Disponibilidad</a></li>
    </ul>
    """)

@app.route('/citas')
def ver_citas():
    conn = get_db_connection()
    citas = conn.execute("SELECT * FROM citas").fetchall()
    conn.close()
    html = "<h1>Citas Registradas</h1><ul>"
    for cita in citas:
        html += f"<li>ID: {cita['id']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}, Paciente: {cita['paciente']}, Doctor: {cita['doctor']}</li>"
    html += "</ul><a href='/'>Volver al inicio</a>"
    return html

@app.route('/registrar', methods=['GET', 'POST'])
def registrar_cita():
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        paciente = request.form['paciente']
        doctor = request.form['doctor']
        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO citas (fecha, hora, paciente, doctor) VALUES (?, ?, ?, ?)",
                         (fecha, hora, paciente, doctor))
            conn.commit()
            mensaje = "Cita registrada exitosamente."
        except sqlite3.IntegrityError:
            mensaje = f"Error: El Dr. {doctor} ya tiene una cita programada el {fecha} a las {hora}."
        conn.close()
        return render_template_string("""
        <h1>Registrar Cita</h1>
        <p>{{ mensaje }}</p>
        <a href="{{ url_for('registrar_cita') }}">Registrar otra cita</a> | <a href="{{ url_for('index') }}">Inicio</a>
        """, mensaje=mensaje)
    return render_template_string("""
    <h1>Registrar Cita</h1>
    <form method="post">
      Fecha (YYYY-MM-DD): <input type="text" name="fecha"><br>
      Hora (HH:MM): <input type="text" name="hora"><br>
      Nombre del paciente: <input type="text" name="paciente"><br>
      Nombre del doctor: <input type="text" name="doctor"><br>
      <input type="submit" value="Registrar">
    </form>
    <a href="{{ url_for('index') }}">Volver al inicio</a>
    """)

@app.route('/disponibilidad', methods=['GET', 'POST'])
def consultar_disponibilidad():
    if request.method == 'POST':
        doctor = request.form['doctor']
        fecha = request.form['fecha']
        # Definir el horario de atención: de 09:00 a 17:00 (citas cada hora)
        hora_inicio = "09:00"
        hora_fin = "17:00"
        formato_hora = "%H:%M"
        inicio = datetime.strptime(hora_inicio, formato_hora)
        fin = datetime.strptime(hora_fin, formato_hora)
        franjas = []
        while inicio <= fin:
            franjas.append(inicio.strftime(formato_hora))
            inicio += timedelta(hours=1)
        # Consultar las horas ocupadas para el doctor en la fecha indicada
        conn = get_db_connection()
        horas_ocupadas = conn.execute("SELECT hora FROM citas WHERE doctor = ? AND fecha = ?", (doctor, fecha)).fetchall()
        conn.close()
        horas_ocupadas = [row['hora'] for row in horas_ocupadas]
        # Determinar las franjas libres
        franjas_libres = [h for h in franjas if h not in horas_ocupadas]
        return render_template_string("""
        <h1>Disponibilidad del Dr. {{ doctor }} en {{ fecha }}</h1>
        <p><strong>Horas ocupadas:</strong> {{ horas_ocupadas }}</p>
        <p><strong>Horas disponibles:</strong> {{ franjas_libres }}</p>
        <a href="{{ url_for('consultar_disponibilidad') }}">Consultar otra disponibilidad</a> | <a href="{{ url_for('index') }}">Inicio</a>
        """, doctor=doctor, fecha=fecha, horas_ocupadas=horas_ocupadas, franjas_libres=franjas_libres)
    return render_template_string("""
    <h1>Consultar Disponibilidad</h1>
    <form method="post">
      Nombre del doctor: <input type="text" name="doctor"><br>
      Fecha (YYYY-MM-DD): <input type="text" name="fecha"><br>
      <input type="submit" value="Consultar">
    </form>
    <a href="{{ url_for('index') }}">Volver al inicio</a>
    """)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
