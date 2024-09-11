import pandas as pd
from zenml import step
from zenml.logger import get_logger
from steps.src.data_processor import CategoricalEncoder

logger= get_logger(__name__)

@step()
def catagorical_encoding(df:pd.DataFrame)->pd.DataFrame:
    try:
        encoder= CategoricalEncoder(method="oneshot")
        df=encoder.fit_transform(df,columns=["product_id","product_category_name"])
        return df
    except Exception as e:
        raise e