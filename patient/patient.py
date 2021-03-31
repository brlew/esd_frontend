from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import environ

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/patient'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TO RUN SERVICE
# docker run -p 5002:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/patient jthm/patient:g1t6

# TO RUN SERVICE
# docker build -t borenlew/patient:g1t6_v2 ./
# docker run -p 5500:5000 -e dbURL=mysql+mysqlconnector://root@host.docker.internal:3306/g1t6_patient borenlew/patient:g1t6_v2

db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'patient'

    pid = db.Column(db.Integer, primary_key=True)
    pName = db.Column(db.Integer, nullable=False)
    pAge = db.Column(db.Integer, nullable=False)
    pNumber = db.Column(db.Integer, nullable=False)
    pAddress = db.Column(db.String(100), nullable=False)
    allergies = db.Column(db.String(100), nullable=True)

    def json(self):
        dto = {
            'pid': self.pid,
            'pName': self.pName,
            'pAge': self.pAge,
            'pNumber': self.pNumber,
            'pAddress': self.pAddress,
            'allergies': self.allergies
        }

        dto['medical_record'] = []
        for oi in self.medical_record:
            dto['medical_record'].append(oi.json())

        return dto

class Medical_Record(db.Model):
    __tablename__ = 'medicalRecord'

    pid = db.Column(db.ForeignKey(
        'patient.pid', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, primary_key=True, index=True)
    pDiagnosis = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, nullable=False, primary_key=True, default=datetime.now)

    patient = db.relationship(
        'Patient', primaryjoin='Medical_Record.pid == Patient.pid', backref='medical_record', 
    )

    def json(self):
        return {'pDiagnosis': self.pDiagnosis, 'created': self.created}
    

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

@app.route("/patient/<int:pid>")
def find_by_pid(pid):
    patient = Patient.query.filter_by(pid=pid).first()
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


@app.route("/patient/<int:pid>", methods=['POST'])
def create_patient(pid):
    if (Patient.query.filter_by(pid=pid).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "pid": pid
                },
                "message": "Patient already exists."
            }
        ), 400

    data = request.get_json()
    patient = Patient(pid, **data)

    try:
        db.session.add(patient)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "pid": pid
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

@app.route("/patient/<int:pid>/medicalRecords", methods=['POST'])
def create_medRec(pid):

    pDiagnosis = request.json.get('pDiagnosis', None)
    medRec = Medical_Record(pid=pid, pDiagnosis=pDiagnosis)

    try:
        db.session.add(medRec)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "pid": pid
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