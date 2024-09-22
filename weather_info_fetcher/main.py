import requests

def get_weather(city, api_key):
    """
    Fetches the weather information for a specified city using the OpenWeatherMap API.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        return temperature, humidity, weather_description
    else:
        return None

def main():
    """
    Main function to run the Weather Info Fetcher.
    """
    print("Welcome to the Weather Info Fetcher!\n")
    
    api_key = input("Enter your OpenWeatherMap API key: ")
    
    while True:
        city = input("Enter the city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        
        weather_info = get_weather(city, api_key)
        
        if weather_info:
            temperature, humidity, weather_description = weather_info
            print(f"\nCurrent temperature in {city}: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather_description.capitalize()}\n")
        else:
            print("City not found. Please check the name and try again.\n")

if __name__ == "__main__":
    main()
