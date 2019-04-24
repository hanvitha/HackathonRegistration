import os, pandas
from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from utils import Utility as Util
app = Flask(__name__)

__author__ = 'hanvitha'

app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
# APP_ROOT = "/opt/app-root/src/aahack"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_USER'] = 'reg_user'
app.config['MYSQL_PASSWORD'] = 'reg_user'
app.config['MYSQL_DATABASE'] = 'reg_db'
app.config['MYSQL_DATABASE_HOST'] = 'http://mysql-registration.apps.aahw6prep-7559.openshiftworkshop.com'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/save", methods=["GET", "POST"])
def save():
    try:
        conn = mysql.connect()
        status = Util.saveUser(conn, request)
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
