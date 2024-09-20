import pandas as pd
from zenml import step
from zenml.logger import get_logger
from steps.src.data_processor import CategoricalEncoder
from steps.src.feature_eng import DateFeatureEngineer

logger= get_logger(__name__)

@step
def catagorical_encoding(df:pd.DataFrame)->pd.DataFrame:
    try:
        encoder= CategoricalEncoder(method="oneshot")
        df=encoder.fit_transform(df,columns=["product_id","product_category_name"])
        return df
    except Exception as e:
        raise e
    
@step
def feature_engg(df:pd.DataFrame)->pd.DataFrame:
    try:
        date_enginer=DateFeatureEngineer(date_format="%d-%m-%Y")
        df_transformed= date_enginer.fit_transform(df,columns=["month_year"])
        logger.info("Successfully engineered features")

        df_transformed.drop(["id","month_year"],axis=1,inplace=True)
        return df_transformed
    except Exception as e:
        raise e