import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import citas_data
import datetime

def optimize_citas():
    df = citas_data.load_citas_data()
    if df is None:
        return

    # Ingeniería de características (ejemplo)
    df['dia_semana'] = df['fecha_hora'].apply(lambda x: x.weekday())
    df['hora_cita'] = df['fecha_hora'].apply(lambda x: x.hour)

    X = df[['dia_semana', 'hora_cita']]
    y = df['duracion_minutos']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modelos
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(random_state=42)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"Modelo: {name}, MSE: {mse}, MAE: {mae}, R2: {r2}")

if __name__ == "__main__":
    optimize_citas()