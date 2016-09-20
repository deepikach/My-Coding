from flask import Flask
from flask_mongoengine import MongoEngine

db=MongoEngine()

app= Flask(__name__)

app.config['MONGODB_SETTINGS'] ={
      'db':'test',
      'host':'mongodb://localhost:27017/test'
}

db.init_app(app)

class User(db.Document):
      email=db.StringField(max_length=30)
      password=db.StringField(max_length=30)

class Addmembers(db.Document):
      Employeename=db.StringField(max_length=20)
      Designation=db.StringField(max_length=20)
      Gender=db.StringField(choices=[('m','male'),('f','female')])
      Qualification=db.StringField(max_length=20)
      Experience=db.IntField(max_length=20)
      Address=db.StringField(max_length=20)
      DOJ=db.IntField(max_length=20)
      Emailid=db.StringField(max_length=20)
      password=db.StringField(max_length=20)

class Clientorder(db.Document):
      companydetails=db.StringField(max_length=20)
      surveyproduct=db.StringField(max_length=20)
      minpeople=db.IntField(max_length=20)
      surveycost=db.IntField(max_length=20)
      deliverydate=db.StringField(max_length=20)

class Clientpayment(db.Document):
      Companyname=db.StringField(max_length=20)
      Nameofsurvey=db.StringField(max_length=20)
      Totalamount=db.IntField(max_length=20)      
      Bankname=db.StringField(max_length=20)
      Accountnumber=db.IntField(max_length=20)
      IFSCcode=db.StringField(max_length=20)

class Clientfeedback(db.Document):
      companyname=db.StringField(choices=[('y','your opinion'),('m','my survey'),('f','fieldteam')])
      nameofsurvey=db.StringField(max_length=20)
      surveydate=db.StringField(max_length=20)
      numofpeopleparticipated=db.IntField(max_length=20)
      status=db.StringField(choices=[('s','starting stage'),('i','in progress'),('c','completed')])
      feedback=db.StringField(choices = [('e','excellent'),  ('g','good'),('n','not satisfactory')])
      suggestions=db.StringField(max_length=90)

def create_db():
    a.User(email="string@yahoo.com",password="12345")
    a.save()
    
@app.route('/login',methods=["POST","GET"])
def login():
    a=User(email="pandu@gmail.com",password="******")
    a.save()
    return User.objects.to_json()

@app.route('/add',methods=["POST","GET"])
def add():
    b=Addmembers(Employeename="priya",Designation="developer",Gender="m",Qualification="m.tech",Experience="7",Address="medchal",Emailid="priya@yahoo.com", DOJ="12",password="123456")
    b.save()
    #b1.delete(oid="57a58734db3f0c14b08949fb")
    return Addmembers.objects().to_json()

@app.route('/order',methods=["POST","GET"])
def order():
    c=Clientorder(companydetails="yoo app",surveyproduct="clothes",minpeople=6,surveycost=60000,deliverydate="jul25")
    c.save()
    return Clientorder.objects().to_json()

@app.route('/payment',methods=["POST","GET"])
def payment():
    d=Clientpayment(Companyname="allusion",Nameofsurvey="surveymonkey",Totalamount=350,Bankname="SBH",Accountnumber=6228935766,IFSCcode="ISN569B369")
    d.save()
    return Clientpayment.objects().to_json()

@app.route('/feedback',methods=["POST","GET"])
def feedback():
    e=Clientfeedback(companyname="y",nameofsurvey="surveymonkey",surveydate="aug25",numofpeopleparticipated=900,status="i",feedback="g",suggestions="improve more")
    e.save()
    return Clientfeedback.objects().to_json()
                                                  
if __name__ == '__main__':
    app.run(debug=True)

