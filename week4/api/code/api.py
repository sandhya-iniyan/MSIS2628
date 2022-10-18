from flask import Flask
import random
import json
import os

app = Flask(__name__)


@app.route('/')
def recommend_meal():
    menu = {
        "Mionetto Prosecco Brut, Treviso, Veneto, Italy NV": "12.50",
        "Mumm Brut Rosé, Napa Valley, California NV": "16.50",
        "Taittinger 'La Francaise' Brut, Reims, Champagne NV": "22.00",
        "Terlan Pinot Grigio, Alto Adige, Italy 2021": "14.00",
        "C. Smith Riesling 'Kung Fu Girl', Columbia Valley, WA 2020": "12.00",
        "Onx Sauvignon Blanc 'Field Day', Templeton Gap, CA 2020": "13.00",
        "Left Coast Cellars White Pinot Noir, Willamette Valley, OR 2020":
        "14.50",
        "Licia Albariño, Rías Baixas, Spain 2021": "12.50",
        "Groth Vineyards Sauvignon Blanc, Napa Valley, California 2021":
        "15.50",
        "Craggy Range Sauvignon Blanc Te Muna Rd, Martinborough, NZ 2021":
        "14.00",
        "Sean Minor Chardonnay, Sonoma Coast, CA 2019": "12.50",
        "Garnier & Fils Chardonnay, Petit Chablis, Chablis, France 2020":
        "16.00",
        "Truchard Vineyards Chardonnay, Carneros, CA 2020": "17.00",
        "Jordan Chardonnay, Russian River, Sonoma, California 2019": "19.00",
        "The Beach by Whispering Angel, Aix-en-Provence, France 2021": "12.50",
    }

    meal, price = random.choice(list(menu.items()))
    recommendation = {"Meal": meal, "Price": price}
    return json.dumps(recommendation)


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5111))
    app.run(debug=True, host='0.0.0.0', port=5000)