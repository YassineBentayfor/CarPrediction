import joblib

# Save the trained model
joblib.dump(reg_model, 'my_regression_model.joblib')


import os
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
joblib_file = os.path.join(os.getcwd(), 'my_regression_model.joblib')
model = joblib.load(joblib_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    wheelbase = float(request.form["wheelbase"])
    carlength = float(request.form["carlength"])
    curbweight = float(request.form["curbweight"])
    boreratio = float(request.form["boreratio"])
    enginesize = float(request.form["enginesize"])
    horsepower = float(request.form["horsepower"])

    features = [[wheelbase, carlength, curbweight, boreratio, enginesize, horsepower]]
    price = model.predict(features)

    return render_template("index.html", prediction_text="The predicted car price is: $%.2f" % price)

if __name__ == "__main__":
    app.run(debug=True)
    
