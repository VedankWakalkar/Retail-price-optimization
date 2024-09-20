from abc import ABC,abstractmethod
from typing import List
import pandas as pd

class FeatureEngineer(ABC):
    @abstractmethod
    def fit_transform(self, df:pd.DataFrame,columns:List[str])->pd.DataFrame:
        pass
         
class DateFeatureEngineer(FeatureEngineer):
    def __init__(self,date_format:str="%m-$d-%Y"):
        self.date_format= date_format

    def fit_transform(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        for column in columns:
            df=self.split_date(df,column)
        return df
    
    def split_date(self, df:pd.DataFrame, column:str)->pd.DataFrame:
         df[column]=pd.to_datetime(df[column],format=self.date_format)
         df[f'{column}_year']=df[column].dt.year
         df[f'{column}_month']=df[column].dt.month
         return df
    