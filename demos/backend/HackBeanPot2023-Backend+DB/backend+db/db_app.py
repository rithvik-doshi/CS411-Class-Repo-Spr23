from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = False

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.app_context().push()

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Models
class User(db.Model):
	__tablename__ = 'Users'
	# Id : Field which stores unique id for every row in
	# database table.
	# first_name: Used to store the first name if the user
	# last_name: Used to store last name of the user
	# Age: Used to store the age of the user
	pid = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50), unique=False, nullable=False)
	last_name = db.Column(db.String(50), unique=False, nullable=False)
	age = db.Column(db.Integer, nullable=False)

	# repr method represents how one object of this datatable
	# will look like
	def __repr__(self):
		return f"Name : {self.first_name}, Age: {self.age}"

class Post(db.Model):
	__tablename__ = 'Posts'
	post_id = db.Column(db.Integer, primary_key=True)
	pid = db.Column(db.Integer, db.ForeignKey(User.pid), primary_key=True)
	text = db.Column(db.String(300), unique=False, nullable=False)

	user = db.relationship('User', foreign_keys='Post.pid')

	def __repr__(self):
		return f"{self.user.first_name} {self.user.last_name} posted: {self.text}"

@app.route('/')
def check():
    return "This is the database-app"

if __name__ == '__main__':
	app.run()
