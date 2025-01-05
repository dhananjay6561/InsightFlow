from abc import ABC, abstractmethod

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Abstract class for bi-variate analysis
class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """Perform the complete bi-variate analysis.
        Parameters:
        df (pd.DataFrame): The dataframe to be analyzed.
        feature1 (str): The first feature to be analyzed.
        feature2 (str): The second feature to be analyzed.

        Returns:
        None - This method visualises the relationship between the two features.
        """
        pass


# Concrete implementation for bi-variate analysis

##This will analyze the relationship between two numerical features by plotting a scatter plot

class NumericalBivariateAnalysisStrategy(BivariateAnalysisStrategy):
    
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """Perform bi-variate analysis on the two numerical features.
        Parameters:
        df (pd.DataFrame): The dataframe to be analyzed.
        feature1 (str): The first numerical feature to be analyzed.
        feature2 (str): The second numerical feature to be analyzed.

        Returns:
        None - Will display a scatter plot of the two numerical features.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=feature1, y=feature2, data=df)
        plt.title(f"Relationship between {feature1} and {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

##This will analyze the relationship between a numerical and a categorical feature by plotting a boxplot

class NumericalCategoricalBivariateAnalysisStrategy(BivariateAnalysisStrategy):
    
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """Perform bi-variate analysis on the numerical and categorical features.
        Parameters:
        df (pd.DataFrame): The dataframe to be analyzed.
        feature1 (str): The numerical feature to be analyzed.
        feature2 (str): The categorical feature to be analyzed.

        Returns:
        None - Will display a boxplot of the numerical feature grouped by the categories in the categorical feature.
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=feature2, y=feature1, data=df)
        plt.title(f"Relationship between {feature1} and {feature2}")
        plt.xlabel(feature2)
        plt.ylabel(feature1)
        plt.show()

##This will analyze the relationship between two categorical features by plotting a heatmap

class CategoricalBivariateAnalysisStrategy(BivariateAnalysisStrategy):
    
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """Perform bi-variate analysis on the two categorical features.
        Parameters:
        df (pd.DataFrame): The dataframe to be analyzed.
        feature1 (str): The first categorical feature to be analyzed.
        feature2 (str): The second categorical feature to be analyzed.

        Returns:
        None - Will display a heatmap of the two categorical features.
        """
        plt.figure(figsize=(10, 6))
        crosstab = pd.crosstab(df[feature1], df[feature2])
        sns.heatmap(crosstab, annot=True, cmap='viridis')
        plt.title(f"Relationship between {feature1} and {feature2}")
        plt.xlabel(feature2)
        plt.ylabel(feature1)
        plt.show()

##Context class for bi-variate analysis

##This class will use the strategy to perform bi-variate analysis

class BivariateAnalyzer:
    def __init__(self, strategy: BivariateAnalysisStrategy):
        """Initialize the BivariateAnalyzer with a specific strategy.
        Parameters:
        strategy (BivariateAnalysisStrategy): The strategy to be used for bi-variate analysis.

        Returns:
        None - This method initializes the BivariateAnalyzer with the specified strategy.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: BivariateAnalysisStrategy):
        """Set a new strategy for bi-variate analysis.
        Parameters:
        strategy (BivariateAnalysisStrategy): The new strategy to be used for bi-variate analysis.
        Returns:
        None - This method sets a new strategy for the BivariateAnalyzer.
        """
        self._strategy = strategy

    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """Perform bi-variate analysis on the features using the current strategy.
        Parameters:
        df (pd.DataFrame): The dataframe to be analyzed.
        feature1 (str): The first feature to be analyzed.
        feature2 (str): The second feature to be analyzed.
        Returns:
        None - This method performs bi-variate analysis on the features using the current strategy.
        """
        self._strategy.analyze(df, feature1, feature2)

# Example usage of the class
if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv("../../extracted_data/AmesHousing.csv")

    # Perform bi-variate analysis
    numerical_numerical_analyser = NumericalBivariateAnalysisStrategy()
    numerical_numerical_analyser.analyze(df, 'Gr Liv Area', 'SalePrice')

    numerical_categorical_analyser = NumericalCategoricalBivariateAnalysisStrategy()
    numerical_categorical_analyser.analyze(df, 'SalePrice', 'Overall Qual')

    categorical_categorical_analyser = CategoricalBivariateAnalysisStrategy()
    categorical_categorical_analyser.analyze(df, 'Neighborhood', 'Sale Condition')

    pass 