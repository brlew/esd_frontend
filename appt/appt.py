from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://is213@localhost:3306/g1t6_appt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TO RUN SERVICE
# docker run -p 5100:5000 -e dbURL=mysql+mysqlconnector://root@host.docker.internal:3306/g1t6_appt veronicateng13/appt:g9t6

# docker build -t borenlew/appt:g1t6_v2 ./
# docker run -p 5100:5000 -e dbURL=mysql+mysqlconnector://root@host.docker.internal:3306/g1t6_appt borenlew/appt:g1t6_v2


db = SQLAlchemy(app)

class Appt(db.Model):
    __tablename__ = 'appt'

    apptID = db.Column(db.Integer, nullable=False, primary_key=True)
    pID = db.Column(db.Integer, nullable=False)
    dID = db.Column(db.Integer, nullable=False)
    apptDateTime = db.Column(db.DateTime, nullable=False)
    apptStatus = db.Column(db.String(10), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    modified = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    timeSlotID = db.Column(db.Integer())

    def json(self):
        dto = {
            "apptID": self.apptID, 
            "pID": self.pID, 
            "dID": self.dID, 
            "apptDateTime": self.apptDateTime, 
            "apptStatus": self.apptStatus, 
            "created": self.created, 
            "modified": self.modified,
            "timeSlotID": self.timeSlotID
        }

        return dto

@app.route("/appt/")
def get_all():
    apptlist = Appt.query.all()
    if len(apptlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "appts": [appt.json() for appt in apptlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no appointments."
        }
    ), 404


@app.route("/appt/<int:apptID>/")
def find_by_apptID(apptID):
    appt = Appt.query.filter_by(apptID=apptID).first()
    if appt:
        return jsonify(
            {
                "code": 200,
                "data": appt.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": f"Appointment ID {apptID} not found."
        }
    ), 404

@app.route("/doctor/appt/<int:dID>/")
def find_by_docID(dID):
    apptlist = Appt.query.filter_by(dID=dID).all()
    if apptlist:
        return jsonify(
            {
                "code": 200,
                "data": [appt.json() for appt in apptlist]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": f"Doctor ID {dID} not found."
        }
    ), 404


@app.route("/appt/", methods=['POST'])
def create_appt():

    # data = request.get_json()
    # print(data)
    pID = request.json.get('pID', None)
    dID = request.json.get('dID', None)
    apptDateTime = request.json.get('apptDateTime', None)
    timeSlotID = request.json.get('timeSlotID', None)
    # apptStatus = request.get_json('apptStatus')

    appt = Appt(pID=pID, dID=dID, apptDateTime=apptDateTime, apptStatus='pending', timeSlotID=timeSlotID)

    try:
        db.session.add(appt)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                # "data": {
                #     "apptID": apptID
                # },
                "message": "An error occurred creating the appointment. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": appt.json()
        }
    ), 201

@app.route("/appt/<string:apptID>", methods=['PUT'])
def update_appt(apptID):
    try:
        appt = Appt.query.filter_by(apptID=apptID).first()
        if not appt:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "apptID": apptID
                    },
                    "message": "Appointment not found."
                }
            ), 404

        # update status
        data = request.get_json(force=True)
        print("data is " + format(data), request.is_json)

        if data['dID']:
            appt.dID = data['dID']
        if data['pID']:
            appt.pID = data['pID']
        if data['apptDateTime']:
            appt.apptDateTime = data['apptDateTime']
        if data['apptStatus']:
            appt.apptStatus = data['apptStatus']
            
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": appt.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "apptID": apptID
                },
                "message": "An error occurred while updating the appointment. " + str(e)
            }
        ), 500






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)

