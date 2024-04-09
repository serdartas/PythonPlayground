import yfinance as yf
from model import Country, City, State, Industry, Sector, Currency, Company, session



def get_all_symbols():
    # Tries each 1, 2, 3 and 4 letter combinations of symbols in yfinance tickers
    # and returns an array of all the ticker symbols these exist in yfinance
    symbols = []
    counter = 0
    for i in range(65, 91):
        for j in range(65, 91):
            for k in range(65, 91):
                for l in range(65, 91):
                    counter += 1
                    if counter == 250:
                        return symbols
                    symbol = chr(i) + chr(j) + chr(k) + chr(l)
                    if not yf.Ticker(symbol).history(period="1mo").empty:
                        symbols.append(symbol)
    return symbols

if __name__ == "__main__":
    print(get_all_symbols())