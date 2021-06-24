from flask import Flask,request,render_template
import numpy as np
import pickle
model=pickle.load(open("classifier.pkl","rb"))

app=Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/predict",methods=['POST'])
def predict():
    if request.method=="POST":
        num_preg=int(request.form["num_preg"])
        glucose_conc=int(request.form["glucose_conc"])
        diastolic_bp=int(request.form["diastolic_bp"])
        insulin=int(request.form['insulin'])
        bmi=float(request.form['bmi'])
        diab_pred=float(request.form["diab_pred"])
        age=int(request.form['age'])
        skin=float(request.form['skin'])
        prediction=model.predict([[num_preg,glucose_conc,diastolic_bp,insulin,bmi,diab_pred,age,skin]])
        if(prediction[0]==1):
            return render_template("index.html",prediction_text="He/She is diabetic")
        else:
            return render_template("index.html",prediction_text="He/She is not diabetic")
    else:
        return render_template("index.html")


if(__name__=="__main__"):
    app.run(debug=True)
