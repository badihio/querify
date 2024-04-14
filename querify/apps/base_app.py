import abc

from . import models


class BaseSource(
    abc.ABC,
):
    name: str

    def __init__(
        self,
        filters: dict,
    ) -> None:
        self.filters = filters

    @property
    def model(
        self,
    ) -> models.Model:
        ...

    @abc.abstractclassmethod
    def get_data(
        self,
    ) -> list[models.Model]:
        ...


class BaseApp(
    abc.ABC,
):
    def get_source_by_name(
        self,
        source_name: str,
    ):
        for source in self.sources:
            if source.name == source_name:
                return source

        raise ValueError('Source not found')

    @property
    def sources(
        self,
    ) -> list[BaseSource]:
        ...
