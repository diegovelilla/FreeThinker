from dotenv import dotenv_values
from datetime import datetime
import requests


def weather_forecaster(input_list):
    """
    Get current weather on specified location.

    Parameters:
    input_list (list): A list containing the location from where you want to check the weather.

        Example format: ["London"]

    Returns:
    (str): The formatted weather or an error message if something goes wrong.
    """
    try:
        CONFIG = dotenv_values("config/.env")

        # Ensure API_KEY is available
        API_KEY = CONFIG.get("WEATHER_API_KEY")
        if not API_KEY:
            raise KeyError(
                "API key is missing. Please check your configuration.")

        if not input_list or not isinstance(input_list, list) or not input_list[0]:
            raise ValueError(
                "The input_list must contain at least one valid city name.")

        city = input_list[0]
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
        response = requests.get(url)
        data = response.json()

        formatted_response = f"""
Weather: {data["weather"][0]["description"]}.
Temperature: {data["main"]["temp"]}°C
Feels like: {data["main"]["feels_like"]}°C
Min temperature: {data["main"]["temp_min"]}°C
Max temperature: {data["main"]["temp_max"]}°C
Humidity: {data["main"]["humidity"]}%
Sunrise: {datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')}
Sunset: {datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')}
"""
        return formatted_response

    except Exceptions as e:
        return f"Error occurred: {e}"
