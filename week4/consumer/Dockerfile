FROM python:3.10.7

VOLUME /app
WORKDIR /app

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

EXPOSE 80
CMD [ "python", "consumer.py" ]