import requests
import os

def get_weather(city_name):
    api_key = os.environ['current_weather_data']  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}q={city_name}&appid={api_key}"

    try:
        response = requests.get(complete_url)
        api_data = response.json()

        # Print the API response for debugging purposes
        print(api_data)

        if api_data['cod'] != 200:
            print(f"Error: {api_data['message']}")
            return

        temp_city = api_data['main']['temp'] - 273.15
        weather_desc = api_data['weather'][0]['description']
        humidity = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']

        print(f"Temperature: {temp_city:.2f}°C")
        print(f"Weather Description: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except KeyError as e:
        print(f"KeyError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    get_weather(city_name.strip())
