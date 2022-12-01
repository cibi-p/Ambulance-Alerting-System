from flask import Flask, render_template, request, redirect
import mysql.connector

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    if request.method == "POST":
        email=request.form.get("email")
        password=request.form.get("password")

        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="2002",
            database="AmbulanceAlertingSystem"
        )
        mycursor=db.cursor()
        sql="SELECT proffession FROM user WHERE email_id=%s and password=%s;"
        val=(email,password)
        mycursor.execute(sql,val)
        result=mycursor.fetchall()
        if len(result)!=0:
            if result[0][0]=="hpt":
                print(result)
                return render_template("hospital.html")
            elif result[0][0]=="trp":
                return render_template("traffic_police.html")
            else:
                return redirect('/ambulance-drive')
        else:
            return render_template('index.html',password="False")
        db.commit()

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

        if proffession=='trp':
            location=request.form.get("location")
            Discord_uname=request.form.get("d_name")
            from1=request.form.get("from1")
            to1=request.form.get("to1")
            from2=request.form.get("from2")
            to2=request.form.get("to2")
            print("adf",from2,to2)
            sql="INSERT INTO trafficsignal(f_rom,t_o,location,name,s_s_status,discord_name) VALUES(%s,%s,%s,%s,1,%s)"
            val=(from1,to1,location,name,Discord_uname)
            mycursor.execute(sql,val)
            db.commit()
            if from2!="" and to2!="":
                sql="INSERT INTO trafficsignal(f_rom,t_o,location,name,s_s_status,discord_name) VALUES(%s,%s,%s,%s,1,%s)"
                val=(from2,to2,location,name,Discord_uname)
                mycursor.execute(sql,val)
                db.commit()
        elif proffession=="hpt":
            hospital_name=request.form.get("hospital")
            ready_to_attend=int(request.form.get("attendpatient"))
            discord_name_d=request.form.get("d_name-d")
            hpt_location=request.form.get("hospitallocation")
            print("-->"+hpt_location)
            sql="INSERT INTO hospital(h_discord_name,hospital_name,accept_patient,location) VALUES(%s,%s,%s,%s)";
            val=(discord_name_d,hospital_name,ready_to_attend,hpt_location)
            mycursor.execute(sql,val)
            db.commit()
        return "<h1>Record added Successfully</h1>"
    return render_template('Admin-Page.html')


@app.route('/ambulance-drive',methods=["GET","POST"])
def ambulancepage():
    db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="2002",
            database="AmbulanceAlertingSystem"
        )
    cursor = db.cursor()
    cursor.execute('SELECT f_rom,t_o from trafficsignal')
    fromlist=cursor.fetchall()
    if request.method=="POST":
        coursor=db.cursor()
        route_from=request.form.get("ambulancedriver-from")
        route_to=request.form.get("ambulancedriver-to")
        sql=f"SELECT location,name,s_s_status,discord_name FROM trafficsignal WHERE f_rom='{route_from}' AND t_o='{route_to}'"
        cursor.execute(sql)
        signal_details=cursor.fetchall()
        print(signal_details)
        if signal_details[0][2]==0:
            signal_status="Busy"
        else:
            signal_status="Free"
        return render_template('Ambulance_driver_Page.html',tp_name=signal_details[0][1],tp_location=signal_details[0][0],s_status=signal_status,fromlist=fromlist)

    return render_template('Ambulance_driver_Page.html',fromlist=fromlist)
if __name__ == "__main__":
    app.run()