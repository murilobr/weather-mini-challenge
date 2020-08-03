import datetime

import requests

from ..weather_provider_interface import WeatherProviderInterface


class OpenWeatherMapProvider(WeatherProviderInterface):
    def __init__(self, API_KEY: str) -> None:
        self.API_KEY = API_KEY

    def request_week_humidity_from_city(self, city: str) -> dict:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.API_KEY}"
        )

        week_weather = r.json()
        week_humidity = {}

        for weather in week_weather.get("list", []):
            weather_date = datetime.date.fromtimestamp(weather["dt"])
            weather_date_str = str(weather_date)

            if weather_date_str not in week_humidity:
                week_humidity[weather_date_str] = []

            week_humidity[weather_date_str].append(weather["main"]["humidity"])

        return week_humidity
