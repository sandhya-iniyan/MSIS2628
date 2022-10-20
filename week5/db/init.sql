DROP TABLE IF EXISTS Meal;

CREATE TABLE IF NOT EXISTS Meal (
    MealId SERIAL PRIMARY KEY, 
    MealName TEXT NOT NULL,
    MealPrice DECIMAL(6,2) NOT NULL
);

INSERT INTO Meal(MealName, MealPrice) VALUES ('Mionetto Prosecco Brut, Treviso, Veneto, Italy NV', 12.50);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Mumm Brut Rosé, Napa Valley, California NV', 16.50);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Taittinger ''La Francaise'' Brut, Reims, Champagne NV', 22.00);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Terlan Pinot Grigio, Alto Adige, Italy 2021', 14.00);
INSERT INTO Meal(MealName, MealPrice) VALUES ('C. Smith Riesling ''Kung Fu Girl'', Columbia Valley, WA 2020', 12.00);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Onx Sauvignon Blanc ''Field Day'', Templeton Gap, CA 2020', 13.00);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Left Coast Cellars White Pinot Noir, Willamette Valley, OR 2020', 14.50);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Licia Albariño, Rías Baixas, Spain 2021', 12.50);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Groth Vineyards Sauvignon Blanc, Napa Valley, California 2021', 15.50);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Craggy Range Sauvignon Blanc Te Muna Rd, Martinborough, NZ 2021', 14.00);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Sean Minor Chardonnay, Sonoma Coast, CA 2019', 12.50);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Garnier & Fils Chardonnay, Petit Chablis, Chablis, France 2020', 16.00);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Truchard Vineyards Chardonnay, Carneros, CA 2020', 17.00);
INSERT INTO Meal(MealName, MealPrice) VALUES ('Jordan Chardonnay, Russian River, Sonoma, California 2019', 19.00);
INSERT INTO Meal(MealName, MealPrice) VALUES ('The Beach by Whispering Angel, Aix-en-Provence, France 2021', 12.50);