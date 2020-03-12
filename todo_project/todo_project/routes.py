from flask import render_template, url_for, flash, redirect, request, abort

# Import the forms
from todo_project.forms import LoginForm, RegistrationForm, UpdateuserForm

from todo_project import app


labels = ['Work', 'Study', 'Sports']

@app.errorhandler(404)
def error_404(error):
    return (render_template('errors/404.html'), 404)

@app.errorhandler(403)
def error_403(error):
    return (render_template('errors/403.html'), 403)

@app.errorhandler(500)
def error_500(error):
    return (render_template('errors/500.html'), 500)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register User', form=form)


@app.route("/user")
def user():
    return render_template('user.html', title='User Page', labels=labels)