from flask import Flask, request, render_template
from flask_cors import cross_origin
from clean_data import data_cleaner
from predict import predict_price

app = Flask(__name__)


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        cleaned_data = data_cleaner(request)

        prediction = predict_price(cleaned_data)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(prediction))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
