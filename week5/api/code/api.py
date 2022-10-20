from flask import Flask
import random
import json
import os
#import psycopg2
app = Flask(__name__)
import psycopg2


@app.route('/')
def recommend_meal():
    conn = psycopg2.connect(database=os.environ.get('POSTGRES_USER'),
                            user=os.environ.get('POSTGRES_USER'),
                            password=os.environ.get('POSTGRES_PASSWORD'),
                            host=os.environ.get('DB_HOST'),
                            port=os.environ.get('DB_PORT'))

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #Retrieving data
    cursor.execute(
        '''SELECT mealName, mealPrice FROM Meal ORDER BY random() limit 1;''')
    #Fetching 1st row from the table
    result = cursor.fetchall()
    conn.close()
    recommendation = {"Meal": result[0][0], "Price": str(result[0][1])}
    return json.dumps(recommendation)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("API_PORT"))