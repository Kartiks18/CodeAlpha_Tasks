# Stock Portfolio Tracker
# Task: Calculate total investment using predefined stock prices

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 310
}

portfolio = {}

print("Welcome to Stock Portfolio Tracker")
print("Enter 'done' when finished.\n")

# Take user input for stock quantities
while True:
    stock = input("Enter stock symbol (AAPL/TSLA/GOOG/AMZN/MSFT): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found! Try again.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total value
total_value = 0
result_text = "Your Stock Portfolio:\n\n"

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    result_text += f"{stock} - {qty} shares × ${price} = ${value}\n"

result_text += f"\nTotal Investment Value = ${total_value}\n"

print("\n" + result_text)

# Optional: Save to file
save = input("Save result to file? (yes/no): ").lower()

if save == "yes":
    filename = "portfolio_result.txt"
    with open(filename, "w") as file:
        file.write(result_text)
    print(f"✔ Result saved to {filename}")
else:
    print("✔ Not saved.")
