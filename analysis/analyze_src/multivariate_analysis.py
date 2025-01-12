from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Abstract class for multivariate analysis
class MultivariateAnalysis(ABC):
    def analyze(self, df: pd.DataFrame):
        """Perform the complete multivariate analysis.
        
        Parameters:
        df (pd.DataFrame): The dataframe to analyze.

        Returns:
        None: The function does not return anything.
        """
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

    @abstractmethod
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        """Generate a correlation heatmap for the dataframe.
        
        Parameters:
        df (pd.DataFrame): The dataframe to analyze.
        
        Returns:
        None: The function does not return anything. This function should display the heatmap.
        """
        pass
    
    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        """Generate a pairplot for the dataframe.
        
        Parameters:
        df (pd.DataFrame): The dataframe to analyze.
        
        Returns:
        None: The function does not return anything. This function should display the pairplot.
        """
        pass    


# Concrete class for multivariate analysis
class SimpleMultiVariateAnalysis(MultivariateAnalysis):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        '''Generate a correlation heatmap for the dataframe.
        
        Parameters:
        df (pd.DataFrame): The dataframe to analyze.
        
        Returns:
        None: The function does not return anything. Displays correlation between numerical features.
        '''
        plt.figure(figsize=(10, 8))  
        sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')  # fmt=".2f" to display 2 decimal places, cmap='coolwarm' for colors, annot=True to display values
        plt.title('Correlation Heatmap')
        plt.show()

    def generate_pairplot(self, df: pd.DataFrame):
        '''Generate a pairplot for the dataframe.
        
        Parameters:
        df (pd.DataFrame): The dataframe to analyze.
        
        Returns:
        None: The function does not return anything. Displays pairplot for numerical features.
        '''
        sns.pairplot(df)
        plt.suptitle('Pairplot', y=1.02)  # y=1.02 to adjust the title position, suptitle sets the title
        plt.show()


# Example usage
if __name__ == '__main__':
    df = pd.read_csv('../../extracted_data/AmesHousing.csv')  # Read the dataset from the specified location
    
    # Create an instance of the concrete class
    MultivariateAnalysis = SimpleMultiVariateAnalysis()  
    
    # Select specific features for analysis
    selected_features = ['Lot Area', 'Gr Liv Area', 'Total Bsmt SF', 'Garage Area', 'SalePrice']  
    
    # Perform the analysis on the selected features
    MultivariateAnalysis.analyze(df[selected_features])  
