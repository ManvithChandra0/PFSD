from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
app = Flask(__name__) #flask object

app.config['SECRET_KEY'] = "1e83685206c53c001c813c57ef736c42"


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:%s@localhost:3306/flaskmysql" % quote('Manvith@123')

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employee_table'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    dob = db.Column(db.String(100))
    dept = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    contactno = db.Column(db.String(100),unique=True)

    def __init__(self, id, name, gender, dob,dept,email,password,contactno):
        self.id=id
        self.name=name
        self.gender=gender
        self.dob=dob
        self.dept=dept
        self.email=email
        self.password=password
        self.contactno=contactno

@app.route("/")
def main():
    return "My Flask Project"

@app.route("/demo1")
def demofunction1():
    return "<b> PFSD S15 Section </b>"

@app.route("/demo2/<name>")
def demofunction2(name):
    return "Hello %s" %name

@app.route("/demo3/<int:id>")
def demofunction3(id):
    return "ID Value= %d" %id

@app.route("/demo4/<float:id>")
def demofunction4(id):
    return "ID Value= %f" %id

@app.route("/index",endpoint="index")
def indexfunction():
    return render_template("index.html")

@app.route("/formdemo",endpoint="formdemo")
def formdemofunction():
    return render_template("formdemo.html")

@app.route("/displayformdata",endpoint="displayformdata",methods=['POST','GET'])
def displayformdatafunction():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        gender = request.form['gender']
        dateofbirth = request.form['dateofbirth']
        department = request.form['department']
        emailid = request.form['emailid']
        contactno = request.form['contactno']
    if request.method == 'GET':
        id = request.form['id']
        name = request.form['name']
        gender = request.form['gender']
        dateofbirth = request.form['dateofbirth']
        department = request.form['department']
        emailid = request.form['emailid']
        contactno = request.form['contactno']

    return render_template("displayformdata.html",id=id,name=name,gender=gender,dateofbirth=dateofbirth,department=department,emailid=emailid,contactno=contactno)


@app.route("/empreg",endpoint="empreg")
def empregfunction():
    return render_template("empreg.html")

@app.route("/saveemp",endpoint="saveemp",methods=['POST','GET'])
def saveempfunction():
    msg=None
    if request.method == 'POST':
        try:
            id = request.form['id']
            name = request.form['name']
            gender = request.form['gender']
            dateofbirth = request.form['dateofbirth']
            department = request.form['department']
            emailid = request.form['emailid']
            password = request.form['password']
            contactno = request.form['contactno']
            emp=Employee(id=id,name=name,gender=gender,dob=dateofbirth,dept=department,email=emailid,password=password,contactno=contactno)
            db.session.add(emp)
            db.session.commit()
            msg="Employee Added Successfully"
        except Exception as e:
            print(e)
            msg="Fail to Add Employee Record"
        return render_template("empreg.html",msg=msg)

@app.route("/emplogin",endpoint="emplogin")
def emploginfunction():
    return render_template("emplogin.html")

@app.route("/checkemplogin",endpoint="checkemplogin",methods=['POST','GET'])
def checkemploginfunction():
    if request.method == 'POST':
        emailid = request.form['emailid']
        password = request.form['password']

        flag = Employee.query.filter_by(email=emailid,password=password).first()
        print(flag)

        if flag:
            emp = Employee.query.filter_by(email=emailid).first()
            session['eid'] = emp.id
            session['ename'] = emp.name
            return render_template("emphome.html",eid=emp.id,ename=emp.name)
        else:
            return render_template("emplogin.html",msg="Login Failed")

@app.route("/emphome",endpoint="emphome")
def emphomefunction():
    eid=session['eid']
    ename=session['ename']
    return render_template("emphome.html",eid=eid,ename=ename)

@app.route("/empchangepwd",endpoint="empchangepwd")
def empchangepwdfunction():
    eid=session['eid']
    ename = session['ename']
    return render_template("empchangepwd.html",eid=eid,ename=ename)

@app.route("/updatepwd",endpoint="updatepwd",methods=['POST','GET'])
def updatepwdfunction():
    msg=None
    eid=session['eid']
    ename = session['ename']
    if request.method == 'POST':
        opwd = request.form['opwd']
        npwd = request.form['npwd']

        flag = Employee.query.filter_by(id=eid,password=opwd).all()
        #print(flag)

        if flag:
            emp = Employee.query.filter_by(id=eid).one()
            print(emp)
            emp.password = npwd
            db.session.commit()
            msg = "Password Updated Successfully"
        else:
            msg = "Old Password is Incorrect"

        return render_template("empchangepwd.html",msg=msg)

@app.route("/emplogout",endpoint="emplogout")
def emplogoutfunction():
    return render_template("emplogin.html")

@app.route("/viewemps",endpoint="viewemps")
def viewempsfunction():
    emplist = Employee.query.all()
    count = Employee.query.count()
    return render_template("viewemps.html",emplist=emplist,count=count)

@app.route("/deleteemp/<int:eid>",endpoint="deleteemp")
def deleteempfunction(eid):
    emp = Employee.query.filter_by(id=eid).first()
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for('viewemps'))

if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True)