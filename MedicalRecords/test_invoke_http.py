# test_invoke_http.py
from invokes import invoke_http

# invoke prescription microservice to get all prescription
results = invoke_http("http://localhost:5002/patient/1", method='GET')

print( type(results) )
print()
print( results )

# invoke book microservice to create a book
prescription_details = { "medName": "amoxicillin", "medDescription": "Antibiotic used to treat a number of bacterial infections", "dosage": "300mg", "medCode": "ABCDE", "pID": 2, "aID": 1 }
create_results = invoke_http(
        "http://localhost:5003/prescription", method='POST', 
        json=prescription_details
    )

print()
print( create_results )