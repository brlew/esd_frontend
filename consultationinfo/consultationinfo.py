from flask import Flask, request, jsonify
from flask_cors import CORS

import os
from os import environ

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

doctAppt_URL = environ.get('doctAppt_URL') or "http://localhost:5100/appt/"
patient_URL = environ.get('patient_URL') or "http://localhost:5500/patient"
prescription_URL = environ.get('prescription_URL') or "http://localhost:5300/prescription"
# docker run -p 5600:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306 jthm/insert_consultdetails:g1t6

@app.route("/consultDetails/doctor/appt/<string:did>", methods=['GET'])
def getAllApptByDoctorID(did):
    result = viewAllAppt(did)
    print('\n------------------------')
    print('result: ', result)
    return jsonify(result), result["code"]

def viewAllAppt(did):
    print('\n-----Invoking Appointment microservice-----')
    doctorAppt_result = invoke_http(doctAppt_URL + did, method='GET')

    print('doctorAppt_result:', doctorAppt_result)

    code = doctorAppt_result["code"]

    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Doctor got no Appointment."
        }

    return {
        "code": 201,
        "data": {
            "doctorAppt_result" : doctorAppt_result
            },
        "message": "Successfully retrieved doctor's appointment"
        }


@app.route("/consultDetails", methods=['GET'])
def getAllPatientMedRec():
    result = viewAllPatientMedRec()
    print('\n------------------------')
    print('result: ', result)
    return jsonify(result), result["code"]

def viewAllPatientMedRec():
    print('\n-----Invoking patient microservice-----')
    patientMedRec_result = invoke_http(patient_URL, method='GET')

    print('patientMedRec_result:', patientMedRec_result)

    code = patientMedRec_result["code"]

    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Patient got no medical Records."
        }

    return {
        "code": 201,
        "data": {
            "patientMedRec_result" : patientMedRec_result
            },
        "message": "Successfully retrieved patient's medical records"
        }


@app.route("/consultDetails/<string:pid>", methods=['GET'])
def getPatientMedRec(pid):
    result = viewPatientMedRec(pid)
    print('\n------------------------')
    print('result: ', result)
    return jsonify(result), result["code"]

def viewPatientMedRec(pid):
    print('\n-----Invoking patient microservice-----')
    patientMedRec_result = invoke_http(patient_URL + "/" + pid, method='GET')

    print('patientMedRec_result:', patientMedRec_result)

    code = patientMedRec_result["code"]

    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Patient got no medical Records."
        }

    return {
        "code": 201,
        "data": {
            "patientMedRec_result" : patientMedRec_result
            },
        "message": "Successfully retrieved patient's medical records"
        }

@app.route("/consultDetails/prescription", methods=['GET'])
def getAllPatientPrescription():
    result = viewAllPatientPrescription()
    print('\n------------------------')
    print('result: ', result)
    return jsonify(result), result["code"]

def viewAllPatientPrescription():
    print('\n-----Invoking prescription microservice-----')
    patientPrescription_result = invoke_http(prescription_URL, method='GET')

    print('patientPrescription_result:', patientPrescription_result)

    code = patientPrescription_result["code"]

    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Patient got no prescription."
        }

    return {
        "code": 201,
        "data": {
            "patientPrescription_result" : patientPrescription_result
            },
        "message": "Successfully retrieved patient's prescription"
        }


@app.route("/consultDetails/prescription/<string:pid>", methods=['GET'])
def getPatientPrescription(pid):
    result = viewPatientPrescription(pid)
    print('\n------------------------')
    print('result: ', result)
    return jsonify(result), result["code"]

def viewPatientPrescription(pid):
    print('\n-----Invoking prescription microservice-----')
    patientPrescription_result = invoke_http(prescription_URL + "/" + pid, method='GET')

    print('patientPrescription_result:', patientPrescription_result)

    code = patientPrescription_result["code"]

    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Patient got no prescription."
        }

    return {
        "code": 201,
        "data": {
            "patientPrescription_result" : patientPrescription_result
            },
        "message": "Successfully retrieved patient's prescription"
        }
    
@app.route("/consultDetails/<string:pid>/medicalRecords", methods=['POST'])
def addConsultDetails(pid):
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            consultDetails = request.get_json()
            print("\nReceived an consultDetails in JSON:", consultDetails)
            # medRec = data.MedicalRecords
            # prescription = data.Prescription

            # do the actual work
            # 1. Send order info {cart items}
            result = processConsultDetails(consultDetails, pid)
            return jsonify(result), 200

        except Exception as e:
            pass  # do nothing.

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400

def processConsultDetails(consultDetails, pid):
    # 2. Send the order info {cart items}
    # Invoke the order microservice

    print('\n-----Invoking patient microservice-----')
    medRec_result = invoke_http(patient_URL + pid + "/" + "medicalRecords", method='POST', json=consultDetails["MedicalRecords"])
    print('medRec_result:', medRec_result)

    # 4. Record new order
    # record the activity log anyway

    print('\n\n-----Invoking prescription microservice-----')
    prescription_result = invoke_http(prescription_URL, method="POST", json=consultDetails["Prescription"])
    print('prescription_result:', prescription_result)
    # - reply from the invocation is not used;
    # continue even if this invocation fails

    # Check the order result; if a failure, send it to the error microservice.
    medRecCode = medRec_result["code"]
    prescriptionCode = prescription_result["code"]
    if medRecCode and prescriptionCode in range(200, 300):

        # Inform the error microservice
        # print("Consult details added successfully!!!!!!")

        # 7. Return error
        return {
            "code": 201,
            "data": {
                "medRec_result": medRec_result,
                "prescription_result": prescription_result
                },
            "message": "Consult details added successfully!!!!!!"
        }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " processing consultation info")
    app.run(host="0.0.0.0", port=5600, debug=True)
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
