import logging
import pandas as pd
from zenml import step
from steps.src.data_loader import DataLoader

@step(enable_cache=False)
def ingest_data(
    table_name:str,
)->pd.DataFrame:
    try:
        data_loader=DataLoader('DATABASE_URL=postgresql://postgresql:Vedank28w@K@localhost:5432/mydb')
        data_loader.loadData(table_name)
        df= data_loader.getData()
        logging.info("Successfully read data from {table_name}")
        return df
    except Exception as e:
        raise e