import pandas as pd
from src.ingest_data import DataIngestorFactory
from zenml import Step


@Step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    '''Data Ingestion Step
    
    This step is used to ingest data from a file path.
    
    Args:
        file_path (str): The path to the file to ingest.
        
    Returns:
        pd.DataFrame: The ingested data.
    '''
    
    ##Detect the file type
    file_extension=".zip"

    ##Ingest the data
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    
    df=data_ingestor.ingest_data(file_path)
    return df