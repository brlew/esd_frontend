from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/g1t6_prescription'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/prescription'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TO RUN SERVICE
# docker run -p 5003:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/prescriptiondb jthm/prescription:g1t6
# docker run -p 5300:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/g1t6_prescription borenlew/prescription:g1t6_v2
 
db = SQLAlchemy(app)
 
class Prescription(db.Model):
    __tablename__ = 'prescription'
 
    prescriptionID = db.Column(db.Integer(), primary_key=True)
    medName = db.Column(db.String(25), nullable=False)
    medDescription = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(20), nullable=False)
    medCode = db.Column(db.String(8), nullable=False)
    pID = db.Column(db.Integer(), nullable=False)
    aID = db.Column(db.Integer(), nullable=False)
 
    # def __init__(self, medCode, medName, medDescription, qty, pID, aID):
    #     self.medCode = medCode
    #     self.medName = medName
    #     self.medDescription = medDescription
    #     self.qty = qty
    #     self.pID = pID
    #     self.aID = aID
 
    def json(self):
        dto = {
            "prescriptionID": self.prescriptionID, 
            "medName": self.medName, 
            "medDescription": self.medDescription, 
            "dosage": self.dosage, 
            "medCode": self.medCode,
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
 
@app.route("/prescription/<string:pID>/<string:aID>")
def find_by_pID(pID,aID):
	# pass
    prescriptionlist = Prescription.query.filter_by(pID=pID, aID=aID).all()
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

    # data = request.get_json()
    # print(data)
    
    medName = request.json.get('medName', None)
    medDescription = request.json.get('medDescription', None)
    dosage = request.json.get('dosage', None)
    medCode = request.json.get('medCode', None)
    pID = request.json.get('pID', None)
    aID = request.json.get('aID', None)

    prescription = Prescription(medName=medName, medDescription=medDescription, dosage=dosage, medCode=medCode, pID=pID, aID=aID)

    try:
        db.session.add(prescription)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                # "data": {
                #     "apptID": apptID
                # },
                "message": "An error occurred creating the prescription. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": prescription.json()
        }
    ), 201


 
# @app.route("/prescription/<integer:pID>", methods=['POST'])
# def create_book(isbn13):
#     	# pass
#     if (Book.query.filter_by(isbn13=isbn13).first()):
#         return jsonify(
#             {
#                 "code": 400,
#                 "data": {
#                     "isbn13": isbn13
#                 },
#                 "message": "Book already exists."
#             }
#         ), 400
 
#     data = request.get_json()
#     book = Book(isbn13, **data)
 
#     try:
#         db.session.add(book)
#         db.session.commit()
#     except:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "isbn13": isbn13
#                 },
#                 "message": "An error occurred creating the book."
#             }
#         ), 500
 
#     return jsonify(
#         {
#             "code": 201,
#             "data": book.json()
#         }
#           ), 201
    
        
 
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)
