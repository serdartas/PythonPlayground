import yfinance as yf
from model import Country, City, State, Industry, Sector, Currency, Company, session

def all_tickers():
    symbol = str()
    tickers = []
    letters = [""]
    letters.extend([chr(letter_code) for letter_code in range(ord('a'), ord('z') + 1)])

    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    symbol = letter1 + letter2 + letter3 + letter4
                    ticker = yf.Ticker(symbol)
                    if not yf.Ticker(symbol).history(period="1mo").empty:
                        continue
                    parse_symbol(symbol, "./stocks/" + symbol + ".json")
    return tickers

def parse_symbol(symbol, file_path):
    ticker = yf.Ticker(symbol)
    dict = ticker.info
    with open(file_path,"a") as f:
        for key in dict:
            f.write('"' + key + '":"' + str(dict[key]) + '",\n')

def save_company(symbol):
    company = Company()
    company.Ticker = symbol
    company.save(session)
    return company


if __name__ == "__main__":
    #parse_symbol("MSFT", "./stocks/msft.json")
    country = Country()
    country.CountryName = "Turkey"
    country.save(session)
    print(country.CountryId, country.CountryName)

    city = City()
    city.CityName = "Istanbul"
    city.CountryId = session.query(Country).filter_by(CountryName='Turkey').first().CountryId
    city.save(session)
    print(city.CityId, city.CityName, city.CountryId)

    save_company("MSFT")