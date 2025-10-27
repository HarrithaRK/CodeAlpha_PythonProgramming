# TASK 2: Stock Portfolio Tracker

# Hardcoded stock prices (dictionary)
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 140,  # Google
    "AMZN": 130,   # Amazon
    "MSFT": 310    # Microsoft
}

portfolio = {}  # To store user's stock and quantity

print("Welcome to the Stock Portfolio Tracker ")
print("Available Stocks:", ', '.join(stock_prices.keys()))
print("Enter 'done' when you finish adding stocks.\n")

# Step 1: Take user input
while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    elif stock not in stock_prices:
        print(" Stock not found. Please enter a valid stock symbol.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print(" Please enter a valid number for quantity.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Step 2: Calculate total investment
total_investment = 0
print("\nYour Portfolio Summary:")
print("-" * 35)
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print("-" * 35)
print(f" Total Investment Value: ${total_investment}")

# Step 3 (Optional): Save to file
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-" * 35 + "\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} × ${price} = ${investment}\n")
        file.write("-" * 35 + "\n")
        file.write(f"Total Investment: ${total_investment}\n")
    print(" Portfolio saved to 'portfolio_summary.txt'.")
