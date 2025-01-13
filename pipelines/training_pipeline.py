import sys
import os
from zenml import pipeline, Model
from zenml import step

# Add the root directory to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)


from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step

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

    ## Data Ingestion
    raw_data = data_ingestion_step(
        file_path="data/archive.zip"
    )

    ## Handle Missing Values
    filled_data = handle_missing_values_step(raw_data)

    ## Feature Engineering
    engineered_data = feature_engineering_step(
        filled_data, strategy="log", features=['SalePrice', 'Gr Liv Area']
    )

    # You can add more steps here, such as model training, evaluation, etc.

# Run the pipeline
if __name__ == "__main__":
    ml_pipeline()