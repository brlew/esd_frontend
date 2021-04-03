from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/g1t6_prescription'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/prescription'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TO RUN SERVICE
# docker run -p 5400:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/g1t6_prescription jthm/prescription:g1t6
 
db = SQLAlchemy(app)
 
class Prescription(db.Model):
    __tablename__ = 'prescription'
 
    prescriptionID = db.Column(db.Integer(), primary_key=True)
    medName = db.Column(db.String(25), nullable=False)
    dosage = db.Column(db.String(20), nullable=False)
    pID = db.Column(db.Integer(), nullable=False)
    aID = db.Column(db.Integer(), nullable=False)
 
    def json(self):
        dto = {
            "prescriptionID": self.prescriptionID, 
            "medName": self.medName, 
            "dosage": self.dosage,
            "pID": self.pID, 
            "aID": self.aID
        }

        return dto
        
@app.route("/prescription")
def get_all():
	# pass
    prescriptionlist = Prescription.query.all()
    if len(prescriptionlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "prescriptions": [prescription.json() for prescription in prescriptionlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "prescription not found."
        }
    ), 40
 
@app.route("/prescription/<string:pID>")
def find_by_pID(pID):
	# pass
    prescriptionlist = Prescription.query.filter_by(pID=pID).all()
    if prescriptionlist:
        return jsonify(
            {
                "code": 200,
                "data": [prescription.json() for prescription in prescriptionlist]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Prescription not found."
        }
    ), 404


@app.route("/prescription", methods=['POST'])
def create_prescription():

    medName = request.json.get('medName', None)
    dosage = request.json.get('dosage', None)
    pID = request.json.get('pID', None)
    aID = request.json.get('aID', None)

    prescription = Prescription(medName=medName, dosage=dosage, pID=pID, aID=aID)

    try:
        db.session.add(prescription)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the prescription. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": prescription.json()
        }
    ), 201

        
 
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5300, debug=True)
