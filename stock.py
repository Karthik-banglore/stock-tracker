# TASK 2: Stock Portfolio Tracker
# Simple stock tracker with hardcoded prices

def main():
    # Hardcoded dictionary for stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2800,
        "MSFT": 350,
        "AMZN": 3200,
        "NVDA": 450
    }
    
    portfolio = {}
    
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")
    
    while True:
        print("\nMenu:")
        print("1. Add stock to portfolio")
        print("2. View portfolio")
        print("3. Calculate total investment")
        print("4. Save results to file")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            add_stock_to_portfolio(portfolio, stock_prices)
        elif choice == "2":
            display_portfolio(portfolio, stock_prices)
        elif choice == "3":
            total_value = calculate_total_investment(portfolio, stock_prices)
            print(f"\nTotal Investment Value: ${total_value:,.2f}")
        elif choice == "4":
            save_portfolio_results(portfolio, stock_prices)
        elif choice == "5":
            print("Thank you for using Stock Portfolio Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_stock_to_portfolio(portfolio, stock_prices):
    """Add stock to portfolio with user input"""
    print("\nAvailable stocks:", list(stock_prices.keys()))
    
    stock_name = input("Enter stock name: ").upper()
    
    if stock_name in stock_prices:
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity > 0:
                if stock_name in portfolio:
                    portfolio[stock_name] += quantity
                else:
                    portfolio[stock_name] = quantity
                print(f"Added {quantity} shares of {stock_name} to portfolio")
            else:
                print("Quantity must be positive!")
        except ValueError:
            print("Please enter a valid number for quantity!")
    else:
        print(f"Stock '{stock_name}' not found in available stocks!")

def display_portfolio(portfolio, stock_prices):
    """Display current portfolio holdings"""
    if not portfolio:
        print("\nYour portfolio is empty!")
        return
    
    print(f"\n{'Stock':<8} {'Quantity':<10} {'Price':<10} {'Value':<12}")
    print("-" * 42)
    
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = quantity * price
        print(f"{stock:<8} {quantity:<10} ${price:<9} ${value:<11,.2f}")

def calculate_total_investment(portfolio, stock_prices):
    """Calculate total investment value using basic arithmetic"""
    total = 0
    for stock, quantity in portfolio.items():
        stock_value = quantity * stock_prices[stock]
        total += stock_value
    return total

def save_portfolio_results(portfolio, stock_prices):
    """Save portfolio results to file (optional feature)"""
    if not portfolio:
        print("Portfolio is empty. Nothing to save!")
        return
    
    file_format = input("Save as 'txt' or 'csv'? ").lower()
    
    if file_format == "txt":
        save_as_txt(portfolio, stock_prices)
    elif file_format == "csv":
        save_as_csv(portfolio, stock_prices)
    else:
        print("Invalid format. Please choose 'txt' or 'csv'")

def save_as_txt(portfolio, stock_prices):
    """Save portfolio to .txt file"""
    filename = "portfolio_results.txt"
    
    with open(filename, "w") as file:
        file.write("Stock Portfolio Results\n")
        file.write("=" * 30 + "\n\n")
        
        total_investment = 0
        
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = quantity * price
            total_investment += value
            
            file.write(f"{stock}: {quantity} shares @ ${price} each = ${value:,.2f}\n")
        
        file.write("\n" + "-" * 30 + "\n")
        file.write(f"Total Investment Value: ${total_investment:,.2f}\n")
    
    print(f"Portfolio saved to {filename}")

def save_as_csv(portfolio, stock_prices):
    """Save portfolio to .csv file"""
    filename = "portfolio_results.csv"
    
    with open(filename, "w") as file:
        # CSV header
        file.write("Stock,Quantity,Price,Value\n")
        
        total_investment = 0
        
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = quantity * price
            total_investment += value
            
            file.write(f"{stock},{quantity},{price},{value:.2f}\n")
        
        # Add total row
        file.write(f"TOTAL,,,{total_investment:.2f}\n")
    
    print(f"Portfolio saved to {filename}")

if __name__ == "__main__":
    main()
