# SeekHealth 
SeekHealth is our effort to allow healthcare providers to aggregate thousands of appointments and consultation information. The SeekHealth API allows healthcare providers to bring features for both their internal and external users.

## 0. Direct Links to Resources
    * [ ] ( ).


## 1. Prerequisites
### 1.1 Installation
Please ensure that you have the following installed on your machine. You can follow [this installation guide](https://docs.google.com/document/d/1hSqhVbgbclf-eOvBx5BQhaTJHxbUSUN4wZTrLNUMyUk/edit#heading=h.3l1qt71ezfd0).
    * Python 3
    * Visual Studio Code
    * Docker Desktop
    * WAMP Server

### 1.2 Launch
Make sure that your WAMP Server and Docker is running.
Please ensure that the default port of MYSQL is 3306. Change the port number by Right Click WAMP Icon -> Tools-> under port use by MySQL-> use a port Other than XXXX. WAMP will be restarted.

## 2. Database
For Windows :
1.  Start WAMP server.

2.  Go to [phpMyAdmin](http://localhost/phpmyadmin/index.php) and log in.
    Username: root
    Password: 

3.  Import the sql statements in the following order. [under the database folder](./tree/main/database)
    - g1t6_patient
    - g1t6_doctor
    - g1t6_appt (if values are not added, please copy the SQL statements from database/appt.sql folders)
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
