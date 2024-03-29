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


class App(
    base_app.BaseApp,
):
    name = 'storage'

    sources = [
        models.Source(
            name='files',
            model=FileModel,
        ),
    ]

    def __init__(
        self,
    ) -> None:
        super().__init__()

        self.storage_client = clients.storage.Client()

    def get_sources(
        self,
    ) -> list[models.Source]:
        return self.sources

    def get_source_by_name(
        self,
        source_name: str,
    ):
        for source in self.sources:
            if source.name == source_name:
                return source

        raise ValueError('Source not found')

    def get_source_data(
        self,
        source_name: str,
    ) -> list:
        if source_name == 'files':
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

        raise ValueError('Source not found')
