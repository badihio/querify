import datetime

from . import base_app
from . import clients


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
        return clients.storage.File

    def get_data(
        self,
    ):
        return list(self.storage_client.get_files())


class DirSource(
    base_app.BaseSource,
):
    name = 'dirs'

    def __init__(
        self,
    ) -> None:
        super().__init__()

        self.storage_client = clients.storage.Client()

    @property
    def model(
        self,
    ):
        return clients.storage.Dir

    def get_data(
        self,
    ):
        return list(self.storage_client.get_dirs())


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
            DirSource(),
        ]
