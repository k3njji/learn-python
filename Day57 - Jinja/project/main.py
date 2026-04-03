from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    req = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = req.json()
    print(posts)
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # find the post based on id
    # post = next((p for p in posts if p["id"] == post_id), None)
    req = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = req.json()
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)