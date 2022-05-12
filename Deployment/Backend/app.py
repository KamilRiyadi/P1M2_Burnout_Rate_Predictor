from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

columns = ['Gender', 'Company_Type', 'WFH_Setup_Available', 'Designation', 'Resource_Allocation', 'Mental_Fatigue_Score']

@app.route("/")
def home():
    return "<h1>Welcome!</h1>"

@app.route("/predict", methods=['GET','POST'])
def model_prediction():
    if request.method == "POST":
        content = request.json
        try:
            data= [content['Gender'],
                   content['Company_Type'],
                   content['WFH_Setup_Available'],
                   content['Designation'],
                   content['Resource_Allocation'],
                   content['Mental_Fatigue_Score']]
            data = pd.DataFrame([data], columns=columns)
            pred = model.predict(data)
            response = {"code": 200, "status":"OK", 
                        "result":{"prediction":round(pred[0], 2)}}
            return jsonify(response)

        except Exception as e:

            response = {"code":500, "status":"ERROR", 
                        "result":{"error_msg":str(e)}}
            return jsonify(response)
    return "<p>Silahkan gunakan method POST untuk mengakses hasil prediksi dari model</p>"
