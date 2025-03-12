import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from docker.python.Database.table_data import load_table_data

def entrenar_modelo():
    df = load_table_data("citas")
    if df is None:
        return None

    df['dia_semana'] = df['fecha_hora'].apply(lambda x: x.weekday())
    df['hora_cita'] = df['fecha_hora'].apply(lambda x: x.hour)

    X = df[['dia_semana', 'hora_cita', 'doctor_id']]
    y = df['duracion_minutos']

    modelo = RandomForestRegressor(random_state=42)
    modelo.fit(X, y)  # Entrenar con todos los datos
    return modelo

def predecir_duracion_cita(modelo, dia_semana, hora_cita, doctor_id):
    nueva_cita = pd.DataFrame({'dia_semana': [dia_semana], 'hora_cita': [hora_cita], 'doctor_id': [doctor_id]})
    duracion_predicha = modelo.predict(nueva_cita)[0]
    return duracion_predicha

if __name__ == "__main__":
    modelo_entrenado = entrenar_modelo()
    if modelo_entrenado:
        # Ejemplo de predicción
        dia_semana = 3  # Jueves
        hora_cita = 14  # 2 PM
        doctor_id = 2 # Dr. Pérez
        duracion_predicha = predecir_duracion_cita(modelo_entrenado, dia_semana, hora_cita, doctor_id)
        print(f"Duración predicha de la cita: {duracion_predicha:.2f} minutos")