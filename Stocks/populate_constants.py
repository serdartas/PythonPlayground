import requests
from model import Country, City, State, Industry, Sector, Currency, Company, Exchange, session, create_city

def populate_countries():
    response = requests.get('https://restcountries.com/v3.1/all')
    countries = response.json()
    
    for country in countries:
        if 'capital' in country and country['capital']:
            for capital in country['capital']:
                create_city(capital, country['name']['common'])

if __name__ == "__main__":
    populate_countries()
