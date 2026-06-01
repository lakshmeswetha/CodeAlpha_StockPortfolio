"""
Stock Portfolio Tracker
Goal: Calculate total investment based on manually defined stock prices.
"""

import csv

# --- Hardcoded stock price dictionary ---
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 420,
    "NFLX": 630,
    "META": 510,
}

def display_available_stocks():
    """Display all available stocks and their prices."""
    print("\n Available Stocks:")
    print(f"{'Symbol':<10} {'Price (USD)':>12}")
    print("-" * 24)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} ${price:>11,.2f}")
    print()

def get_portfolio_from_user():
    """Prompt the user to enter stock names and quantities."""
    portfolio = {}
    print("Enter your stock holdings (type 'done' when finished):")

    while True:
        symbol = input("  Stock symbol (e.g., AAPL): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' not found. Available: {', '.join(STOCK_PRICES.keys())}")
            continue

        try:
            qty = int(input(f"  Quantity of {symbol}: ").strip())
            if qty <= 0:
                print(" Quantity must be a positive number.")
                continue
            # If stock already added, update quantity
            portfolio[symbol] = portfolio.get(symbol, 0) + qty
        except ValueError:
            print(" Please enter a valid whole number for quantity.")

    return portfolio

def calculate_investment(portfolio):
    """Calculate the value of each stock and the total investment."""
    breakdown = {}
    total = 0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        breakdown[symbol] = {
            "quantity": qty,
            "price": price,
            "value": value,
        }
        total += value

    return breakdown, total

def display_results(breakdown, total):
    """Print a formatted summary of the portfolio."""
    print("\n" + "=" * 52)
    print("     PORTFOLIO SUMMARY")
    print("=" * 52)
    print(f"{'Symbol':<8} {'Qty':>6} {'Price':>10} {'Value':>12}")
    print("-" * 52)

    for symbol, data in breakdown.items():
        print(
            f"{symbol:<8} {data['quantity']:>6} "
            f"${data['price']:>9,.2f} "
            f"${data['value']:>11,.2f}"
        )

    print("-" * 52)
    print(f"{'TOTAL INVESTMENT':>36}: ${total:>11,.2f}")
    print("=" * 52)

def save_results(breakdown, total):
    """Optionally save the portfolio to a .txt or .csv file."""
    print("\nWould you like to save the results?")
    print("  [1] Save as .txt")
    print("  [2] Save as .csv")
    print("  [3] Skip")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        filename = "portfolio_summary.txt"
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 40 + "\n")
            f.write(f"{'Symbol':<8} {'Qty':>6} {'Price':>10} {'Value':>12}\n")
            f.write("-" * 40 + "\n")
            for symbol, data in breakdown.items():
                f.write(
                    f"{symbol:<8} {data['quantity']:>6} "
                    f"${data['price']:>9,.2f} "
                    f"${data['value']:>11,.2f}\n"
                )
            f.write("-" * 40 + "\n")
            f.write(f"Total Investment: ${total:,.2f}\n")
        print(f" Saved to '{filename}'")

    elif choice == "2":
        filename = "portfolio_summary.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price (USD)", "Value (USD)"])
            for symbol, data in breakdown.items():
                writer.writerow([symbol, data["quantity"], data["price"], data["value"]])
            writer.writerow([])
            writer.writerow(["Total", "", "", total])
        print(f" Saved to '{filename}'")

    else:
        print("Results not saved.")

def main():
    print("╔══════════════════════════════════╗")
    print("║    STOCK PORTFOLIO TRACKER     ║")
    print("╚══════════════════════════════════╝")

    display_available_stocks()

    portfolio = get_portfolio_from_user()

    if not portfolio:
        print("\n No stocks entered. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)
    display_results(breakdown, total)
    save_results(breakdown, total)

    print("\nThank you for using Stock Portfolio Tracker! \n")

if __name__ == "__main__":
    main()
