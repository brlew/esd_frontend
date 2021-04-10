# esd_frontend

## Setup instructions
###
- have WAMP running
- have Docker running


### Database
For Windows :
1.  Start WAMP server.

2.  Go to phpMyAdmin (http://localhost/phpmyadmin/index.php) and log in.
    Username: root
    Password: 

3.  Import the sql statements in the following order.
    - g1t6_patient
    - g1t6_doctor
    - g1t6_appt (don't show the appts)
    - g1t6_prescription
    - g1t6_employee


### Postman
4.  Open Postman App and import `ESD_G9T2.postman_collection.json`.
    Run the requests to test the endpoints.

### Docker
5.  Build the docker images.
    ```
    cd esd_frontend
    docker-compose up -d
    docker images
    ```

6.  When 'docker images' is run, you should see the following images with tag `g1t6`.
    - veronicateng13/activity_log
    - jthm/patient
    - jthm/consultationinfo
    - jthm/prescription
    - jthm/appt
    - borenlew/bookingappt
    - borenlew/doctor
    - rabbitmq

### Login Portal
7.  Patient Login. Access through http://localhost:5800/signup.
    ```
    cd esd_frontend/finish
    python patientlogin.py
    ```

    QR code. Access through http://localhost:3002.
    ```
    cd singpass/sg-verify-demo-app
    npm install
    npm start
    ```

8. Employee Login. Access through ?.
    ```
    cd esd_frontend/finish
    python employeelogin.py
    ```


### Others
pharmacist: 5600
- patient ms
- prescription ms
