# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", list(stock_prices.keys()))

# Taking user input
while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        portfolio[stock_name] = quantity
    else:
        print("❌ Stock not available!")

# Calculating total investment
print("\n📊 Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock} - {quantity} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value = ${total_investment}")

# Save to file option
save_option = input("Do you want to save the result? (yes/no): ").lower()

if save_option == "yes":
    file_type = input("Save as (1) TXT or (2) CSV? Enter 1 or 2: ")

    if file_type == "1":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity
                file.write(f"{stock} - {quantity} × {price} = {investment}\n")
            file.write(f"\nTotal Investment = {total_investment}")
        print("✅ Saved as portfolio.txt")

    elif file_type == "2":
        with open("portfolio.csv", "w") as file:
            file.write("Stock,Quantity,Price,Investment\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity
                file.write(f"{stock},{quantity},{price},{investment}\n")
            file.write(f"\nTotal Investment,,,{total_investment}")
        print("✅ Saved as portfolio.csv")

    else:
        print("❌ Invalid choice")

print("🚀 Thank you for using Stock Portfolio Tracker!")
