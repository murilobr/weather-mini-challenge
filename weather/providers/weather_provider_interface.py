import abc


class WeatherProviderInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "request_week_humidity_from_city")
            and callable(subclass.request_week_humidity_from_city)
            or NotImplementedError
        )

    @abc.abstractmethod
    def request_week_humidity_from_city(self, city: str) -> dict:
        raise NotImplementedError
