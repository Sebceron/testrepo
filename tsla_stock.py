import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


# Fetch Tesla stock data for the past year
stock = yf.Ticker("TSLA")
data = stock.history(period="1y")

# Display the first few rows
print(data.head(20))



print(data.info())  # Check data types and null values
print(data.describe())  # Get statistical summaries



# visualize closing prices

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label='Closing Price')
plt.title('Tesla Stock Closing Prices (Past Year)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()





"add moving averages"

# Calculate moving averages
data['20-Day MA'] = data['Close'].rolling(window=20).mean()
data['50-Day MA'] = data['Close'].rolling(window=50).mean()

# Plot the moving averages with the closing price
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label='Closing Price')
plt.plot(data.index, data['20-Day MA'], label='20-Day Moving Average', linestyle='--')
plt.plot(data.index, data['50-Day MA'], label='50-Day Moving Average', linestyle='--')
plt.title('Tesla Stock with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()







"visualize daily price changes"

# Calculate daily price changes
data['Daily Change'] = data['Close'].pct_change()

# Plot daily changes
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Daily Change'], label='Daily Change')
plt.axhline(0, color='red', linestyle='--', linewidth=1)
plt.title('Tesla Daily Price Changes (Past Year)')
plt.xlabel('Date')
plt.ylabel('Daily Change (%)')
plt.legend()
plt.grid()
plt.show()



"save the visualization"

plt.savefig('tesla_stock_analysis.png')




"volume analisis - Visualize trading volumes"

plt.figure(figsize=(10, 6))
plt.bar(data.index, data['Volume'], label='Trading Volume', color='orange')
plt.title('Tesla Trading Volume (Past Year)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid()
plt.show()






"Compare Multiple Stocks: Fetch and compare data for multiple companies (e.g., Tesla and Apple)"

tickers = ["TSLA", "AAPL"]
data = yf.download(tickers, period="1y")['Close']

# Plot comparison
data.plot(figsize=(12, 8), title="Tesla vs. Apple Stock Prices")
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid()
plt.show()