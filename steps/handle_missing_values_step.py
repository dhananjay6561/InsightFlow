import pandas as pd

from src.handle_missing_values import (
    DropMissingValues,
    FillMissingValues,
    MissingValuesHandler
)

from zenml import step

@step
def handle_missing_values_step( df: pd.DataFrame, strategy: str="mean") -> pd.DataFrame:
    '''Handle Missing Values Step
    
    This step is used to handle missing values in a dataframe.
    
    Args:
        df (pd.DataFrame): The dataframe to handle missing values for.
        strategy (str): The strategy to use to handle missing values. Default is "mean".
    
    Returns:
        pd.DataFrame: The dataframe with missing values handled.
    '''
    if strategy == "drop":
        handler = MissingValuesHandler(DropMissingValues(axis=0))  ##axis=0 means drop rows with missing values axis=1 means drop columns with missing values
    elif strategy in ["mean", "median", "mode","constant"]:
        handler = MissingValuesHandler(FillMissingValues(method=strategy))
    else:   
        raise ValueError("Invalid strategy: {}".format(strategy))
    
    cleaned_df = handler.handle_missing_values(df)
    return cleaned_df
