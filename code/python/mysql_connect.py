import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="2002",
	database="AmbulanceAlertingSystem"
)
mycursor = mydb.cursor()
sql="INSERT INTO user(name,Email_Id,proffession) VALUES('Hari','ex@example.com','dtr')"
mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record inserted.")
