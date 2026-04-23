from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'
UPLOAD_FOLDER = 'C:\\Python by Angela Yu\\Day68 - Authentication\\static\\files\\'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Python by Angela Yu/Day68 - Authentication/instance/users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB



class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable = False)
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        if db.session.execute(db.select(User).where(User.email == email)).scalar():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('register'))
        else:
            new_user = User(
                email = email,
                name = name,
                password = password
            )
            print(new_user.password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('secrets.html')
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar()
        if user:
            if check_password_hash(user.password, request.form.get('password')):
                login_user(user)
                return render_template('secrets.html')
            else:
                flash('Password incorrect, please try again.')
                return redirect(url_for('login'))
        else:
            flash("That email does not exist, please register first")
            return redirect(url_for('register'))
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    if current_user.is_authenticated:
        return render_template("secrets.html", name=current_user.name)
    return render_template("secrets.html")


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True)
