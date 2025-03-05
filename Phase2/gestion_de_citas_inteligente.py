import sqlite3
from datetime import datetime, timedelta

def crear_base_de_datos():
    """
    Conecta a una base de datos SQLite (o la crea si no existe) y crea
    la tabla 'citas' para almacenar la información de las citas.
    La tab
    """
    
    conexion = sqlite3.connect('clinica_dental_inteligente.db')    
    cursor = conexion.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            hora TEXT,
            paciente TEXT,
            doctor TEXT,
            UNIQUE(doctor, fecha, hora)
        )
    """)
    
    conexion.commit()
    return conexion

def registrar_cita(conexion, fecha, hora, paciente, doctor):
    """
    Inserta una nueva cita en la base de datos.
    Si ya existe una cita para el mismo doctor en esa fecha y hora, se muestra un error.
    """
    cursor= conexion.cursor()
    try:
        cursor.execute("INSERT INTO citas (fecha, hora, paciente, doctor) VALUES (?, ?, ?, ?)", 
                       (fecha, hora, paciente, doctor))
        conexion.commit()
        print(f"Cita registrada exitosamente para el Dr. {doctor}.")
    except sqlite3.IntegrityError:
        print(f"Error: El Dr. {doctor} ya tiene una cita programada el {fecha} a las {hora}.")

def consultar_citas(conexion):
    """
    Recupera todas las citas registradas en la base de datos.
    """
    cursor = conexion.cursor()
    cursor.execute("SELECt * FROM citas")
    citas = cursor.fetchall()
    
    return citas

def consultar_disponibilidad(conexion, doctor, fecha):
    """
    Consulta las horas ocupadas para un doctor en una fecha específica.
    Devuel
    """
    cursor = conexion.cursor()
    cursor.execute("SELECT hora FROM citas WHERE doctor = ? AND fecha = ?", (doctor, fecha))
    horas_ocupadas = [row[0] for row in cursor.fetchall()]
    
    return horas_ocupadas

def visualizar_disponibilidad(conexion, doctor, fecha, hora_inicio="09:00", hora_fin="17:00"):
    """
    Muestra las franjas horarias disponibles para un doctor en una fecha determinada,
    considerando el horario de atención (por defecto de 09:00 a 17:00).
    """
    # Generar la lista de franjas horarias (citas cada hora)
    formato_hora = "%H:%M"
    inicio = datetime.strptime(hora_inicio, formato_hora)
    fin = datetime.strptime(hora_fin, formato_hora)
    franjas = []
    while inicio <= fin:
        franjas.append(inicio.strftime(formato_hora))
        inicio += timedelta(hours=1)
        
    # Obtener las horas ocupadas para el doctor en esa fecha
    horas_ocupadas = consultar_disponibilidad(conexion, doctor, fecha)
    
    # Calcular las franjas libres
    franjas_libres = [hora for hora in franjas if hora not in horas_ocupadas]
    
    print(f"\nDisponibilidad para el Dr. {doctor} en {fecha}:")
    print("Horas ocupadas:", horas_ocupadas)
    print("Horas disponibles:", franjas_libres)
    return franjas_libres

def modificar_cita(conexion, cita_id, nueva_fecha, nueva_hora, nuevo_doctor, nuevo_paciente):
    """
    Modifica una cita existente dada su ID.
    Permite cambiar fecha, hora, doctor y paciente.
    """
    cursor  =conexion.cursor()
    try:
        cursor.execute("""
            UPDATE citas
            SET fecha = ?, hora = ?, doctor = ?, paciente = ?
            WHERE id = ?
        """, (nueva_fecha, nueva_hora, nuevo_doctor, nuevo_paciente, cita_id))
        conexion.commit()
        
        if cursor.rowcount > 0:
            print(f"Cita {cita_id} modificada exitosamente.")
        else:
            print(f"No se encontró la cita con ID {cita_id}.")
    except sqlite3.IntegrityError:
        print(f"Error: El Dr. {nuevo_doctor} ya tiene una cita programada el {nueva_fecha} a las {nueva_hora}.")

def cancelar_cita(conexion, cita_id):
    """
    Cancela (elimina) una cita dada su ID.
    """
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM citas WHERE id = ?", (cita_id,))
    conexion.commit()
    if cursor.rowcount > 0:
        print(f"Cita {cita_id} cancelada exitosamente.")
    else:
        print(f"No se encontró la cita con ID {cita_id}.")
        
def enviar_recordatorio(cita):
    """
    Simula el envío de un recordatorio para una cita.
    'cita' es una tupla con (id, fecha, hora, paciente, doctor).
    """
    # Usamos los índices según el orden de las columnas:
    # cita[1] = fecha, cita[2] = hora, cita[3] = paciente, cita[4] = doctor.
    print(f"Recordatorio: Cita para el paciente {cita[3]} con el Dr. {cita[4]} programada el {cita[1]} a las {cita[2]}.")


def main():
    conexion = crear_base_de_datos()
    
    while True:
        print("\nMenú de Agenda Inteligente:")
        print("1. Registrar nueva cita")
        print("2. Visualizar disponibilidad de un doctor")
        print("3. Modificar cita")
        print("4. Cancelar cita")
        print("5. Ver todas las citas")
        print("6. Enviar recordatorios")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\nRegistro de nueva cita:")
            fecha = input("Fecha (YYYY-MM-DD): ")
            hora = input("Hora (HH:MM): ")
            paciente = input("Nombre del paciente: ")
            doctor = input("Nombre del doctor: ")
            registrar_cita(conexion, fecha, hora, paciente, doctor)
        elif opcion == "2":
            print("\nVisualizar disponibilidad:")
            doctor = input("Nombre del doctor: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            visualizar_disponibilidad(conexion, doctor, fecha)
        elif opcion == "3":
            print("\nModificar cita:")
            cita_id = input("Ingrese el ID de la cita a modificar: ")
            nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ")
            nueva_hora = input("Nueva hora (HH:MM): ")
            nuevo_paciente = input("Nuevo nombre del paciente: ")
            nuevo_doctor = input("Nuevo nombre del doctor: ")
            modificar_cita(conexion, cita_id, nueva_fecha, nueva_hora, nuevo_doctor, nuevo_paciente)
        elif opcion == "4":
            print("\nCancelar cita:")
            cita_id = input("Ingrese el ID de la cita a cancelar: ")
            cancelar_cita(conexion, cita_id)
        elif opcion == "5":
            print("\nCitas registradas:")
            citas = consultar_citas(conexion)
            for cita in citas:
                print(cita)
        elif opcion == "6":
            print("\nEnviando recordatorios para todas las citas:")
            citas = consultar_citas(conexion)
            for cita in citas:
                enviar_recordatorio(cita)
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    # Cerrar la conexión a la base de datos
    conexion.close()

if __name__ == "__main__":
    main()
    


