import datetime

from . import base_app
from . import clients
from . import models


class FileModel(
    models.Model,
):
    name: str
    size_in_bytes: int
    owner: str
    update_date: datetime.datetime
    access_date: datetime.datetime


class FileSource(
    base_app.BaseSource,
):
    name = 'files'

    def __init__(
        self,
    ) -> None:
        super().__init__()

        self.storage_client = clients.storage.Client()

    @property
    def model(
        self,
    ):
        return FileModel

    def get_data(
        self,
    ):
        return [
            FileModel(
                name=file.name,
                size_in_bytes=file.size_in_bytes,
                owner=file.owner,
                update_date=file.update_date,
                access_date=file.access_date,
            )
            for file in self.storage_client.get_files()
        ]


class App(
    base_app.BaseApp,
):
    name = 'storage'

    @property
    def sources(
        self,
    ) -> list:
        return [
            FileSource(),
        ]
