import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split
class DataSplitter:
    def __init__(self,df:pd.Dataframe,features:List[str],target:str,test_size:float=0.2):
        self.df=df
        self.features=features
        self.target=target
        self.test_size=test_size

    def split(self)-> tuple[pd.DataFrame,pd.DataFrame,pd.Series,pd.Series]:
        X=self.df[self.features]
        y=self.df[self.target]
        X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=self.test_size,shuffle=False)
        return X_train,X_test,y_train,y_test