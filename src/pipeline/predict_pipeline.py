import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
              model_path=os.path.join("artifacts",'model.pkl')
              preprocessor_path=os.path.join('artifacts',"preprocessor.pkl")

              preprocessor=load_object(file_path=preprocessor_path)
              model=load_object(file_path=model_path)

              print("After Loading")
              data_scaled=preprocessor.transform(features)
              preds=model.predict(data_scaled)
              return preds
        
        except Exception as e:
            raise CustomException(e,sys)


        

class CustomData:
         def __init__(self,age,typeofcontact,citytier,durationofpitch,occupation,gender,
                      numberofpersonvisiting,numberoffollowups,productpitched,prefferedpropertystar,
                      maritalstatus,numberoftrips,passport, pitchsatisfactionscore,owncar,
                      numberofchildrenvisiting,designation,monthlyincome):
        
                    self.age=age
                    self.typeofcontact=typeofcontact
                    self.citytier=citytier
                    self.durationofpitch=durationofpitch
                    self.occupation=occupation
                    self.gender=gender
                    self.numberofpersonvisiting=numberofpersonvisiting
                    self.numberoffollowups=numberoffollowups
                    self.productpitched=productpitched
                    self.prefferedpropertystar=prefferedpropertystar
                    self.maritalstatus=maritalstatus
                    self.numberoftrips=numberoftrips
                    self.passport=passport
                    self.pitchsatisfactionscore=pitchsatisfactionscore
                    self.owncar=owncar
                    self.numberofchildrenvisiting=numberofchildrenvisiting
                    self.designation=designation
                    self.monthlyincome=monthlyincome

         def get_data_as_data_frame(self):
            try:
                custom_data_input_dict={
                    "Age":[self.age],
                    "TypeofContact":[self.typeofcontact],
                    "CityTier":[self.citytier],
                    "DurationOfPitch":[self.durationofpitch],
                    "Occupation":[self.occupation],
                    "Gender":[self.gender],
                    "NumberOfPersonVisiting":[self.numberofpersonvisiting],
                    "NumberOfFollowups":[self.numberoffollowups],
                    "ProductPitched":[self.productpitched],
                    "PreferredPropertyStar":[self.prefferedpropertystar],
                    "MaritalStatus":[self.maritalstatus],
                    "NumberOfTrips":[self.numberoftrips],
                    "Passport":[self.passport],
                    "PitchSatisfactionScore":[self.pitchsatisfactionscore],
                    "OwnCar":[self.owncar],
                    "NumberOfChildrenVisiting":[self.numberofchildrenvisiting],
                    "Designation":[self.designation],
                    "MonthlyIncome":[self.monthlyincome]
                    }
                
                return pd.DataFrame(custom_data_input_dict)
            except Exception as e:
                raise CustomException(e,sys)
    

        
