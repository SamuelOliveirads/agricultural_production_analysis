import pandas as pd
from sqlalchemy import create_engine
import os

def load_data():
    connection_str = os.environ.get('DATABASE_URL')
    engine = create_engine(connection_str)
    query_crop_data = "SELECT * FROM crop.crop_data;"
    df_crop_data = pd.read_sql(query_crop_data, engine)

    cod_municipios = pd.read_json('../dataset/ibge_municipios.json')
    cod_municipios = cod_municipios.rename(columns={'ibge_code': 'cod_municipio'})

    commodities_data = df_crop_data.merge(cod_municipios, on='cod_municipio')

    return commodities_data
