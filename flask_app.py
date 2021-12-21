from flask import Flask, render_template, request

from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')

mydb = client["covid"]
mycol = mydb["covid_db"]


@app.route('/', methods=['GET'])
def index():
    return (render_template('index.html'))


@app.route('/', methods=['POST'])
def result():
    country1 = request.form['country1']
    country2 = request.form['country2']
    country3 = request.form['country3']
    print(country1, country2, country3)

    casesCountry1 = getCases(country1)
    casesCountry2 = getCases(country2)
    casesCountry3 = getCases(country3)
    print(casesCountry1)

    deathsCountry1 = getDeaths(country1)
    deathsCountry2 = getDeaths(country2)
    deathsCountry3 = getDeaths(country3)
    print(deathsCountry1)

    dateLabels = getDates(country1)
    print(dateLabels)

    return (render_template('index.html', country1=country1, country2=country2, country3=country3,
                            casesCountry1=casesCountry1, casesCountry2=casesCountry2, casesCountry3=casesCountry3,
                            deathsCountry1=deathsCountry1, deathsCountry2=deathsCountry2, deathsCountry3=deathsCountry3,
                            dateLabels=dateLabels))


def getCases(country):
    with open(client):
        caseList = []
        for record in client['records']:
            if record['countryterritoryCode'] == country:
                caseList.append(int(record['cases']))
    return (list(reversed(caseList)))


def getDeaths(country):
    with open(client):
        deathsList = []
        for record in client['records']:
            if record['countryterritoryCode'] == country:
                deathsList.append(int(record['deaths']))
    return (list(reversed(deathsList)))


def getDates(country):
    with open(client):
        dateRepList = []
        for record in client['records']:
            if record['countryterritoryCode'] == country:
                dateRepList.append(record['dateRep'])
    return (list(reversed(dateRepList)))


# Ici, le module est exécuté en tant que programme principal : les instructions qui suivent sont donc exécutées.
# Dans le cas où ce module est importé dans un autre programme, cette partie du code est sans effet.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
