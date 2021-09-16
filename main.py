from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all() 


@app.route("/signup/" , method = ["POST"])
def signUp():
    username = request.form["username"]
    password = request.form["password"]
    user = User(username, password)
    db.session.add(user)
    db.session.commit()
    return {"username": username , "password":password}


    
app.run()
