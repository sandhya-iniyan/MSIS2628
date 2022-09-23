FROM python:3.7.14
RUN apt-get update && apt-get install wget

# WORKDIR is the fold created in the container, not the local directory

RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv

COPY . .
RUN ["python", "./main.py"]