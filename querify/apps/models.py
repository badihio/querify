import pydantic
import typing


class Model(
    pydantic.BaseModel,
):
    ...


class Source(
    pydantic.BaseModel,
):
    name: str
    model: typing.Any
