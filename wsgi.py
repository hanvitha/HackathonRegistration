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
# host="mysql.registration.svc.cluster.local"
host="mysql.registration.svc"
user="root"
password="reg_user"
database="reg_db"

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/save", methods=["GET", "POST"])
def save():
    try:
        db = mysql.connector.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database
                                     )
        cursor = db.cursor(buffered=True)
        util = Util()
        print("User %s logged in!"%request.form['fname'])
        status, uid = util.saveUser(db, cursor, request)
        if status and status == 200:
            return render_template("thankyou.html", fname=request.form['fname'], uid=uid)
        raise Exception("Unable to insert data!")
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        return "<h1>Oops! Something went wrong.. Could you try after sometime or reach out to the host!</h1>"
    finally:
        db.close()
        cursor.close()

@app.route("/users", strict_slashes=False)
def users():
    return render_template("users.html")


@app.route("/users/<status>", strict_slashes=False, methods=["GET", "POST"])
def usersall(status=None):
    try:
        db = mysql.connector.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database
                                     )
        cursor = db.cursor(buffered=True)
        if status == 'all':
            cursor.execute('''select * from users''')
        elif status == 'done':
            cursor.execute('''select * from users where status=1''')
        else:
            cursor.execute('''select * from users where status=0''')

        allusers = cursor.fetchall()
        # print(allusers)
        return render_template("usersRegistered.html", users=allusers, host=host,user=user, password=password, database=database)
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        return "<h1>Oops! Something went wrong.. Could you try after sometime or reach out to the host!</h1>"
    finally:
        db.close()
        cursor.close()

@app.route("/updatestatus", methods=["POST"])
def updatestatus():
    db = mysql.connector.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database
                                 )
    cursor = db.cursor(buffered=True)
    uid = request.args.get('uid')
    status = request.args.get('status')
    print("checking on status")
    if(status=="0"):
        status="1"
    else:
        status="0"
    cursor.execute('''update users set status=%s where uid=%s''', (status,uid))
    print("Done updating status")
    return "success"

if __name__ == '__main__':
    app.run()
