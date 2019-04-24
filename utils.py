
from flask import json
import random

class Utility:
    def saveUser(self, conn, request):
        try:
            print("Not yet!")
            cursor = conn.cursor()
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            phone = request.form['phone']
            team = request.form['team']
            role = request.form['role']
            redhatid = request.form['redhatid']

            uid = fname[:1]+lname
            existingusers = cursor.execute("select *from users where uid=%s",[uid])
            if(existingusers>0):
                uid = uid+random.randint(10,210)
            print("Trying to insert! ")
            cursor.execute("INSERT INTO users(uid,fname,lname, email,phone, team, redhatid, role)) VALUES(%s,%s,%s,%d,%s,%s,%s,%s)",(uid,fname,lname, email,phone, team, redhatid, role))
            conn.commit()
            print("yay!")
            return 200
        except Exception as e:
            print (json.dumps({'error':str(e)}))
            return 400
        finally:
            cursor.close()
            conn.close()

    def fetchUserDetails(self, conn):
        return "Wow!"