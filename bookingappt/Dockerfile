FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY ./invokes.py .
RUN pip install --no-cache-dir -r requirements.txt 
RUN python -m pip install requests
RUN python -m pip install flask_cors
COPY ./bookingappt.py .
CMD [ "python", "./bookingappt.py"]