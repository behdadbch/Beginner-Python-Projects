# Currency Converter

## 💱 Description

The **Currency Converter** is a command-line application that converts an amount from one currency to another using real-time exchange rates fetched from an external API. Users can input the amount, the source currency, and the target currency to receive the converted amount.

## 🧰 Key Concepts Covered

- Making HTTP requests
- Working with APIs
- Handling JSON data
- User Input and Output
- Error Handling
- Arithmetic Operations

## 🚀 How to Use the Currency Converter

### Prerequisites

- Python 3.x installed on your machine.
- Access to a command-line interface (CLI) or terminal.
- An API key from [ExchangeRate-API](https://www.exchangerate-api.com/) or another currency conversion API (free account).

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd currency_converter
Install required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python main.py
Follow the on-screen instructions to perform currency conversions.
📖 Usage Instructions

Upon running the application, you will be prompted to:

Enter the amount to convert.
Enter the source currency code (e.g., USD, EUR).
Enter the target currency code (e.g., GBP, JPY).
Example Output:
vbnet
Copy code
Welcome to the Currency Converter!

Enter the amount to convert: 100
Enter the source currency code (e.g., USD): USD
Enter the target currency code (e.g., EUR): EUR

Fetching exchange rate...

100 USD is equivalent to 84.50 EUR
🛠️ Code Overview

The application consists of functions to handle API requests and perform the conversion:

get_exchange_rate(api_key, base_currency, target_currency): Fetches the exchange rate between two currencies.
convert_currency(amount, rate): Calculates the converted amount.
Modules Used
requests: For making HTTP requests to the currency conversion API.
🤝 Contributing

Contributions are welcome! If you have ideas to enhance this currency converter, feel free to fork the repository and submit a pull request.

📧 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.

### Code Explanation and Best Practices
1. Modular Functions

get_exchange_rate(): Handles the API request and returns the exchange rate between two currencies.
main(): Manages user interaction and orchestrates the conversion process.
2. API Integration

ExchangeRate-API: Uses a free API to fetch current exchange rates.
Error Handling: Checks for successful responses and handles errors gracefully.
3. User Input Handling

Amount Validation: Ensures the user enters a valid numerical amount.
Currency Codes: Accepts currency codes and converts them to uppercase for consistency.
4. Arithmetic Operations

Conversion Calculation: Multiplies the amount by the exchange rate to get the converted amount.
5. User Experience

Clear Prompts: Guides the user through each step of the conversion process.
Formatted Output: Displays the converted amount with two decimal places for clarity.
Enhancements and Extensions
Consider adding the following features to enhance the Currency Converter:

Support for More Currencies: Ensure the application handles all ISO currency codes.
Historical Rates: Allow users to fetch historical exchange rates.
Graphical User Interface (GUI): Create a GUI version using Tkinter or another library.
Caching Rates: Implement caching to reduce API calls and improve performance.
Testing the Currency Converter
Valid Inputs: Test with different amounts and currency codes to ensure accurate conversions.
Invalid Inputs: Enter invalid amounts or currency codes to verify that the program handles them appropriately.
API Key Validation: Test with both valid and invalid API keys.
