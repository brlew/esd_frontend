from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import datetime

app = Flask(__name__)
CORS(app)

#prescription_URL = "http://localhost:5000/prescription"
appt_URL = "http://localhost:5100/appt/"
doctor_URL = "http://localhost:5200/doctor/"

# To Run
# python bookingappt.py 
# docker build -t borenlew/bookingappt:g1t6_v2 ./
# docker run -p 5400:5000 borenlew/bookingappt:g1t6_v2

@app.route("/bookingappt/", methods=['POST'])
def bookingappt():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            apptRequest = request.get_json()
            print("\nReceived an appointment in JSON:", apptRequest)

            # do the actual work
            # 1. Send order info {cart items}
            result = processBookAppt(apptRequest)
            print('\n------------------------')
            print('result: ', result)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "bookingappt.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processBookAppt(apptRequest):
    print('\n-----Invoking processBookAppt microservice-----')
    apptRequest_result = invoke_http(appt_URL, method='POST', json=apptRequest)
    print('apptRequest_result:', apptRequest_result)

    code = apptRequest_result["code"]

    
    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Fail to process booking"
        }

    return {
        "code": 201,
        "message": "Successfully added booking"
        }



@app.route("/bookingappt/", methods=['GET'])
def getBookingAvail():
    result = findDoctorAvailability()
    print('\n------------------------')
    print('result: ', result)
    return jsonify(result), result["code"]


def findDoctorAvailability():
    print('\n-----Invoking doctor microservice-----')
    doctoravail_result = invoke_http(doctor_URL, method='GET')
    # dID = doctoravail_result['dID']
    # timeSlot = doctoravail_result['timeSlot']
    # bookingStatus = doctoravail_result['bookingStatus']

    print('doctoravail_result:', doctoravail_result)

    code = doctoravail_result["code"]
    # code = 200

    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Doctor is not available at this time slot findDoctorAvailability"
        }

    return {
        "code": 201,
        "data": {
            "doctoravail_result" : doctoravail_result
            },
        "message": "Successfully retrieved doctor's availability"
        }


# Get by doctor by departments
@app.route("/bookingappt/dpt/<departments>", methods=['GET'])
def getBookingAvail2(departments):
    result = findDoctorAvailabilityByDpt(departments)
    print('\n------------------------')
    print('result: ', result)
    return jsonify(result), result["code"]


def findDoctorAvailabilityByDpt(dptArg):
    print('\n-----Invoking doctor microservice get via dpt-----')
    dpt_URL = doctor_URL + "/dpt/" + dptArg
    doctoravail_result = invoke_http(dpt_URL, method='GET')
    # dID = doctoravail_result['dID']
    # timeSlot = doctoravail_result['timeSlot']
    # bookingStatus = doctoravail_result['bookingStatus']

    print('doctoravail_result:', doctoravail_result)

    code = doctoravail_result["code"]

    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Doctor is not available at this time slot"
        }

    return {
        "code": 201,
        "data": {
            "doctoravail_result" : doctoravail_result
            },
        "message": "Successfully retrieved doctor's availability"
        }

# Delete Doctor Time Slot

@app.route("/bookingappt/statuschange/<timeSlotID>", methods=['POST'])
def removetimeSlotID(timeSlotID):
    result = findTimeSlotIDtoStatus(timeSlotID)
    getTimeSlot = result['data']['doctoravail_result']['data']['timeSlot']
    getTimeSlot = getTimeSlot[:-4]
    print(getTimeSlot)
    getCleanTimeSlot = datetime.datetime.strptime(getTimeSlot, '%a, %d %b %Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    #print("THIS IS THE RESULT: ")
    #print(result['data']['doctoravail_result']['data']['timeSlot'])
    #alert(getDateTime)
    addTimeSlotIDtoPatientAppt(timeSlotID, getCleanTimeSlot)
    print('\n------------------------')
    print('result: ', result)
    return jsonify(result), result["code"]

def findTimeSlotIDtoStatus(timeSlotIDArg):
    print('\n-----Invoking doctor microservice get via timeSlotID to change bookingstatus to Unavailable-----')
    rts_URL = doctor_URL + "/statuschange/" + timeSlotIDArg
    doctoravail_result = invoke_http(rts_URL, method='PUT', json={"timeSlotID": timeSlotIDArg, "bookingStatus": "Unavailable"})

    print('doctoravail_result:', doctoravail_result)

    code = doctoravail_result["code"]

    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Doctor is not available at this time slot"
        }

    return {
        "code": 201,
        "data": {
            "doctoravail_result" : doctoravail_result
            },
        "message": "Successfully deleted Doctor's Timeslot"
        }


# def findTimeSlotIDtoDel(timeSlotIDArg):
#     print('\n-----Invoking doctor microservice get via timeSlotID to delete-----')
#     rts_URL = doctor_URL + "/removets/" + timeSlotIDArg
#     doctoravail_result = invoke_http(rts_URL, method='GET')

#     print('doctoravail_result:', doctoravail_result)

#     code = doctoravail_result["code"]

#     if code not in range(200, 300):
#         return {
#             "code": 400,
#             "message": "Doctor is not available at this time slot"
#         }

#     return {
#         "code": 201,
#         "data": {
#             "doctoravail_result" : doctoravail_result
#             },
#         "message": "Successfully deleted Doctor's Timeslot"
#         }



def addTimeSlotIDtoPatientAppt(timeSlotIDArg, timeSlotDetails):
    print('\n-----Invoking appt microservice add timeSlotID via POST-----')
    addTS_URL = appt_URL
    add_appt_result = invoke_http(addTS_URL, method='POST', json={"pID":1,"dID":1,"timeSlotID":timeSlotIDArg,"apptDateTime": timeSlotDetails})

    print('add_appt_result:', add_appt_result)

    code = add_appt_result["code"]

    if code not in range(200, 300):
        return {
            "code": 400,
            "message": "Appt add failure"
        }

    return {
        "code": 201,
        "data": {
            "add_appt_result" : add_appt_result
            },
        "message": "Successfully add Timeslot into patient account"
        }



# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for process an appointment...")
    app.run(host="0.0.0.0", port=5400, debug=True)
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
