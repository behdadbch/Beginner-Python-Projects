# Weather Info Fetcher

## 🌤️ Description

The **Weather Info Fetcher** is a command-line application that retrieves current weather information for a specified city using the OpenWeatherMap API. Users can enter the name of a city and receive details such as temperature, humidity, and weather conditions.

## 🧰 Key Concepts Covered

- Making HTTP requests
- Working with APIs
- Handling JSON data
- User Input and Output
- Error Handling

## 🚀 How to Use the Weather Info Fetcher

### Prerequisites

- Python 3.x installed on your machine.
- Access to a command-line interface (CLI) or terminal.
- An API key from OpenWeatherMap (free account).

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd weather_info_fetcher
Install required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python main.py
Follow the on-screen instructions to get the weather information.
📖 Usage Instructions

Upon running the application, you will be prompted to:

Enter the name of the city for which you want the weather information.
Example Output:
yaml
Copy code
Welcome to the Weather Info Fetcher!

Enter the city name: London
Current temperature in London: 15°C
Humidity: 82%
Weather: Clear sky
🛠️ Code Overview

The application consists of a main function that handles user input and an API call function to fetch weather data.

Modules Used
requests: For making HTTP requests to the OpenWeatherMap API.
🤝 Contributing

Contributions are welcome! If you have ideas to enhance this weather fetcher, feel free to fork the repository and submit a pull request.

📧 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.

### Code Explanation and Best Practices
1. Modular Functions

get_weather(city, api_key): Encapsulates the logic for making the API request and handling the response. This modular design improves code organization.
2. API Integration

Requests Library: Utilizes the requests library to make HTTP GET requests to the OpenWeatherMap API, fetching weather data in a structured format.
3. JSON Handling

Data Parsing: Retrieves and extracts relevant data (temperature, humidity, weather description) from the JSON response.
4. User Input Handling

City Input: Prompts the user for the city name, with an option to exit the application.
Error Handling: Checks the API response status code to determine if the request was successful.
5. User Experience

Clear Prompts: Guides the user through entering their API key and city name.
Formatted Output: Displays the weather information in a clear and readable format.
