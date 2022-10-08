FROM python

VOLUME /app
WORKDIR /app

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

EXPOSE 8000