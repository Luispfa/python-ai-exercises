import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from docker.python.Database.table_data import load_table_data

def train_citas_model():
    df = load_table_data("citas")
    if df is None:
        return None
    
    X = pd.DataFrame(index=range(len(df)), data={'dummy': [1] * len(df)})  # Característica dummy para regresión simple
    y = df['duracion_minutos']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Error cuadrático medio: {mse}")

    return model

if __name__ == "__main__":
    train_citas_model()