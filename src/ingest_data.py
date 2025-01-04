import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd


## Defining the abstract class for data ingestion
class IngestData(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Abstract method to ingest data from a file"""
        pass


## Defining the class for ingesting data from a csv file
class IngestCSVData(IngestData):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Ingest data from a csv file"""
        
        ## Ensure the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        ## Ensuring that the file is .zip
        if not file_path.endswith('.zip'):
            raise ValueError("File must be a .zip file")
        
        ## Create a directory named "extracted_data" in the root directory
        extracted_dir = os.path.abspath(os.path.join("..", "extracted_data"))  # Root directory
        os.makedirs(extracted_dir, exist_ok=True)  # Create the directory if it doesn't exist
        
        ## Extracting the file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extracted_dir)
        
        ## Finding the extracted CSV file
        extracted_files = os.listdir(extracted_dir)
        csv_files = [f for f in extracted_files if f.endswith('.csv')]

        if len(csv_files) == 0:
            raise ValueError("No CSV file found in extracted data")
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found in extracted data")
        
        ## Reading the CSV file into a pandas dataframe
        df = pd.read_csv(os.path.join(extracted_dir, csv_files[0]))

        ## Returning the dataframe
        return df


class DataIngestorFactory:
    @staticmethod
    def get_ingestor(file_extension: str) -> IngestData:
        """Factory method to return the appropriate data ingestor"""
        
        ## Checking if the file is a .zip file
        if file_extension == '.zip':        
            return IngestCSVData()
        else:
            raise ValueError(f"No ingestor available for file type {file_extension}")


## Example usage
if __name__ == "__main__":
    # Construct the correct file path
    file_path = os.path.abspath(os.path.join("..", "data", "archive.zip"))  # Move up one level to the project root
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
    else:
        file_extension = os.path.splitext(file_path)[1]
        ingestor = DataIngestorFactory.get_ingestor(file_extension)
        df = ingestor.ingest(file_path)
        print(df.head())