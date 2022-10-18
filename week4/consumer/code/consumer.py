#import urllib.request
from flask import Flask, render_template
import json
import os
import requests

app = Flask(__name__)


@app.route('/')
def show_meal():
    
    url = os.environ.get("API_ENDPOINT")
    response = requests.get(url)
    data = response.content
    meal = data[0]
    price = data[1]   
    return render_template('index.html', meal=meal, price=price)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("CONSUMER_PORT"))