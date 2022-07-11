from flask.helpers import flash
from searchgolfs import app
from flask import render_template, redirect, url_for, flash
from searchgolfs.models import Item, User
from searchgolfs.forms import RegisterForm, LoginForm
from searchgolfs.models import db
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/searchgolf')
def searchgolf():
    # db.create_all()
    items = Item.query.all()
    return render_template('searchgolf.html', items=items)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()

    # when the user clicks submit we will check some stuff
    if form.validate_on_submit():
        user_being_created = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)

        db.session.add(user_being_created)
        db.session.commit()
        return redirect(url_for('searchgolf'))
    
    # check validations if errors capture here
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f' There was an error creating your user {err_msg}', category='danger')

    return render_template('register.html',form=form)


@app.route('/login', methods=['GET','POST'])
def login_page():

    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success you are logged in as {attempted_user.username}',category='success')
            return redirect(url_for('searchgolf'))
        else:
            flash(f'Username and password is not matched you are logged in as {attempted_user.username}', category='danger')

    return render_template('login.html', form=form)