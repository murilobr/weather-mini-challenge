import datetime

from flask import Request, render_template

from .retrieve_week_weather_use_case import RetrieveWeekWeatherUseCase


class RetrieveWeatherController:
    def __init__(self, retrieve_weather_use_case: RetrieveWeekWeatherUseCase) -> str:
        self.retrieve_weather_use_case = retrieve_weather_use_case

    def _get_weekdays_with_high_rain_probability(
        self, week_weather: dict, humidity_limit: int
    ) -> list:
        return [
            {
                "weekday": datetime.datetime.strptime(k, "%Y-%m-%d").strftime("%A"),
                "can_rain": humidity_limit in v,
            }
            for (k, v,) in week_weather.items()
        ]

    def _get_weekdays_umbrella_needed(self, high_rain_probability_weekdays: list) -> list:
        return [
            ud["weekday"] for ud in high_rain_probability_weekdays if ud["can_rain"]
        ]

    def _transform_list_to_human_readable(self, weekdays_umbrella_needed) -> str:
        umbrella_days_str = ", ".join(weekdays_umbrella_needed[:-1])
        if len(umbrella_days_str) > 0:
            umbrella_days_str += f" and {weekdays_umbrella_needed[-1]}"
        return umbrella_days_str

    def handler(self) -> str:
        week_weather = self.retrieve_weather_use_case.execute()

        high_rain_probability_weekdays = self._get_weekdays_with_high_rain_probability(
            week_weather, 70
        )

        weekdays_umbrella_needed = self._get_weekdays_umbrella_needed(
            high_rain_probability_weekdays
        )

        if len(weekdays_umbrella_needed) == 0:
            umbrella_needed_days_human_readable = "No umbrella needed"
        else:
            umbrella_needed_days_human_readable = self._transform_list_to_human_readable(
                weekdays_umbrella_needed
            )

        return render_template(
            "index.html", **{"umbrella_days": umbrella_needed_days_human_readable},
        )
