from abc import ABC, abstractmethod

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Abstract class for missing value analysis
class UnivariateAnalysisStrategy(ABC):
    def analyze(self, df: pd.DataFrame, feature: str):
        """Perform the complete univariate analysis.
        Parameters:
        df (pd.DataFrame): The dataframe to be analyzed.
        feature (str): The feature to be analyzed.

        Returns:
        None - This method visualises the distribution of the feature and identifies outliers.

        """
        pass

    ##concrete implementation for univariate analysis

class SimpleUnivariateAnalysisStrategy(UnivariateAnalysisStrategy):

    ##This will analyze numerical features by plotting a histogram and identifying outliers
    def analyze(self, df: pd.DataFrame, feature: str):
        """Perform univariate analysis on the feature.
        Parameters:
        df (pd.DataFrame): The dataframe to be analyzed.
        feature (str): The feature to be analyzed.

        Returns:
        None - Will display a histogram of the feature and print the number of unique values, missing values, and value counts.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True, bins=30)  ##kde is kernel density estimation and bins is the number of bins in the histogram
        ##kde adds a line to the histogram that represents the distribution of the data and makes histogram more smooth
        ##bins is the number of bins/intervals in the histogram

        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()

##concrete strategy for univariate analysis of categorical features

class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):

    ##This will analyze the categorical features by plotting a bar chart
    def analyze(self, df: pd.DataFrame, feature: str):
        """Perform univariate analysis on the feature.
        Parameters:
        df (pd.DataFrame): The dataframe to be analyzed.
        feature (str): The feature to be analyzed.

        Returns:
        None - Will display a barchart of the feature and print the number of unique values, missing values, and value counts.
        """
        plt.figure(figsize=(10, 6))
        sns.countplot(x=feature, data=df, palette='muted', hue=feature)  ##palette is the color palette to be used in the bar chart 
        ##muted here means the colors will be less saturated
        plt.title(f"Count of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45) ##rotate the x-axis labels by 45 degrees
        plt.show()
            
##Context class for univariate analysis

##This class will use the strategy to perform univariate analysis

class UnivariateAnalyzer:
    def __init__(self, strategy: UnivariateAnalysisStrategy):
        """Initialize the UnivariateAnalyzer with a specific strategy.
        Parameters:
        strategy (UnivariateAnalysisStrategy): The strategy to be used for univariate analysis.

        Returns:
        None - This method initializes the UnivariateAnalyzer with the specified strategy.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: UnivariateAnalysisStrategy):
        """Set a new strategy for univariate analysis.
        Parameters:
        strategy (UnivariateAnalysisStrategy): The new strategy to be used for univariate analysis.
        Returns:
        None - This method sets a new strategy for the UnivariateAnalyzer.
        """
        self._strategy = strategy

    def analyze(self, df: pd.DataFrame, feature: str):
        """Perform univariate analysis on the feature using the current strategy.
        Parameters:
        df (pd.DataFrame): The dataframe to be analyzed.
        feature (str): The feature to be analyzed.
        Returns:
        None - This method performs univariate analysis on the feature using the current strategy.
        """
        self._strategy.analyze(df, feature)

##Example usage of the class
if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv("../../extracted_data/AmesHousing.csv")

    # Perform univariate analysis on the 'SalePrice' feature
    univariate_analyzer = UnivariateAnalyzer(SimpleUnivariateAnalysisStrategy())  ##Create an instance of the UnivariateAnalyzer with the SimpleUnivariateAnalysisStrategy
    univariate_analyzer.analyze(df, 'SalePrice')  ##Analyze the 'SalePrice' feature
    univariate_analyzer.set_strategy(CategoricalUnivariateAnalysis())  ##Set the strategy to CategoricalUnivariateAnalysis
    univariate_analyzer.analyze(df, 'Neighborhood')  ##Analyze the 'Neighborhood' feature

    pass ##This is the end of the code snippet