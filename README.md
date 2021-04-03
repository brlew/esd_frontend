# esd_frontend

## Setup instructions

### Database
For Windows :
1.  Start WAMP server.

2.  Go to phpMyAdmin (http://localhost/phpmyadmin/index.php) and log in.
    Username: root
    Password: 

3.  Import the sql statements in the following order.
    - g1t6_patient
    - g1t6_doctor
    - g1t6_appt
    - g1t6_prescription
    - g1t6_logincred

pharmacist: 5600
- patient ms
- prescription ms

### Postman
4.  Open Postman App and import `ESD_G9T2.postman_collection.json`.
    Run the requests to test the endpoints.

### Docker
5.  docker-compose
    ```
    cd esd_frontend
    docker-compose up -d
    docker images
    ```

6.  When 'docker images' is run, you should see the following images with tag `g1t6`.
    - borenlew/bookingappt
    - borenlew/prescription
    - borenlew/doctor
    - borenlew/patient
    - borenlew/appt

