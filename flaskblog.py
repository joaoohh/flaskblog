from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
posts= [
    {
        'author': 'João Henrique Cordeiro',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'date_posted': 'April 1, 2025'
    },

    {
        'author': 'Geovana Remes Gomes Araujo',
        'title': 'Blog Post 2',
        'content': 'Second Blog Post',
        'date_posted': 'April 2, 2025'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route("/about")
def about():
    return render_template('about.html', title = 'About')
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form=form)
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)
if __name__ == '__main__':
    app.run(debug=True)

