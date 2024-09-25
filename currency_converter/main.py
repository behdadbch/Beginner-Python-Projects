import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    """
    Fetches the exchange rate between base_currency and target_currency.
    """
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rate']
        else:
            print("Error in fetching exchange rate:", data['error-type'])
            return None
    else:
        print("HTTP Error:", response.status_code)
        return None

def main():
    """
    Main function to run the Currency Converter.
    """
    print("Welcome to the Currency Converter!\n")
    
    api_key = input("Enter your ExchangeRate-API key: ").strip()
    
    while True:
        try:
            amount = float(input("\nEnter the amount to convert: "))
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")
            continue
        
        base_currency = input("Enter the source currency code (e.g., USD): ").strip().upper()
        target_currency = input("Enter the target currency code (e.g., EUR): ").strip().upper()
        
        print("\nFetching exchange rate...\n")
        rate = get_exchange_rate(api_key, base_currency, target_currency)
        
        if rate:
            converted_amount = amount * rate
            print(f"{amount} {base_currency} is equivalent to {converted_amount:.2f} {target_currency}")
        else:
            print("Failed to retrieve exchange rate. Please check your inputs and try again.")
        
        again = input("\nDo you want to perform another conversion? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Currency Converter! Goodbye!")
            break

if __name__ == "__main__":
    main()