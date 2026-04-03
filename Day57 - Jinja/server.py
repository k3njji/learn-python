from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)
@app.route("/")
def home():
    random_number = random.randint(1, 100)
    year = datetime.datetime.now().year

    return render_template("index.html", num = random_number, year = year)

@app.route("/guess/age/<name>")
def guess_age(name):
    res = requests.get(f"https://api.agify.io?name={name}")
    age = res.json()["age"]
    # names = name
    return render_template("guess_age.html", name=name, age=age, names=name)

@app.route("/guess/gender/<name>")
def guess_gender(name):
    res = requests.get(f"https://api.genderize.io?name={name}")
    # age = res.json()["age"]
    # names = name
    # print(res.json())
    return render_template("guess_gender.html", names=name, gender=res.json()["gender"])

@app.route("/blog")
def blog():
    req = requests.get("https://www.npoint.io/docs/c790b4d5cab58020d391")
    posts = req.json()
    print(posts)
    return render_template("blog.html")

if __name__ == "__main__":
    app.run(debug=True)