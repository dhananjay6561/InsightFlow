from abc import ABC, abstractmethod
import pandas as pd

## Defining the abstract class for data inspection strategies
## Subclasses must implement the inspect method
class DataInspection(ABC):
    @abstractmethod
    def inspect(self, data: pd.DataFrame):
        """Perform specific data inspection tasks.
        
        Parameters:
        data (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: This method prints the results of the inspection directly.
        """
        pass

## Strategy for basic data inspection
class DataTypeInspectionStrategy(DataInspection):
    def inspect(self, data: pd.DataFrame):
        """Inspect the data types of the columns in the dataframe and non-null counts.
        
        Parameters:
        data (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: This method prints the data types of the columns and non-null counts.
        """
        print("Data Types and Non-Null Counts:")
        print(data.info())

## Strategy for Summary Statistics Inspection
class SummaryStatisticsInspectionStrategy(DataInspection):
    def inspect(self, data: pd.DataFrame):
        """Inspect the summary statistics for numerical and categorical features in the dataframe.
        
        Parameters:
        data (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: This method prints the summary statistics of the dataframe.
        """
        print("Summary Statistics (Numerical Features):")
        print(data.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(data.describe(include=["object"]))

## Context Class for Data Inspection
class DataInspector:
    def __init__(self, strategy: DataInspection):
        """Initialize the DataInspector with a specific strategy.
        
        Parameters:
        strategy (DataInspection): The strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspection):
        """Set a new strategy for data inspection.
        
        Parameters:
        strategy (DataInspection): The new strategy to be used for data inspection.
        
        Returns:
        None
        """
        self._strategy = strategy

    def execute_inspection(self, data: pd.DataFrame):
        """Execute the data inspection strategy.
        
        Parameters:
        data (pd.DataFrame): The dataframe to be inspected.
        
        Returns:
        None
        """
        self._strategy.inspect(data)


## Example Usage
if __name__ == "__main__":
    ## Read the data into a pandas dataframe
    df = pd.read_csv("../../extracted_data/AmesHousing.csv")

    ## Create a DataInspector with the DataTypeInspectionStrategy
    inspector = DataInspector(DataTypeInspectionStrategy())
    inspector.execute_inspection(df)  ## Execute the data inspection strategy

    ## Set the SummaryStatisticsInspectionStrategy
    inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    inspector.execute_inspection(df)  ## Execute the data inspection strategy
