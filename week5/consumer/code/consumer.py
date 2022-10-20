#import urllib.request
from flask import Flask, render_template
import json
import os
import requests

app = Flask(__name__)


@app.route('/')
def show_meal():

    url = 'http://{host}:{port}'.format(host=os.environ.get('API_HOST'),
                                        port=os.environ.get('API_PORT'))
    response = requests.get(url)
    data = response.json()
    meal = data['Meal']
    price = data['Price']
    return render_template('index.html', meal=meal, price=price)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('CONSUMER_PORT'))