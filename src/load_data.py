import pandas as pd
from sqlalchemy import create_engine
import os

def load_data() -> pd.DataFrame:
    connection_str = os.environ.get('DATABASE_URL')
    engine = create_engine(connection_str)
    
    df_crop_data = pd.read_sql("SELECT * FROM crop.crop_data;", engine)
    df_cod_municipios = pd.read_sql("SELECT * FROM crop.cod_municipios;", engine)

    commodities_data = df_crop_data.merge(df_cod_municipios, on='cod_municipio')

    return commodities_data
