# CodeAlpha Task 2 - Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("====================================")
print("     STOCK PORTFOLIO TRACKER")
print("====================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:

    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock name!")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity


print("\n====================================")
print("          PORTFOLIO SUMMARY")
print("====================================")

if not portfolio:
    print("No stocks were added.")

else:

    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Value':<12}")
    print("-" * 46)

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        value = quantity * price

        total_investment += value

        print(
            f"{stock:<10}"
            f"{quantity:<12}"
            f"${price:<11}"
            f"${value:<11}"
        )

    print("-" * 46)
    print(f"Total Investment: ${total_investment}")

    # Save result in text file
    with open("portfolio_result.txt", "w") as file:

        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=======================\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            value = quantity * price

            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Value: ${value}\n"
            )

        file.write(f"\nTotal Investment: ${total_investment}")

    print("\nResult saved to portfolio_result.txt")