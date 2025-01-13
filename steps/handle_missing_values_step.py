import pandas as pd
from zenml import step
from src.handle_missing_values import MissingValueHandler, DropMissingValues, FillMissingValues

@step
def handle_missing_values_step(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    '''Handle Missing Values Step
    
    This step is used to handle missing values in a dataframe.
    
    Args:
        df (pd.DataFrame): The dataframe to handle missing values for.
        strategy (str): The strategy to use for handling missing values. Default is "mean".
        
    Returns:
        pd.DataFrame: The dataframe with missing values handled.
    '''
    
    if strategy == "drop":
        handler = MissingValueHandler(DropMissingValues(axis=0))  ## axis=0 means drop rows
    elif strategy in ["mean", "median", "mode", "constant"]:
        handler = MissingValueHandler(FillMissingValues(method=strategy))
    else:
        raise ValueError(f"Invalid strategy: {strategy}")

    df_cleaned = handler.handle_missing_values(df)
    return df_cleaned