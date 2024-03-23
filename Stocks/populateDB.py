import yfinance as yf
import requests

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
                    if "symbol" not in ticker.info:
                        continue
    return tickers

def parse_symbol(symbol, file_path):
    ticker = yf.Ticker(symbol)
    dict = ticker.info
    with open(file_path,"a") as f:
        for key in dict:
            f.write('"' + key + '":"' + str(dict[key]) + '",\n')



if __name__ == "__main__":
    parse_symbol("MSFT", "./stocks/msft.json")