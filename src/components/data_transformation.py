import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from src.utils import save_object

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging


import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts",'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()


    def get_data_transformation(self):

        try:
            logging.info("Data Transformation Initiated")

            numerical_columns=['Age', 'CityTier', 'DurationOfPitch', 'NumberOfPersonVisiting',
                  'NumberOfFollowups', 'PreferredPropertyStar', 'NumberOfTrips',
                  'Passport', 'PitchSatisfactionScore', 'OwnCar',
                  'NumberOfChildrenVisiting', 'MonthlyIncome']


            categorical_columns=['TypeofContact','Occupation', 'Gender',
                                  'ProductPitched','MaritalStatus', 'Designation']
            
            logging.info(f"Our Numeric features are {numerical_columns}")
            logging.info(f"Our categorical Features are{categorical_columns}")

    
            
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )

            preprocessor=ColumnTransformer([
                   ("num_pipeline",num_pipeline,numerical_columns),
                   ("cat_pipeline",cat_pipeline,categorical_columns)
            ])

            return preprocessor


        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info(f'Train DataFrame Head: \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')

            preprocessing_obj=self.get_data_transformation()

            target_column_name='ProdTaken'
                

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                    "Applying preprocessing object on training data frame and testing data frame"
                  )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing Object")

            save_object(
                    file_path=self.data_transformation_config.preprocessor_obj_file_path,
                    obj=preprocessing_obj
                    )
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,

            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise CustomException(e,sys)