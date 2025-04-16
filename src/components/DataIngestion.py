import os 
import sys
from src.exception import CustomException
from src.logger import logging 
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass 

@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join('artifacts',"data.csv")
    

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self,Data_path):
        logging.info('Method Data Ingestion')
        try:
            self.input_path=Data_path or "E:\\Software-log-Monitoring-system-using-Hybrid-Classification-Model\\notebook\\synthetic_logs.csv"
            df=pd.read_csv(self.input_path)
            logging.info('Read the dataset as a dataFrame')
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True) #To make artifacts folder
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info(f"Saving raw data to: {self.ingestion_config.raw_data_path}")
            
            return self.ingestion_config.raw_data_path
        except Exception as e:
            raise CustomException(e,sys)



"""
What is dataclass?
dataclass is a decorator that is used to initalize all the variable inside the class that means instead of writing a __init__(constructor)
it will do the same operation it will initialize all the variables that we defined inside the class 

Why we need a seperate class DataIngestionConfig?

Because we can reuse the code if we want to use it in some other module

"""

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion('E:\\Software-log-Monitoring-system-using-Hybrid-Classification-Model\\notebook\\synthetic_logs.csv')
