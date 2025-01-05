from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Abstract class for missing value analysis
class MissingValuesAnalysis(ABC):
    def analyze(self, df: pd.DataFrame):
        """Perform the complete missing value analysis."""
        self.identify_missing_values(df)
        self.visualise_missing_values(df)

    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame):
        """Identify missing values in the dataframe."""
        pass

    @abstractmethod
    def visualise_missing_values(self, df: pd.DataFrame):
        """Visualize missing values in the dataframe."""
        pass

# Concrete implementation for missing value analysis
class SimpleMissingValuesAnalysis(MissingValuesAnalysis):
    def identify_missing_values(self, df: pd.DataFrame):
        """Identify missing values in the dataframe."""
        missing_values = df.isnull().sum()
        print("Missing Value count by Column:")
        print(missing_values[missing_values > 0])

    def visualise_missing_values(self, df: pd.DataFrame):
        """Visualize missing values in the dataframe."""
        print("\nVisualizing Missing Values")
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')  ##viridis is a color map for missing values(purple -> no missing values, yellow -> missing values)
        plt.title("Missing Values in the Data")
        plt.show()

# Example usage of the class
if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv("../../extracted_data/AmesHousing.csv")

    # Perform missing value analysis
    missing_values_analyser = SimpleMissingValuesAnalysis()
    missing_values_analyser.analyze(df)
