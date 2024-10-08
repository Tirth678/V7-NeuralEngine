import os
import zipfile
from abc import ABC, abstractclassmethod

import pandas as pd

#define an abstract class for data ingestor
class DataIngestor(ABC):
    @abstractclassmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        pass

#implement a concrete class for zip ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: src) -> pd.DataFrame:
        #ensure the file is a .zip
        if not file_path.endswith(".zip"):
            raise ValueError("The povided file is not a .zip file\n")

#extract zip file
with zipfile.ZipFile(file_path, "r") as zip_ref:
    zip_ref.extract("extracted_data")

#find the extracted CSV file
extracted_files = os.listdir("extracted_data")
csv_files = [f for f in extracted_files if f.endswith(" .csv")]

if len(csv_files) == 0:
    raise FileNotFoundError("No CSV found in the extracted data")
if len(csv_files) > 1:
    raise ValueError("Multiple CSV files found, please speicify which one to use")

#read csv into a dataframe
csv_file_path = os.join("extracted_data", csv_files)
df = pd.read_csv(csv_file_path)

# return the bataFrame
# return df

class DataIngestorFactory:
    @staticmethod
    def get_data_DataIngestor(file_extension: str) -> DataIngestor:
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No Ingestor available for file extension {file_extension}")


 # case 01:
if __name__ == "__main__":
    pass

