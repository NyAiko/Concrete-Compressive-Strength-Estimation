# import pandas as pd
import numpy as np
from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
@app.route('/')

def home():
    return render_template('home.html')
@app.route('/',methods=['GET','POST'])
def predict():
    if request.method =="POST":
        file_name = 'gbr_beton.p'
        with open(file_name,'rb') as pickled:
             data = pickle.load(pickled)
             model= data['model']
             print('model loaded')
        features = [float(x) for x in request.form.values()]
        #features = np.array(features)
        #features = features.reshape(1,-1)
        #print(features)
        WC =features[1]/features[0]
        X = []
        X.append(WC)
        i = 2
        while i<=len(features)-1:
            X.append(features[i])
            i = i+1
        X = np.array(X)
        X = X.reshape(1,-1)   
        Y = model.predict(X)
        Y = round(float(Y))
        pred = str(Y)+' MPa'
        print(model.predict(X))
    return render_template('home.html',prediction=pred)
if __name__=='__main__':
    app.run()