from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

##Route for home Page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
             age=request.form["age"],
        prefferedpropertystar=request.form["prefferedpropertystar"],
        typeofcontact=request.form["typeofcontact"],
        maritalstatus=request.form["maritalstatus"],
        citytier=request.form["citytier"],
        numberoftrips=request.form["numberoftrips"],
        durationofpitch=request.form["durationofpitch"],
        passport=request.form["passport"],
        pitchsatisfactionscore=request.form["pitchsatisfactionscore"],
        occupation=request.form["occupation"],
        gender=request.form["gender"],
        owncar=request.form["owncar"],
        numberofpersonvisiting=request.form["numberofpersonvisiting"],
        numberofchildrenvisiting=request.form["numberofchildrenvisiting"],
        numberoffollowups=request.form["numberoffollowups"],
        designation=request.form["designation"],
        productpitched=request.form["productpitched"],
        monthlyincome=request.form["monthlyincome"]
        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        output=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
