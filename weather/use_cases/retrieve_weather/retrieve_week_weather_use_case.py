import datetime

from weather.providers.weather_provider_interface import WeatherProviderInterface


class RetrieveWeekWeatherUseCase:
    def __init__(self, weather_provider: WeatherProviderInterface) -> None:
        self.CITY = "Ribeirao Preto"
        self.weather_provider = weather_provider

    def remove_today_from_week_weather(self, week_weather):
        today = datetime.datetime.now()
        today_str = today.strftime("%Y-%m-%d")
        return {k: v for (k, v) in week_weather.items() if k != today_str}

    def execute(self) -> dict:
        week_weather = self.weather_provider.request_week_humidity_from_city(self.CITY)
        return self.remove_today_from_week_weather(week_weather)
