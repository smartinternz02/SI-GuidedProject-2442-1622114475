# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:39:09 2021

@author: Lasya Priya
"""

import joblib 
import pandas as pd
from flask import Flask,request,render_template

app1=Flask(__name__)
model=joblib.load('sales.sav')

@app1.route('/')
def home():
    return render_template('predict.html')
@app1.route('/predict',methods=['POST'])
def y_predict():
    if request.method=='POST':
        ds=request.form["date"]
        a={"ds":[ds]}
        ds=pd.DataFrame(a)
        prediction=model.predict(ds)
        print(prediction)
        output=round(prediction.iloc[0,15])
        print(output)
        return render_template('predict.html',output="The sale value on the selected date is {} thousands".format(output))
    return render_template("predict.html")

if __name__ == "__main__" :
    app1.run(debug=True)


        
        