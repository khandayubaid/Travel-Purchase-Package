import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass


    def predict(self,features):
        try:

            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(model_path)
            preprocessor=load_object(preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        


class CustomData:                       ##this class will be responsible for mapping all inputs given in html page with the backend to particular values
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
            custom_data_input_dict = {
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
            raise CustomException(e, sys)
    

        
