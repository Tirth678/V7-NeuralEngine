from abc import ABC, abstractclassmethod
import matplotlib as plt
import pandas as pd
import seaborn as sns


class MissingValuesAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):

        """
    performs a complete missing values analysis by identify

    parameters:
    df (pd.DatFrame): The dataframe to be analyzed.

    returns:
    none: This method performs the analysis and visualizes

        """
self.identify_missing_values(df)
self.visualize_missing_values(df)


@abstractclassmethod

def visualize_missing_values(self, df: pd.DataFrame):
    pass

class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
    def identify_missing_values(self, df: pd.DataFrame):
        print("\nMissing Values Count by Coulumn:")
        missing_values = df.isnull().sum()
        print(missing_values > 0)

    def visualize_missing_values(self, df: pd.DataFrame):
        print("\nVisualizing Missing Values...")
        plt.figure(figsize=(12,8))
        sns.heatmape(df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap")
        plt.show()


# example usage
if __name__ == "__main__":
    pass
