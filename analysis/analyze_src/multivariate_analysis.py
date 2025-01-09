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
 ##Concrete class for multivariate analysis

class SimpleMultiVariateAnalysis(MultivariateAnalysis):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        '''Generate a correlation heatmap for the dataframe.
        
        Parameters:
        df (pd.DataFrame): The dataframe to analyze.
        
        Returns:
        None: The function does not return anything. Displays correlation between numerical features.
        
        '''
        plt.figure(figsize=(10, 8))  
        sns.heatmap(df.corr(), annot=True, fmt="0.2f", cmap='coolwarm')  ##fmt="0.2f" to display 2 decimal places and cmap='coolwarm' for color, annot = True to display values
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
        plt.suptitle('Pairplot',y=1.02)  ##y=1.02 to adjust the title position and suptitle to set the title
        plt.show()

        ##Example usage

        if __name__ == '__main__':
            df = pd.read_csv('../../extracted_data/AmesHousing.csv')
            MultivariateAnalysis = SimpleMultiVariateAnalysis()##create an instance of the class
            selected_features = ['Lot Area', 'Gr Liv Area', 'Total Bsmt SF', 'Garage Area', 'SalePrice'] ##selected features for analysis
            MultivariateAnalysis.analyze(df[selected_features]) ##analyze the selected features
            pass