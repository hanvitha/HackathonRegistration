
This is python flask app created to register attendees during an event. This is made to run on Openshift cluster.
Once registered, we had the users details. With that, Openshift cluster admin can go in and give them cluster access/register them in console. 

Mysql table schema:
make these as variables in secrets..i didn’t as it was a last minute app and also didn’t have a lot to hide.
host="mysql.registration.svc.cluster.local"
user="root"
password="reg_user"
database="reg_db"


uid :userID ->generated as (firstletter from firstname) + lastname example hanvitha gavini->hgavini, if multiple, it will be number appended like hgavini2 from next.
fname : Firstname
lname: Last name
email : email address 
phone: phone
team :team name
redhatid: redhatid if any
role: current role at their org
status: given cluster access 1 or not 0
All strings

Flow:
Home -> take in user details (  /save )->thankyou html with user name

/users
Users registered ->usersregistered.hmtl

/users/<status>
To see users who are given cluster access.status = 1 registered, status 0 still need to be added to cluster

Once you configured your mysql db on openshift -> go to self service service from developer view -> copy the git code base -> paste it in the app repo area. everything else default / your preferences and click create. you will be able to see the app up and running in minutes.





