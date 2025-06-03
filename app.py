from flask import Flask, render_template, request
import pickle
import numpy as np

with open(r'C:\Users\Hi\dai_hoc\TriTueNhanTao\Final\Diabetes_model', 'rb') as to_read:
    rf_cv = pickle.load(to_read)

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = int(request.form['high_blood'])
    data2 = int(request.form['cholesterol'])
    data3 = int(request.form['bmi'])
    data4 = int(request.form['heart_disease'])
    data5 = int(request.form['physical_activity'])
    data6 = int(request.form['alcohol'])
    data7 = int(request.form['general_health'])
    data8 = int(request.form['mental_health'])
    data9 = int(request.form['physical_health'])
    data10 = int(request.form['walking_difficulty'])
    data11 = int(request.form['age_group'])
    data12 = int(request.form['education'])
    data13 = int(request.form['income'])
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13]])
    pred = rf_cv.predict(arr)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)

