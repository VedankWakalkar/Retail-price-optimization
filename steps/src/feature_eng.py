from abc import ABC,abstractmethod
from typing import List
import pandas as pd

class FeatureEngineer(ABC):
    @abstractmethod
    def fit_transform(self, df:pd.DataFrame,columns:List[str])->pd.DataFrame:
         
class DataFeatureEngineer()