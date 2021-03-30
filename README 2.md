# IS213 ESD_G9T6 - SeekHealth Website

## 

### Docker Commands
1. [Clean Up] STOP and REMOVE all docker containers 
```
    docker ps
    FOR /f "tokens=*" %i IN ('docker ps -q') DO docker stop %i
    docker ps -a
    FOR /f "tokens=*" %i IN ('docker container ls –aq') DO docker rm %i
```

### Microservices
REP: repository
MS: microservice

```
docker pull <REP>/<MS>:g1t6
```
- appointment: veronicateng13/appt:g1t6
- doctor: veronicateng13/doctor:g1t6
- patient: borenlew/patient:g1t6

- insert_medical_record:
- book_an_appt:


```
docker run -p <PORT>:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/medical_enterprise_sol veronicateng13/<MS>:g1t6
```
- appt: PORT 5100
- doctor: PORT 5200
- bookingappt: PORT 5400


### Setup instructions
For Windows :
1.  Start WAMP server.

2.  Go to phpMyAdmin (http://localhost/phpmyadmin/index.php) and log in.
    Username: root
    Password: 

3.  Import medical.sql into phpMyAdmin.You will see the following tables in your schema.
    - appointment
    - apptavailability
    - doctor
    - medicalrecords
    - patient
    - prescription

### Docker
5.  In VS Code terminal, pull the docker image from Docker Hub and run it.
    (https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html)
    ```
    cd appt
    # docker build -t veronicateng13/appt:g1t6 ./
    docker pull veronicateng13/appt:g1doct6
    docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/medical_enterprise_sol veronicateng13/appt:g1t6
    ```

### Postman
6.  Open Postman App and import `ESD_G9T2.postman_collection.json`.
    Run the requests to test the endpoints.


## Others, for my reference
2. Run Docker server 
   where <host port>:<container port>
    ```
    netstat -aon | findstr :5000
    docker run -p 5001:5000 veronicateng13/appt:1.0
    ```