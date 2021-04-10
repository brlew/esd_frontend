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
4.  Open Postman App and import `ESD_G9T2.postman_collection.json`. Run the requests to test the endpoints.
    Alternatively, access SeekHealth's API through https://documenter.getpostman.com/view/12748512/TzCQcnSk#dc506403-f9e6-47c9-8ec7-2a61ce658a0e.
    
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
py files
appt
    - appt.py: appt/appt.py
doctor
    - doctor.py: doctor/doctor.py
employee
    - employeelogin.py: finish/employeelogin.py
patient
    - patient.py: patient/patient.py
    - patientlogin.py: finish/patientlogin.py
prescription
    - prescription.py: prescription/prescription.py


pharmacist: 5600
- patient ms
- prescription ms
