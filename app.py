# from urllib import request
from flask import Flask, render_template, request
from jinja2 import Environment, PackageLoader, select_autoescape
from flask_pymongo import PyMongo
app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/VAERS_Data"
mongo = PyMongo(app)


@app.route("/")
def index():
    data = mongo.db.Daily_ADRS_count.find().sort("date")
    data1 = mongo.db.gender_distribution_data.find()
    data2 = mongo.db.adrs_distribution.find()
    data3 = mongo.db.symptoms_data.find().sort("date")
    count = 0
    symptoms_label = []
    symptoms_percentage = []
    for x in data3:
        if count == 10:
            break
        count = count + 1
        symptoms_label.append(x["data"])
        z = int(x["percentage"][:2])
        symptoms_percentage.append("width:"+str(z)+"%")
    adrs = []
    count_adrs = []
    gender_label = []
    gender_percentage = []
    date = []
    count = []
    for x in data2:
        print(x)
        adrs.append(x["label"])
        count_adrs.append(x["data"])
    for x in data1:
        gender_label.append(x["Gender"])
        gender_percentage.append(x["Values_in_percentage"])
    for x in data:
        date.append(x["date"])
        count.append(x["count"])
    return render_template("index.html",
                           date=date, count=count, gender_label=gender_label, gender_percentage=gender_percentage, adrs=adrs, count_adrs=count_adrs, symptoms_label=symptoms_label, symptoms_percentage=symptoms_percentage)


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/form")
def form():
    return render_template("ADR_form.html")


@app.route("/submit", methods=["POST"])
def submit():
    age = request.form.get("age")
    gender = request.form.get("gender")
    DOV = request.form.get("dov")
    DOR = request.form.get("dor")
    symptoms = request.form.get("Symptoms")
    medical_history = request.form.get("medical_history")
    curr_ill = request.form.get("curr_ill")
    oth_med = request.form.get("oth_med")
    died = request.form.get("died")
    hospitalized = request.form.get("hospitalized")
    ER = request.form.get("ER")
    vaccine_type = request.form.get("vaccine_type")
    vaccine_name = request.form.get("vaccine_name")
    print("---------- ", age, gender, DOV, DOR, curr_ill, "medical: ",
          medical_history, " ..", vaccine_name, hospitalized, died, " --------------")
    return render_template("submit.html")


if __name__ == '__main__':
    app.run(debug=True)
