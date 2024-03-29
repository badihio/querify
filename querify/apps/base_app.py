import abc

from . import models


class BaseApp(
    abc.ABC,
):
    @abc.abstractmethod
    def get_sources(
        self,
    ) -> list[models.Source]:
        ...

    @abc.abstractmethod
    def get_source_data(
        self,
        source_name: str
    ) -> list[models.Model]:
        ...
