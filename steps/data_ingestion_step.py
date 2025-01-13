import pandas as pd
from src.ingest_data import DataIngestorFactory
from zenml import step


@step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    '''Data Ingestion Step
    
    This step is used to ingest data from a file path.
    
    Args:
        file_path (str): The path to the file to ingest.
        
    Returns:
        pd.DataFrame: The ingested data.
    '''
    
    ## Detect the file type
    file_extension = ".zip"  # Assuming the file is a ZIP file

    ## Ingest the data
    data_ingestor = DataIngestorFactory.get_ingestor(file_extension) 
    
    df = data_ingestor.ingest(file_path) 
    return df