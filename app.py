from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2d5ca6681f533eeb43d8c4d92e3a9b87'

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

@app.route("/register")
def register():	
	form = RegistrationForm()
	return render_template("register.html", title='Register', form=form)

@app.route("/Login")
def register():	
	form = LoginForm()	
	return render_template("Login.html", title='Login', form=form)

if __name__ == "__main__":
	app.run(debug=True)
