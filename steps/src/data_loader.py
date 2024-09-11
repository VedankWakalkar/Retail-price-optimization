import pandas as pd
from sqlalchemy import create_engine,exc

class DataLoader:
    def __init__(self,db_url:str):
        self.db_url=db_url
        self.engine=create_engine(self.db_url)
        self.data=None
    
    def loadData(self,table_name:str)->pd.DataFrame:
        query="SELECT * FROM" +table_name
        try:
            self.data=pd.read_sql(query,self.engine)
            return self.data
        except exc.SQLAlchemyError as e:
            raise e
    
    def getData(self)->pd.DataFrame:
        if self.data is not None:
            return self.data
        else:
            raise ValueError("No data loaded yet. Please run loadData() first.")