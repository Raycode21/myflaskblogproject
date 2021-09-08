from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == "__main__":
	app.run(debug=True)
