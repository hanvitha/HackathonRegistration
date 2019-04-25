
from flask import json
import random

class Utility:
    def saveUser(self, conn, cursor, request):
        try:
            print("Not yet!")
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            phone = request.form['phone']
            team = request.form['team']
            role = request.form['role']
            redhatid = request.form['redhatid']
            print(fname)
            uid = fname[:1]+lname
            existingusers = cursor.execute("select *from users where uid=%s"%uid)
            if(existingusers>0):
                uid = uid+random.randint(10,210)

            sql_insert_query ='''INSERT INTO users(uid,fname,lname, email,phone, team, redhatid, role) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
            insert_tuple = (uid,fname,lname, email,phone, team, redhatid, role)
            print("Trying to insert! ", sql_insert_query)
            print("Connection ",conn)
            result = cursor.execute(sql_insert_query, insert_tuple)
            conn.commit()
            print("saved %s,%s,%s,%s,%s,%s,%s,%s"%(uid,fname,lname, email, phone, team, redhatid, role))
            return 200
        except Exception as e:
            print (json.dumps({'error':str(e)}))
            return 400
        finally:
            cursor.close()
            conn.close()

    def fetchUserDetails(self, conn):
        return "Wow!"