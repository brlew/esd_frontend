from invokes import invoke_http

# invoke book microservice to get all books
results = invoke_http("http://localhost:5100/appt", method='GET')

print( type(results) )
print()
print( results )

# invoke book microservice to create a book
# apptID = '2'
# pID = '3'
# apptDateTime = '2021-01-27 03:50:55'
apptDetails = { "pID": 1, "dID": 2, "apptDateTime": "2021-01-27 03:50:55", "apptStatus": 'pending'}
create_results = invoke_http(
        "http://localhost:5100/appt/", method='POST', 
        json=apptDetails
    )

print()
print( create_results )
