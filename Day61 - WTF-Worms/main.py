from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
# from models import User

class MyForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[DataRequired(), validators.Regexp(r'^[A-Za-z0-9]+$')])
    submit = SubmitField('Submit')

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect('/success')
        else:
            return redirect('/denied')
    else:
        print(form.errors)
    return render_template('login.html', form=form)

@app.route('/denied')
def denied():
    return render_template('denied.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
