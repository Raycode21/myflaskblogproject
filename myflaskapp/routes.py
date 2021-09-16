from flask import render_template, url_for, flash, redirect
from myflaskapp import app
from myflaskapp.forms import RegistrationForm, LoginForm
from myflaskapp.models import User, Post


posts = [
{
	'author': 'Ray Code',
	'title': 'Blogpost 1',
	'content': 'First Post Content',
	'date_posted': 'September 6, 2021'
	
},
{
	'author': 'Ronald Dacy',
	'title': 'Blogpost 2',
	'content': 'Second Post Content',
	'date_posted': 'September 7, 2021'
}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts=posts)

@app.route("/about")
def about():
	return render_template("about.html", title='About')	

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)