from flask import render_template, url_for, flash, redirect, request, abort

from todo_project import app, db, bcrypt

# Import the forms
from todo_project.forms import LoginForm, RegistrationForm, UpdateuserForm

# Import the Models
from todo_project.models import User, Task

# Import 
from flask_login import login_required, current_user, login_user, logout_user

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    
    # After you submit the form
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # Check if the user exists and the password is valid
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login Successfull', 'success')
            return render_template('home.html', title='Home Page', labels=labels)
        else:
            flash('Login Unsuccessful. Please check Username Or Password', 'danger')
    
    return render_template('login.html', title='Login', form=form)
    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/register", methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created For {form.username.data}', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='User Page', labels=labels)