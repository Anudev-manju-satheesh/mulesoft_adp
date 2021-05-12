from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init app

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(base_dir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

#initdb
db = SQLAlchemy(app)

#init marshmallow
ma = Marshmallow(app)


#creation class
class formula_one(db.Model):
    cno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),unique = True)
    car = db.Column(db.String(100))
    points = db.Column(db.Integer)

    def __init__(self,cno, name,car,points):
        self.cno = cno
        self.name = name
        self.car = car
        self.points = points

#Schema
class f1Schema(ma.Schema):
    class Meta:
        fields = ('cno','name','car','points')


#init schema
f1_Schema = f1Schema()
f1_Schema_s = f1Schema(many=True)


#routes
@app.route('/create', methods =['POST'])
def add_member():
    cno = request.json['cno']
    name = request.json['name']
    car = request.json['car']
    points = request.json['points']

    new_entry = formula_one(cno,name,car,points)

    db.session.add(new_entry)
    db.session.commit()

    return f1_Schema.jsonify(new_entry)

#getting all entries
@app.route('/get_all',methods = ['GET'])
def get_entries():
    all_entry = formula_one.query.all()
    result = f1_Schema_s.dump(all_entry)
    return jsonify(result)

#getting single entry
@app.route('/get_all/<cno>', methods = ['GET'])
def get_entry(cno):
    entry = formula_one.query.get(cno)
    return f1_Schema.jsonify(entry)


#update
@app.route('/f1/<cno>', methods =['PUT'])
def update(cno):
    new = formula_one.query.get(cno)

    cno = request.json['cno']
    name = request.json['name']
    car = request.json['car']
    points = request.json['points']

    new.cno = cno
    new.name = name
    new.car = car
    new.points = points

    db.session.commit()

    return f1_Schema.jsonify(new)

#delete entry
@app.route('/f1/<cno>', methods = ['DELETE'])
def delete_entry(cno):
    entry = formula_one.query.get(cno)
    db.session.delete(entry)
    db.session.commit()
    return f1_Schema.jsonify(entry)


#run server

if __name__  == '__main__':
    app.run(debug = True)