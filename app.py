from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this is secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(100), default='default.png')


def __init__(self, username, email, password, **kwargs):
    self.username = username
    self.email = email

    self.set_password(password)


def __repr__(self):
    return f"<User('{self.id}', '{self.username}', '{self.email}')>"


def set_password(self, password):
    self.password = generate_password_hash(password)


def check_password(self, password):
    return check_password_hash(self.password, password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutme.html')

@app.route('/post')
def post():
    return render_template('post.html')

if __name__ == '__main__':
    app.debug = True
    app.run()