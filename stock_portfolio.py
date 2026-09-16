stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Stock Price:", stock_prices[stock_name])
        print("Investment:", investment)

    else:
        print("Stock not found. Please choose from the available stocks.")

print("\n===== Portfolio Summary =====")
print("Total Investment: $", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")
    file.write("Total Investment: $" + str(total_investment))

print("Portfolio summary saved to portfolio.txt")
