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
