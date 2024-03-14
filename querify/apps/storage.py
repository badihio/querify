import datetime

from . import base_app
from . import clients


class FileModel(
    base_app.Model,
):
    name: str
    size_in_bytes: str
    owner: str
    update_date: datetime.datetime
    access_date: datetime.datetime


class App(
    base_app.BaseApp,
):
    name = 'storage'

    def __init__(
        self,
    ) -> None:
        super().__init__()

        self.storage_client = clients.storage.Client()

    def get_sources(
        self,
    ) -> list[base_app.Source]:
        return [
            base_app.Source(
                name='files',
                model=FileModel,
            ),
        ]

    def get_source_data(
        self,
        source_name: str,
    ) -> list | None:
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

