from flask import Flask, request, render_template
import numpy as np
import pickle
app = Flask(__name__)
model = pickle.load(open("student_calc.pkl","rb"))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods = ['post','get'])
def predict():
    print(request.form)
    int_feature = request.form["study_hours"]
    int_feature = int(int_feature)
    Prediction_arr = [np.array(int_feature)]
    print(int_feature)
    print(Prediction_arr)
    Prediction = model.predict([Prediction_arr])
    output = round(Prediction[0],2)
    if int_feature < 0 or int_feature > 24:
        return render_template('index.html', prediction_text = 'Are you a human!!!? Please enter a valid study hours between 1 to 24')
    else:
        return render_template('index.html', prediction_text = 'You will get [{}%] marks, when you do study [{}] hours per day'.format(output,(Prediction_arr[0])))


if __name__ == "__main__":
    app.run()