import flask
import random

app = flask.Flask(__name__)

random_number = random.randint(0, 10)

@app.route("/")
def home(): 
    return "Welcome to the Higher or Lower Game! Guess a number between 0 and 10.<br>" \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/guess/<int:number>")
def guess(number):
    if number < random_number:
        return "Too low! Try again.<br>" \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > random_number:
        return "Too high! Try again.<br>" \
        'img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return "Congratulations! You guessed the number!<br>" \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    
if __name__ == "__main__":
    app.run(debug=True)