from abc import ABC, abstractclassmethod
import pandas as pd


class DataInspectionStrategy(ABC):
    @abstractclassmethod
    def inspect (self, df: pd.DatFrame):
        """
        Perform a speicifc type of data inspection

        parameters:
        df (pd.DataFrame): The DataFrame on which the inspection on which the inspection is to be perfoermed

        returns:
        None: This method prints the insepction results directly
        """
        pass

# this statergy insepcts the data type of each column and count
class DataTypesInsepctionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        inspects and prints data types and NOT-NULL counts

        parameters:
        df (pd.DataFrame): The dataFrame to be inspected.

        returns:
        none: prints the data type and non-null counts to the
        """
    print("\nData Types and Non-null Counts:")
    print(df.info())


# for summary statitics inspection
class SummaryStatiticsInspectionStratergy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        prints summary statictics for numercial and cateogrical

        parameters:
        df(pd.DataFrame): The dataframe to be inspected

        returns:
        none: print summary statitics to the console
        """
    print("\n Summary Statitics (Numercial Featuers):")
    print(df.describe())
    print("\nSummary Statitics (Categorical Features):")
    print(df.describe(include=["0"]))


# context class that uses a dataInspectionStrategy

class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        
