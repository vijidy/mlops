# read the data from different storage

import os
import sys
from src.exception import customException
from src.logger import logging
import pandas as pd
from sklearn.model_selection  import train_test_split
from dataclasses import dataclass

# inputs are given to this class

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv") #output of data ingestion are stored in this folder(trained data)
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class DataIngestion:
   
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self): #read data from the db or source
        logging.info("Enter the data ingestion method or componet")
        try :
            df=pd.read_csv('D:/mlprojects/notebook/data/stud.csv')
            logging.info("Exported or Read the Dataset as Dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test Split Initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")

            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path,self.ingestion_config.raw_data_path)

        except Exception as e:
           
            raise customException(e,sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

