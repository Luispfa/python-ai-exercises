import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def setup_database():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        cursor = connection.cursor()

        with open("clinica_dental_schema.sql", "r") as sql_file:
            sql_script = sql_file.read()
            sql_commands = sql_script.split(';')  # Split the SQL script into individual commands

            for command in sql_commands:
                command = command.strip()  # Remove leading/trailing whitespace
                if command:  # Check if the command is not empty
                    cursor.execute(command)
                    connection.commit()  # Commit after each command

        cursor.close()
        connection.close()
        print("Base de datos configurada correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al configurar la base de datos: {err}")

if __name__ == "__main__":
    setup_database()