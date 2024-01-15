from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predictdata", methods=['GET','POST'])
def predict_datapoint():
    if request.method=="GET":
        return render_template('home.html')
    else:
        data = CustomData(
            age=request.form.get("age"),
            prefferedpropertystar=request.form.get("prefferedpropertystar"),
            typeofcontact=request.form.get("typeofcontact"),
            maritalstatus=request.form.get("maritalstatus"),
            citytier=request.form.get("citytier"),
            numberoftrips=request.form.get("numberoftrips"),
            durationofpitch=request.form.get("durationofpitch"),
            passport=request.form.get("passport"),
            pitchsatisfactionscore=request.form.get("pitchsatisfactionscore"),
            occupation=request.form.get("occupation"),
            gender=request.form.get("gender"),
            owncar=request.form.get("owncar"),
            numberofpersonvisiting=request.form.get("numberofpersonvisiting"),
            numberofchildrenvisiting=request.form.get("numberofchildrenvisiting"),
            numberoffollowups=request.form.get("numberoffollowups"),
            designation=request.form.get("designation"),
            productpitched=request.form.get("productpitched"),
            monthlyincome=request.form.get("monthlyincome")
            )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        if results[0]==1:
            res='Take'
            return render_template('home.html',results=res)
        else:
            res='Not Take'
            return render_template('home.html',results=res)
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)