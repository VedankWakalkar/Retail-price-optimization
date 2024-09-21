from zenml.client import Client
from zenml.integrations.mlflow.experiment_trackers import MLFlowExperimentTracker
from sklearn.linear_model import LinearRegression
from zenml.integrations.mlflow.experiment_trackers import MLFlowExperimentTracker
from materializers.custom_materializer import SKLearnModelMaterializer,ListMaterializer,StatsModelMaterializer
import pandas as pd
from typing_extensions import Annotated
from zenml import step
from typing import List
import mlflow
import mlflow.sklearn 

experiment_tracker=Client().active_stack_experiment_tracker

if not experiment_tracker or not isinstance(experiment_tracker,MLFlowExperimentTracker):
    raise RuntimeError(
        "Your active status needs to contain a MLFlow experiment tracker for this example to work"
    )

@step(experiment_tracker="mlflow_tracker",
      settings={"experiment_tracker.mlflow":{"experiment_name":"test_name"}},
      enable_cache=False,output_materializers=[SKLearnModelMaterializer,ListMaterializer]
      )
def sklearn_train(
    X_train:Annotated[pd.DataFrame,"X_train"],
    y_train:Annotated[pd.Series,"y_train"]
)-> tuple[
    Annotated[LinearRegression,"model"],
    Annotated[List[str],"predictions"]
]:
    try:
        mlflow.end_run()
        with mlflow.start_run() as run:
            mlflow.sklearn.autolog()
            model=LinearRegression()
            model.fit(X_train,y_train)
            predictors=X_train.columns.tolist()
            return model,predictors
    except Exception as e:
        raise e