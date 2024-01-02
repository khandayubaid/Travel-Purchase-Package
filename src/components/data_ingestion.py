import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# where to save raw data ,train data,test data so ncreate input we create this class dataingestion class

@dataclass            #decorator
class DataIngestConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestConfig()         #the above 3 paths wiil get saved into this class variable

    def initiate_data_ingestion(self):              ## to read the data from the database like mongodb,sql etc
        logging.info("Entered the Data Ingestion Method")
        try:
            df=pd.read_csv(r"C:\Users\ubaid\Desktop\Ineuron_Intership\notebooks\Data\tour_package.csv")               # here we will write data (Can be locally or from any other database)
            logging.info("Read the Dataset as DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test Split Initiated")
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)


            logging.info("Ingestion Is Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,

            )


        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)