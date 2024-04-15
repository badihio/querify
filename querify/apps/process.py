from . import base_app
from . import clients


class ProcessSource(
    base_app.BaseSource,
):
    name = 'processes'

    def __init__(
        self,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)

        self.process_client = clients.process.Client()

    @property
    def model(
        self,
    ):
        return clients.process.Process

    def get_data(
        self,
    ):
        return list(self.process_client.get_processes())


class App(
    base_app.BaseApp,
):
    name = 'process'

    @property
    def sources(
        self,
    ) -> list:
        return [
            ProcessSource,
        ]
