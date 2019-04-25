import os
from flask import Flask, render_template, json, request
# from flaskext.mysql import MySQL
import mysql.connector
from utils import Utility as Util
app = Flask(__name__)

__author__ = 'hanvitha'

app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
# APP_ROOT = "/opt/app-root/src/aahack"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
db = mysql.connector.connect(host="http://mysql-registration.apps.aahw6prep-7559.openshiftworkshop.com",user="reg_user", password="reg_user",database="reg_db", port=3306)
cursor = db.cursor()
# mysql = MySQL()
# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'reg_user'
# app.config['MYSQL_DATABASE_DB'] = 'reg_db'
# app.config['MYSQL_DATABASE_HOST'] = 'mysql.registration.svc'
# mysql.init_app(app)
# https://mysql-registration.apps.aahw6prep-7559.openshiftworkshop.com

u = Util
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/save", methods=["GET", "POST"])
def save():
    try:
        util = Util()
        print("User %s logged in!"%request.form['fname'])
        status = util.saveUser(db, cursor, request)
        if(status == 200):
            return render_template("thankyou.html", fname=request.form['fname'])
        raise Exception("Unable to insert data!")
    except Exception as e:
        print( "<h1>Oops! Something went wrong.. Could you try after sometime or reach out to the host!</h1>")
        return json.dumps({'error': str(e)})

@app.route("/usersRegistered", methods=["GET", "POST"])
def users():
    # get all details from form
    formelements = request
    # create oc login
    # send email to their email address!

    return "something!"


if __name__ == '__main__':
    app.run()
