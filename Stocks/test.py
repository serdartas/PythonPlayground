import yfinance as yf

# Define the ticker symbol
symbol = "a1s"
print(yf.Ticker(symbol).basic_info["currency"])
# Check if the ticker symbol exists


# Print the result
