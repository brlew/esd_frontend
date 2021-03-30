from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

# from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/g1t6_doctor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TO RUN SERVICE
# docker run -p 5200:5000 -e dbURL=mysql+mysqlconnector://root@host.docker.internal:3306/g1t6_doctor borenlew/doctor:g1t6_v1

db = SQLAlchemy(app)

class Doctor(db.Model):
    __tablename__ = 'doctor'

    dID = db.Column(db.Integer(), nullable=False, primary_key=True)
    dName = db.Column(db.String(50), nullable=False)
    dDepartment = db.Column(db.String(50), nullable=False)
    dRoom = db.Column(db.String(50), nullable=False)

    def json(self):
        dto = {
            'dID': self.dID,
            'dName': self.dName,
            'dDepartment': self.dDepartment,
            'dRoom': self.dRoom
        }

        dto['doct_Availability'] = []
        for oi in self.apptAvailability:
            dto['doct_Availability'].append(oi.json())

        return dto

    # def __init__(self, dID, dName, dDepartment, dRoom):
    #     self.dID = dID
    #     self.dName = dName
    #     self.dDepartment = dDepartment
    #     self.dRoom = dRoom

    # def json(self):
    #     return {"dID": self.dID, "dName": self.dName, "dDepartment": self.dDepartment, "dRoom": self.dRoom}

class Appt_Availability(db.Model):
    __tablename__ = 'doctorAvail'

    dID = db.Column(db.ForeignKey(
        'doctor.dID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, primary_key=True, index=True)
    timeSlot = db.Column(db.DateTime, primary_key=True)
    bookingStatus = db.Column(db.String(32), nullable=False)
    timeSlotID = db.Column(db.Integer(), primary_key=True)

    # order_id = db.Column(db.String(36), db.ForeignKey('order.order_id'), nullable=False)
    # order = db.relationship('Order', backref='order_item')
    doctor = db.relationship(
        'Doctor', primaryjoin='Appt_Availability.dID == Doctor.dID', backref='apptAvailability')

    def json(self):
        return {'dID': self.dID, 'timeSlot': self.timeSlot, 'bookingStatus': self.bookingStatus, 'timeSlotID': self.timeSlotID}


@app.route("/doctor/")
def get_all():
    doclist = Doctor.query.all()
    if len(doclist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "doctors": [doc.json() for doc in doclist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no doctors."
        }
    ), 404


@app.route("/doctor/<int:dID>/")
def find_by_apptID(dID):
    doctor = Doctor.query.filter_by(dID=dID).first()
    if doctor:
        return jsonify(
            {
                "code": 200,
                "data": doctor.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": f"Doctor ID {dID} not found."
        }
    ), 404

@app.route("/doctor/dpt/<string:dDepartment>/")
def find_by_department(dDepartment):
    doclistdpt = Doctor.query.filter_by(dDepartment=dDepartment).all()
    if len(doclistdpt):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "doctors": [doc.json() for doc in doclistdpt]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no doctors."
        }
    ), 404

# Delete TimeSlot from doct_avail, never use until

@app.route("/doctor/removets/<int:timeSlotID>/")
def find_by_timeSlotID(timeSlotID):
    apptAvail = Appt_Availability.query.filter_by(timeSlotID=timeSlotID).first()
    if apptAvail:
        db.session.delete(apptAvail)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": apptAvail.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": f"Timeslot ID {timeSlotID} not found."
        }
    ), 404

# change bookingstatus
@app.route("/doctor/statuschange/<int:timeSlotID>", methods=['PUT'])
def update_appt(timeSlotID):
    try:
        apptGetTID = Appt_Availability.query.filter_by(timeSlotID=timeSlotID).first()
        if not apptGetTID:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "timeSlotID": timeSlotID
                    },
                    "message": "timeSlotID not found."
                }
            ), 404

        # update status
        data = request.get_json(force=True)
        print("data is " + format(data), request.is_json)

        # if data['dID']:
        #     apptGetTID.dID = data['dID']
        if data['timeSlotID']:
            apptGetTID.timeSlotID = data['timeSlotID']
        # if data['timeSlot']:
        #     apptGetTID.timeSlot = data['timeSlot']
        if data['bookingStatus']:
            apptGetTID.bookingStatus = data['bookingStatus']
            
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": apptGetTID.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "timeSlotID": timeSlotID
                },
                "message": "An error occurred while updating the appointment. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)