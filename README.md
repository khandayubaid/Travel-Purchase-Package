# 🧳Travel Package Purchase Prediction 
An End to End project using CICD pipeline which will help us to predict whether a new Customer will Purchase the Package or Not.

## General Info
The "Travel Purchase Package Prediction" initiative is centered around addressing a binary classification challenge at the intersection of travel and data science. Tailored specifically for predicting travel package purchases, the system leverages rich historical data encompassing customer interactions and purchasing behaviors. At its core, the project aims to categorize customers into two distinct segments: those with a high likelihood of purchasing the travel package and those unlikely to do so.

By mining insights from past purchase records and diverse customer attributes, the system employs a diverse array of machine learning algorithms. These algorithms meticulously analyze intricate patterns and relationships within the dataset, culminating in the development of a robust binary classification model. The model's effectiveness is paramount, as it accurately classifies customers, thereby furnishing businesses with invaluable insights to fine-tune marketing strategies and optimize sales efforts.

This project fundamentally transforms customer engagement and revenue generation within the travel industry by empowering businesses to proactively address the nuanced needs and preferences of their customer base. The end result is a sophisticated binary classification model that enhances prediction accuracy, serving as a strategic asset for businesses seeking to elevate their marketing initiatives and maximize sales amidst the dynamic landscape of the travel sector.

***
## ⏳Data Source
[Travel Package Data](https://question.transtutors.com/6129343_1_tourism-data.xlsx)
***

## Problem Statement
Tourism is one of the most rapidly growing global industries and tourism forecasting is
becoming an increasingly important activity in planning and managing the industry.
Because of high fluctuations of tourism demand, accurate predictions of purchase of
travel packages are of high importance for tourism organizations.
The goal is to predict whether the customer will purchase the travel or not.

## 📷 Demo Photos

![Screenshot (146)](https://github.com/khandayubaid/Travel-Purchase-Package/assets/143508601/67748da1-fca4-4162-be1e-e431b642fe44)
This interface functions as the portal to our project. Ensure accurate input across all fields, and the system will generate predictions tailored to your specifications. Specifically, it will predict whether the customer is likely to purchase the package or not based on the information you provide. Your detailed inputs enable the system to deliver precise and personalized forecasts, aiding in strategic decision-making for travel package offerings.

## 🖥️Library Used
 There will be file named requirement.txt which will contain all these libraries used in project.
 ```
pandas
numpy
seaborn
matplotlib
scikit-learn
SVC
flask
dill
```


## ⚙️Project Structure
We have used the following structure to develop this End-To-End Project:
* ```setup.py```It is a script in Python that is used for packaging and distributing Python projects.
* ```requirements.txt it will have all the packages that i really need to install while im implementing the project.
* ```logger.py``` It helps in capturing detailed information about events occurring at specific times or within specific files.
* ```exception.py``` takes charge of handling custom exceptions that arise when an error occurs in any file. It provides detailed information including the file name, line number, and the nature of the error.
* ```.gitignore``` prevents the inclusion of specific files that we don't want to push to GitHub.
* ```readme.md``` contain general informtion about the project steps and requiremnts for further explaination.
datacontain the dataset.
* ```src``` contain many subfolder. we need to give a ```__init__.py``` file in each directory so that we can use each file as a package.
* ```src/data_ingestion.py``` It is a part of a module when we are developing a project. it will have all the code that will be related to reading the data.
* ```src/data_transformation.py```After ingesting the data i may do transformation of data or validation of data. For this we will have this file. Over here will be probably writing the code, how to change the categorical variable to numerical variable, how to handle the one hot encoding or label encoding etc.
* ```src/Model_trainer.py```handles both model training and hyperparameter tuning. It returns a model pickle file that is trained on the provided data and can be utilized for subsequent predictions.
* ```src/Prediction_Pipeline.py``` is responsible for the Creating the Pipeline using the app.py
* ```utils.py``` is used for creating and storing the common function which are used through out the Project.
* ```app.py``` serves as the web application file that interacts with users.
