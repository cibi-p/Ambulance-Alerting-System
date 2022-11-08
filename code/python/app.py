from flask import Flask, render_template, request
import mysql.connector

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin',methods=["GET","POST"])
def admin():
    if request.method == "POST":
        name=request.form.get("name")
        email=request.form.get("Email")
        proffession=request.form.get("proffession")
        password=request.form.get("password")

        #database connection
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="2002",
            database="AmbulanceAlertingSystem"
        )
        mycursor=db.cursor()
        sql="INSERT INTO user(name,Email_Id,proffession,password) VALUES(%s,%s,%s,%s);"
        val=(name,email,proffession,password)

        mycursor.execute(sql,val)
        db.commit()

        return "<h1>Record added Successfully"
    return render_template('Admin-Page.html')

if __name__ == "__main__":
    app.run()