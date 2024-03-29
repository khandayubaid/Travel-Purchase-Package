import os
import sys
import numpy as np
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

from src.utils import save_object,evaluate_models


#Model Imports
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import f1_score,classification_report,accuracy_score
import pickle
import warnings

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()



    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info(f"Split Training and Test Input Data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                    "Logistic_regression":LogisticRegression(),
                    "Random_Forest_Classifier":RandomForestClassifier(),
                    "Decision_Tree_Classifier":DecisionTreeClassifier(),
                    "XGBoost_Classifier": XGBClassifier(),
                    "K_Neighbour_Classifier":KNeighborsClassifier(),
                    "Naive_Bayes_Classifier":GaussianNB(),
                    "SupportVectorClassifier":SVC(),
                    "AdaBoost":AdaBoostClassifier()
          }

            params={
                    "Random_Forest_Classifier":{
                    'criterion':['gini', 'log_loss', 'entropy'],
                    'max_features':['sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256] },

                    "Decision_Tree_Classifier":{
                    'criterion':['entropy', 'gini', 'log_loss'],
                                 'splitter':['best','random'],
                                'max_features':['sqrt','log2']},
                        
                        "K_Neighbour_Classifier":{'n_neighbors' : [5,7,9,11,13,15],
                            'weights' : ['uniform','distance'],
                            'metric' : ['minkowski','euclidean','manhattan']},
                        
                        "SupportVectorClassifier":{
                            'C': [0.1, 1, 10, 100, 1000], 
                            'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
                            'kernel': ['rbf']},
                        
                         "AdaBoost":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]},

                    "XGBoost_Classifier":{
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 1.0],
                    'max_depth': [3, 4, 5],
                    'subsample': [0.8, 0.9, 1.0],
                    'colsample_bytree': [0.8, 0.9, 1.0],
                    'gamma': [0, 1, 2],
                    'min_child_weight': [1, 2, 3]},
                        
                     "Logistic_regression":{},
                        
                        "Naive_Bayes_Classifier":{}
            }
            

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models,param=params
            )



            ## To get best model score
            best_model_score=max(sorted(model_report.values()))


            ## Best Model Name

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
           ]
            
            

            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No Best Model")
            
            print(f'Best Model Found , Model Name : {best_model} , accuracy : {best_model_score}')
            print('\n====================================================================================\n')


            logging.info(f"Best found model on both training & testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            accu_score=accuracy_score(y_test,predicted)

            logging.info(f"Finding best Model")

            return accu_score




        except Exception as e:
            raise CustomException(e,sys)