import datetime

from . import base_app


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

    def get_sources(
        self,
    ):
        return [
            base_app.Source(
                name='files',
                model=FileModel,
            ),
        ]

    def get_source_data(self, source_name: str) -> list:
        return super().get_source_data(source_name)
