import logging  ## for logging information
import pandas as pd  ## for data manipulation
from abc import ABC, abstractmethod

## Setting up the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  ## asctime is the time of the event, name is the name of the logger, levelname is the level of the message, message is the message

## Abstract class for handling missing values
class MissingValuesHandler(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Handle Missing Values
        
        This method is used to handle missing values in a dataframe.
        
        Args:
            df (pd.DataFrame): The dataframe to handle missing values for.
            
        Returns:
            pd.DataFrame: The dataframe with missing values handled.
        '''
        pass

## Concrete class for handling missing values
class DropMissingValues(MissingValuesHandler):
    def __init__(self, axis=0):  ## axis=0 means drop rows, axis=1 means drop columns
        '''Drop Missing Values

        This class is used to drop missing values from a dataframe.

        Args:
            axis (int): The axis to drop missing values along. Default is 0.
        '''
        self.axis = axis

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Handle Missing Values

        This method is used to handle missing values in a dataframe.

        Args:
            df (pd.DataFrame): The dataframe to handle missing values for.

        Returns:
            pd.DataFrame: The dataframe with missing values handled.
        '''
        logging.info(f"Dropping missing values with axis: {self.axis}")
        return df.dropna(axis=self.axis)

## Concrete class for filling missing values
class FillMissingValues(MissingValuesHandler):
    def __init__(self, method="mean", fill_value=None):  ## method is the method to use to fill missing values, fill_value is the value to fill missing values with
        '''Fill Missing Values

        This class is used to fill missing values in a dataframe.

        Args:
            method (str): The method to use to fill missing values. Default is "mean".
            fill_value (int): The value to fill missing values with. Default is None.
        '''
        self.method = method
        self.fill_value = fill_value

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Fill Missing Values

        This method is used to fill missing values in a dataframe.

        Args:
            df (pd.DataFrame): The dataframe to fill missing values for.

        Returns:
            pd.DataFrame: The dataframe with missing values filled.
        '''
        logging.info(f"Filling missing values with method: {self.method} and fill_value: {self.fill_value}")

        df_cleaned = df.copy()
        if self.method == "mean":
            numeric_columns = df_cleaned.select_dtypes(include=['int64', 'float64']).columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df_cleaned[numeric_columns].mean())
        elif self.method == "median":
            numeric_columns = df_cleaned.select_dtypes(include=['int64', 'float64']).columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df_cleaned[numeric_columns].median())
        elif self.method == "mode":
            for column in df_cleaned.columns:
                df_cleaned[column].fillna(df_cleaned[column].mode().iloc[0], inplace=True)
        elif self.method == "constant":
            df_cleaned = df_cleaned.fillna(self.fill_value)
        else:
            logging.warning(f"Unknown method '{self.method}'. No missing values handled.")

        logging.info("Missing values filled.")
        return df_cleaned

## Context class for handling missing values
class MissingValueHandler:
    def __init__(self, strategy: MissingValuesHandler):
        '''Initialize Missing Value Handler

        This class is used to initialize the missing value handler with a specific missing value handling strategy.

        Args:
            strategy (MissingValuesHandler): The strategy to be used for handling missing values.
        '''
        self.strategy = strategy

    def set_strategy(self, strategy: MissingValuesHandler):
        '''Set Strategy

        This method is used to set a new strategy for the missing value handler.

        Args:
            strategy (MissingValuesHandler): The new strategy to be used for handling missing values.
        '''
        logging.info("Switching to new strategy")
        self.strategy = strategy

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Handle Missing Values

        This method is used to handle missing values in a dataframe.

        Args:
            df (pd.DataFrame): The dataframe to handle missing values for.

        Returns:
            pd.DataFrame: The dataframe with missing values handled.
        '''
        logging.info(f"Handling missing values using strategy: {self.strategy}")
        return self.strategy.handle(df)