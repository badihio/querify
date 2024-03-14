import abc
import pydantic


class Model(
    pydantic.BaseModel,
):
    ...


class Source(
    pydantic.BaseModel,
):
    name: str
    model: Model


class BaseApp(
    abc.ABC,
):
    @abc.abstractmethod
    def get_sources(
        self,
    ) -> list[Source]:
        ...

    @abc.abstractmethod
    def get_source_data(
        self,
        source_name: str
    ) -> list[Model]:
        ...
