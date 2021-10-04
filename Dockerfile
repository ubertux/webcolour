FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3-pip  && pip3 install flask
COPY .  /opt
WORKDIR /opt
EXPOSE 8080
ENTRYPOINT python3 /opt/app.py
