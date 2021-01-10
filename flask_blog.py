import os
from flask import Flask, render_template, url_for, flash, redirect
from flask.globals import request
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('secret_key')

posts = [
    {
    'author': "Viren Patel",
    "title": "Blog Post 1",
    'content': 'First post content',
    'date_posted': "Jan 10, 2021"
    },
    {
    'author': "Manav Shah",
    "title": "Blog Post 2",
    'content': 'Second post content',
    'date_posted': "Jan 10, 2021"
    }
]

# Home page.
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

# About Page.
@app.route('/about')
def about():
    return render_template('about.html', title="Blog | About")

# Registration Page.
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == "POST":
        if form.validate_on_submit():

            flash(f'Account created for {form.username.data}!', category="success")
            return redirect(url_for('home'))

    return render_template('register.html', title="Register", form=form)

# Login Page.
@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            flash('You have been loggen in successfully!', 'success')
        else:
            flash('Login Unsucessful. Please check username and password!', 'danger')

    return render_template('login.html', title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)