from flask import Flask, render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv
from discordwebhook import Discord


load_dotenv()
token=os.getenv('TOKEN')
disc=Discord(url=os.getenv('Trafic_webhook'))
disc2=Discord(url=os.getenv('hospital_webhook'))
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
                return redirect("/hospital")
            elif result[0][0]=="trp":
                return redirect("/traffic-police")
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

@app.route('/hospital', methods=['GET','POST'])
def hospital():
    db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="2002",
            database="AmbulanceAlertingSystem"
    )
    cursor =db.cursor()
    cursor.execute('SELECT hospital_name,accept_patient FROM hospital')
    hospital_name_hp=cursor.fetchall()
    for ki in range(len(hospital_name_hp)):
        hospital_name_hp[ki]=list(hospital_name_hp[ki])
        if hospital_name_hp[ki][1]==1:
            hospital_name_hp[ki][1]='Yes'
        else:
            hospital_name_hp[ki][1]='No'
    print(hospital_name_hp)
    if request.method=='POST':
        hospital_name_get=request.form.get('hospital_name_hp')
        ap_accept_patient=request.form.get('accept_patient')
        sql=f'UPDATE hospital SET accept_patient={ap_accept_patient} WHERE hospital_name="{hospital_name_get}"'
        print(sql)
        cursor.execute(sql)
        db.commit()
        sql=f'SELECT hospital_name,accept_patient FROM hospital WHERE hospital_name="{hospital_name_get}"'
        cursor.execute(sql)
        hospital_name_hp2=cursor.fetchall()
        for ki in range(len(hospital_name_hp2)):
            hospital_name_hp2[ki]=list(hospital_name_hp2[ki])
            if hospital_name_hp2[ki][1]==1:
                hospital_name_hp2[ki][1]='Yes'
            else:
                hospital_name_hp2[ki][1]='No'
        return render_template('hospital.html',hospital_name_hp=hospital_name_hp2,record_updated="Changed successfully")
    return render_template('hospital.html',hospital_name_hp=hospital_name_hp)
@app.route('/traffic-police', methods=['GET','POST'])
def traffic_poice():
    db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="2002",
            database="AmbulanceAlertingSystem"
    )
    cursor =db.cursor()
    cursor.execute('SELECT DISTINCT location,s_s_status FROM trafficsignal')
    traffic_police_tp=cursor.fetchall()
    for ki in range(len(traffic_police_tp)):
        traffic_police_tp[ki]=list(traffic_police_tp[ki])
        if traffic_police_tp[ki][1]==1:
            traffic_police_tp[ki][1]='Free'
        else:
            traffic_police_tp[ki][1]='Busy'
    print(traffic_police_tp)
    if request.method=='POST':
        traffic_location_tp=request.form.get('traffic_name_tp')
        signal_statu_tp=request.form.get('Signal_Status')
        sql=f'UPDATE trafficsignal SET s_s_status={signal_statu_tp} WHERE location="{traffic_location_tp}"'
        print(sql)
        cursor.execute(sql)
        db.commit()
        sql=f'SELECT DISTINCT location, s_s_status FROM trafficsignal WHERE location="{traffic_location_tp}"'
        cursor.execute(sql)
        traffic_police_tp2=cursor.fetchall()
        for ki in range(len(traffic_police_tp2)):
            traffic_police_tp2[ki]=list(traffic_police_tp2[ki])
            if traffic_police_tp2[ki][1]==1:
                traffic_police_tp2[ki][1]='Free'
            else:
                traffic_police_tp2[ki][1]='Busy'
        return render_template('traffic_police.html',traffic_list=traffic_police_tp2,record_updated="Changed successfully")
    return render_template('traffic_police.html',traffic_list=traffic_police_tp)
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
        sql=f"SELECT hospital_name,accept_patient FROM hospital where location='{route_to}'"
        cursor.execute(sql)
        hospital_details=cursor.fetchall()
        print(hospital_details)
        text_hospital_name=''
        text_hospital=f"A patient is comming"
        for ki in range(len(hospital_details)):
            hospital_details[ki]=list(hospital_details[ki])
            if hospital_details[ki][1]==0:
                hospital_details[ki][1]="No"
            else:
                hospital_details[ki][1]="Yes"
            text_hospital_name+=f"{hospital_details[ki][0]}, "
        disc2.post(content=f"A patient is comming to {route_to}. Your hospital {text_hospital_name} cover in this location, get ready with the bed")
        signal_details=list(signal_details)
        for ki in range(len(signal_details)):
            signal_details[ki]=list(signal_details[ki])
            print(signal_details[ki][2])
            if signal_details[ki][2]==0:
                signal_details[ki][2]="Busy"
            else:
                signal_details[ki][2]="Free"
            print(signal_details[ki][2])
            discord_notification=str(f"Ambulance is comming in {signal_details[ki][0]}, {signal_details[ki][1]}. free the road from {route_from} to {route_to}")
            print(discord_notification)
            disc.post(content=discord_notification)
        print(signal_details)
        
        return render_template('Ambulance_driver_Page.html',signal_details=signal_details,fromlist=fromlist, hospital_details=hospital_details)

    return render_template('Ambulance_driver_Page.html',fromlist=fromlist)

if __name__ == "__main__":
    app.run()
    
