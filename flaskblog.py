from flask import Flask, render_template, url_for, flash
from flask.helpers import flash
from werkzeug.utils import redirect

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm, RegestrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8bee0a560054550f03c9d0eeed455e78'

# BD Location.
# Development Database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# ORM, SQLite in development, Postgress in production.
db = SQLAlchemy(app)

# User to Post is one to many relations.


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # Posts Ids.
    posts = db.relationship('Post', backref='author', lazy=True)

    # How object are printed.
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegestrationForm()

    # This is a shortcut for form.is_submitted() and form.validate().
    if form.validate_on_submit():
        flash(f'Account created Done, User{form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@flask.com' and form.password.data == '123456789':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Check your username and Password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
