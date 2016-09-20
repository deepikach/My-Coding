from flask import Flask,request
from flask_mongoengine import MongoEngine

db=MongoEngine()
app=Flask(__name__)
app.config['MONGODB_SETTINGS']={
   'db':'test',
   'host':'mongodb://localhost:27017/test'
}
db.init_app(app)

class Clientlogin(db.Document):
      email=db.StringField(max_length=20)
      password=db.StringField(max_length=20)

class Analysis(db.Document):
      productname=db.StringField(max_length=20)
      numberofsurveysdoneonaproduct=db.IntField(max_length=30)
      surveycompanyname=db.StringField(max_length=30)
      peopleparticipated=db.IntField(max_length=30)
      remarks=db.StringField(max_length=50)

@app.route('/login',methods=["POST","GET"])
def login():
    a=Clientlogin(email='ping@yahoo.com',password='*****')
    a.save()
    return Clientlogin.objects.to_json()

@app.route('/analysis',methods=["POST","GET"])
def analysis():
   b=Analysis(productname='kurtha',numberofsurveysonaproduct="100",surveycomapanyname='surveymonkey',peopleparticipated='900',remarks='improve')
   b.save()
   return Analysis.objects.to_json()
if __name__=='__main__':
   app.run()