import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def load_citas_data():
    try:
        engine = create_engine(f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}")
        query = "SELECT * FROM citas"
        df = pd.read_sql(query, engine)
        return df
    except Exception as err:
        print(f"Error al cargar datos de citas: {err}")
        return None