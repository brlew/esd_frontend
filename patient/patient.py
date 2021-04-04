from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import environ

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/patient'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/g1t6_patient'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TO RUN SERVICE
# docker run -p 5500:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/g1t6_patient jthm/patient:g1t6

db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(25), nullable=True)
    partialnric = db.Column(db.String(15),nullable=True)
    race = db.Column(db.String(15), nullable=True)
    dob = db.Column(db.String(15), nullable=True)
    mobileno = db.Column(db.Integer, nullable=True)

    def json(self):
        dto = {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'partialnric': self.partialnric,
            'race': self.race,
            'dob': self.dob,
            'mobileno': self.mobileno
        }

        dto['medical_record'] = []
        for oi in self.medical_record:
            dto['medical_record'].append(oi.json())

        return dto

class Medical_Record(db.Model):
    __tablename__ = 'medicalRecord'

    id = db.Column(db.ForeignKey(
        'patient.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, primary_key=True, index=True)
    pDiagnosis = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, nullable=False, primary_key=True, default=datetime.now)

    patient = db.relationship(
        'Patient', primaryjoin='Medical_Record.id == Patient.id', backref='medical_record', 
    )

    def json(self):
        dto = {
            'pDiagnosis': self.pDiagnosis, 
            'created': self.created
        }

        return dto
    

@app.route("/patient")
def get_all():
    patientlist = Patient.query.all()
    if len(patientlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "patients": [patient.json() for patient in patientlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no patients."
        }
    ), 404

@app.route("/patient/<int:id>")
def find_by_id(id):
    patient = Patient.query.filter_by(id=id).first()
    if patient:
        return jsonify(
            {
                "code": 200,
                "data": patient.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Patient not found."
        }
    ), 404


@app.route("/patient/<int:id>", methods=['POST'])
def create_patient(id):
    if (Patient.query.filter_by(id=id).all()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Patient already exists."
            }
        ), 400

    data = request.get_json()
    patient = Patient(id, **data)

    try:
        db.session.add(patient)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred creating the patient."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": patient.json()
        }
    ), 201

@app.route("/patient/<int:id>/medicalRecords", methods=['POST'])
def create_medRec(id):

    pDiagnosis = request.json.get('pDiagnosis', None)
    medRec = Medical_Record(id=id, pDiagnosis=pDiagnosis)

    try:
        db.session.add(medRec)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred creating the Medical Records. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "message": "Medical records successfully added!"
        }
    ), 201


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5500, debug=True)