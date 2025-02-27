import sqlite3

def crear_base_datos():
    """
    Conecta a una base de datos SQLite (o la crea si no existe) y crea
    la tabla 'citas' para almacenar la información de las citas.
    """
    # Conecta a la base de datos (el archivo se llamará "clinica_dental.db")
    conexion = sqlite3.connect("clinica_dental.db")
    cursor = conexion.cursor()
    
    # Crea la tabla "citas" si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            hora TEXT,
            paciente TEXT
        )
    """)
    conexion.commit()
    return conexion

def registrar_cita(conexion, fecha, hora, paciente):
    """
    Inserta una nueva cita en la base de datos.
    """
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO citas (fecha, hora, paciente) VALUES (?, ?, ?)", 
                   (fecha, hora, paciente))
    conexion.commit()
    print("Cita registrada exitosamente.")

def consultar_citas(conexion):
    """
    Recupera todas las citas registradas en la base de datos.
    """
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM citas")
    citas = cursor.fetchall()
    return citas

def enviar_recordatorio(cita):
    """
    Simula el envío de un recordatorio para una cita.
    Aquí, 'cita' es una tupla con (id, fecha, hora, paciente).
    """
    print(f"Recordatorio: Cita para {cita[3]} programada el {cita[1]} a las {cita[2]}.")

def main():
    # Crear o conectar a la base de datos
    conexion = crear_base_datos()
    
    # Registrar una nueva cita: se solicitan datos al usuario
    print("Ingrese los datos de la cita:")
    fecha = input("Fecha (YYYY-MM-DD): ")
    hora = input("Hora (HH:MM): ")
    paciente = input("Nombre del paciente: ")
    
    registrar_cita(conexion, fecha, hora, paciente)
    
    # Consultar y mostrar todas las citas registradas
    citas = consultar_citas(conexion)
    print("\nCitas registradas:")
    for cita in citas:
        print(cita)
    
    # Simular el envío de recordatorios a cada cita registrada
    print("\nEnviando recordatorios...")
    for cita in citas:
        enviar_recordatorio(cita)
    
    # Cerrar la conexión a la base de datos
    conexion.close()

if __name__ == "__main__":
    main()
