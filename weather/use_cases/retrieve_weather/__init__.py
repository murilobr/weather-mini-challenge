import configparser
import os

from weather.providers.implementations.open_weather_map_provider import (
    OpenWeatherMapProvider,
)
from weather.use_cases.retrieve_weather.retrieve_weather_controller import (
    RetrieveWeatherController,
)
from weather.use_cases.retrieve_weather.retrieve_week_weather_use_case import (
    RetrieveWeekWeatherUseCase,
)

config = configparser.ConfigParser()
config.read(os.path.abspath("conf.ini"))

open_weather_map_provider = OpenWeatherMapProvider(config["DEFAULT"]["API_KEY"])
retrieve_week_weather_use_case = RetrieveWeekWeatherUseCase(open_weather_map_provider)
retrieve_weather_controller = RetrieveWeatherController(retrieve_week_weather_use_case)
