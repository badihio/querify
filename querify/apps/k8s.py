from . import base_app
from . import clients


class PodSource(
    base_app.BaseSource,
):
    name = 'pods'

    def __init__(
        self,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)

        self.k8s_client = clients.k8s.Client()

    @property
    def model(
        self,
    ):
        return clients.k8s.Pod

    def get_data(
        self,
    ):
        return list(self.k8s_client.get_pods())


class NamespaceSource(
    base_app.BaseSource,
):
    name = 'namespaces'

    def __init__(
        self,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)

        self.k8s_client = clients.k8s.Client()

    @property
    def model(
        self,
    ):
        return clients.k8s.Namespace

    def get_data(
        self,
    ):
        return list(self.k8s_client.get_namespaces())


class App(
    base_app.BaseApp,
):
    name = 'k8s'

    @property
    def sources(
        self,
    ) -> list:
        return [
            PodSource,
            NamespaceSource,
        ]
