from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/submit', methods=["POST"])
def submit():
    form = request.form
    print(form)
    if form:
        my_email = os.getenv("EMAIL_ADDRESS")
        password = os.getenv("EMAIL_PASSWORD")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=form['email'],
                msg=f"Subject:New Contact Form Submission\n\nName: {form['name']}\nEmail: {form['email']}\nPhone: {form['phone']}\nMessage: {form['message']}"
            )
        
    return "Form submitted successfully!"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
