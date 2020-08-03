from unittest.mock import MagicMock, patch

from freezegun import freeze_time

from weather.use_cases.retrieve_weather.retrieve_week_weather_use_case import (
    RetrieveWeekWeatherUseCase,
)


@freeze_time("2020-01-01")
def test_remove_today_from_week_weather():
    week_weather = {
        "2020-01-01": [10, 20, 30, 40],
        "2020-01-02": [10, 20, 30, 40],
        "2020-01-03": [10, 20, 30, 40],
        "2020-01-04": [10, 20, 30, 40],
        "2020-01-05": [10, 20, 30, 40],
        "2020-01-06": [10, 20, 30, 40],
    }

    open_weather_map_provider = MagicMock()
    retrieve_week_weather_use_case = RetrieveWeekWeatherUseCase(
        open_weather_map_provider
    )

    result = retrieve_week_weather_use_case.remove_today_from_week_weather(week_weather)

    assert "2020-01-01" not in result


def test_request_week_humidity_from_city_is_called():
    open_weather_map_provider = MagicMock()

    retrieve_week_weather_use_case = RetrieveWeekWeatherUseCase(
        open_weather_map_provider
    )
    retrieve_week_weather_use_case.execute()

    open_weather_map_provider.request_week_humidity_from_city.assert_called_once_with(
        "Ribeirao Preto"
    )


@patch.object(RetrieveWeekWeatherUseCase, "remove_today_from_week_weather")
def test_remove_today_from_week_weather_is_called(
    mocked_remove_today_from_week_weather,
):
    week_weather = {
        "2020-01-01": [10, 20, 30, 40],
        "2020-01-02": [10, 20, 30, 40],
        "2020-01-03": [10, 20, 30, 40],
        "2020-01-04": [10, 20, 30, 40],
        "2020-01-05": [10, 20, 30, 40],
        "2020-01-06": [10, 20, 30, 40],
    }

    open_weather_map_provider = MagicMock()

    retrieve_week_weather_use_case = RetrieveWeekWeatherUseCase(
        open_weather_map_provider
    )

    retrieve_week_weather_use_case.execute()
    mocked_remove_today_from_week_weather.assert_called_once()
