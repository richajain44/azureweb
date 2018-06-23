from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
import os
from flask_migrate import Migrate
app =Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Timepass@123@localhost/height_collector'
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://%s:%s@%s/%s' % (os.environ['DBUSER'], os.environ['DBPASS'], os.environ['DBHOST'], os.environ['DBNAME'])
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://richa@height-collect:Password*6@height-collect.postgres.database.azure.com/datadb'
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://manager@height-collector:Timepass@123@height-collector.postgres.database.azure.com/postgres'

db =SQLAlchemy(app)
MIGRATE = Migrate(app, db)
class Data(db.Model):
	_tablename_="data"
	id=db.Column(db.Integer,primary_key=True)
	email=db.Column(db.String(120),unique=True)
	#email=db.Column(db.String(120))
	height=db.Column(db.Integer)
	
	def __init__(self,email,height):
		self.email=email
		self.height=height
	
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/success",methods=['POST'])

def success():
	if request.method=='POST':
		email= request.form['email_name']
		height =request.form['height_name']
		print(email,height)
		send_email(email,height)
		
		if db.session.query(Data).filter(Data.email==email).count()==0:
			data=Data(email,height)
			db.session.add(data)
			db.session.commit()
			return render_template("success.html")
		return render_template("index.html", text="Please enter a new email address")
	
if __name__=="__main__":
	app.debug=True
	app.run()
