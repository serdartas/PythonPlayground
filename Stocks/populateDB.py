import yfinance as yf

msft = yf.Ticker("MSFT")
inf = msft.info
print(inf)


