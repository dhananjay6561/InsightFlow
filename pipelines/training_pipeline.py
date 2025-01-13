from zenml import pipeline, Model
from zenml import step
from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step

## Define a pipeline
@pipeline(

    model=Model(
       name='insightflow',
    ),
)

def ml_pipeline():
    '''Define a pipeline
    
    This pipeline is used to train a model on the insightflow dataset.
    '''

    ##Data Ingestion
    raw_data = data_ingestion_step(
        file_path="data/archive.zip"
    )

    ##Handle Missing Values

    filled_data = handle_missing_values_step(raw_data)
     