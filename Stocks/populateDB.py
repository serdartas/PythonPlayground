import yfinance as yf
from datetime import datetime
import requests
from model import * # Country, City, State, Industry, Sector, Currency, Company, session, Exchange, create_city

def all_tickers():
    # stop_at = 100
    # counter = 0
    symbol = str()
    tickers = []
    letters = [""]
    letters.extend([chr(letter_code) for letter_code in range(ord('a'), ord('z') + 1)])

    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    # if(counter >= stop_at):
                    #     break
                    # counter += 1
                    symbol = letter1 + letter2 + letter3 + letter4
                    try:
                        ticker = yf.Ticker(symbol)
                        # if not yf.Ticker(symbol).history(period="1mo").empty:
                        #     continue
                        # parse_symbol(symbol, "./Stocks/parsed_json/" + symbol + ".json")
                        save_company(symbol)
                    except Exception as e:
                        print(f"Could not get data for ticker '{symbol}': {e}")

    return tickers


def parse_symbol(symbol, file_path):
    try:
        ticker = yf.Ticker(symbol)
        dict = ticker.info
        with open(file_path, "a") as f:
            for key in dict:
                f.write('"' + key + '":"' + str(dict[key]) + '",\n')
        
    except Exception as e:
        pass

def save_company(symbol):
    try:
        ticker = yf.Ticker(symbol)
        dict = ticker.info
        print("Saving", dict['shortName'])
        CityId = create_city(dict['city'], dict['country']).CityId
        CurrencyId = create_currency(dict['financialCurrency'], dict['financialCurrency']).CurrencyId # Company finances currency might differ from exchange currency
        ExchangeId = create_exchange(dict['exchange'], dict['currency'], dict['currency']).ExchangeId
        IndustryId = create_industry(dict['industry']).IndustryId
        SectorId = create_sector(dict['sector']).SectorId
        StateId = create_state(dict['state'], dict['country']).StateId

        company = Company()
        company.Ticker = symbol
        company.CityId = CityId
        company.CurrencyId = CurrencyId
        company.ExchangeId = ExchangeId
        company.IndustryId = IndustryId
        company.SectorId = SectorId
        company.StateId = StateId
        
        company.AuditRisk = int(dict['auditRisk'])
        company.BoardRisk = int(dict['boardRisk'])
        company.BookValue = float(dict['bookValue'])
        company.BusinessSummary = dict['longBusinessSummary']
        company.CompensationRisk = int(dict['compensationRisk'])
        company.EmployeeCount = int(dict['fullTimeEmployees'])
        company.GovernanceEpochDate = datetime.utcfromtimestamp(int(dict['governanceEpochDate']))
        company.HeldPercentInsiders = float(dict['heldPercentInsiders'])
        company.OverallRisk = int(dict['overallRisk'])
        company.ShareholderRisk = int(dict['shareHolderRightsRisk'])
        company.TotalShares = int(dict['sharesOutstanding'])
        company.PublicShares = int(dict['floatShares'])
        company.save(session)
        return company
    except Exception as e:
        pass

if __name__ == "__main__":

    #parse_symbol("MSFT", "./Stocks/parsed_json/msft.json")
    #country = Country()
    #country.CountryName = "France"
    #country.save(session)
    #print(country.CountryId, country.CountryName)

    #city = City()
    #city.CityName = "Paris"
    #city.CountryId = session.query(Country).filter_by(CountryName='France').first().CountryId
    #city.save(session)
    #print(city.CityId, city.CityName, city.CountryId)

    # save_company("MSFT")
    all_tickers()