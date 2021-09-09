from flask import Flask, request, render_template
from flask_cors import cross_origin
from utils import Model

app = Flask(__name__)


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        model = Model(request)

        prediction = model.predict()

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(prediction))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
