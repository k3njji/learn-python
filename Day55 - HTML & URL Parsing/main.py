from flask import Flask, request
app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

@app.route("/")
@make_bold
def home():
    return "Hello, Flask!"

@app.route("/greet/<name>/<int:age>")
def greet(name, age):
    # name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name}!</h1><p>You are {age}.</p>"

@app.route("/bye")
def bye():
    return "Goodbye!"

if __name__ == "__main__":
    app.run(debug=True)