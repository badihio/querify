import concurrent.futures
import kubernetes
import pydantic


class Pod(
    pydantic.BaseModel,
):
    name: str
    namespace: str


class Namespace(
    pydantic.BaseModel,
):
    name: str


class Client:
    def __init__(
        self,
    ):
        kubernetes.config.load_kube_config()

        self.client = kubernetes.client.CoreV1Api()

    def get_namespace_pods(
        self,
        namespace: str,
    ):
        response = self.client.list_namespaced_pod(
            namespace=namespace,
        )

        return [
            Pod(
                name=pod.metadata.name,
                namespace=pod.metadata.namespace,
            )
            for pod in response.items
        ]

    def get_pods(
        self,
    ):
        namespaces = list(self.get_namespaces())

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=10,
        ) as executor:

            futures = [
                executor.submit(self.get_namespace_pods, namespace.name)
                for namespace in namespaces
            ]

            for future in concurrent.futures.as_completed(
                fs=futures,
            ):
                result = future.result()

                yield from result

    def get_namespaces(
        self,
    ):
        response = self.client.list_namespace()

        for namespace in response.items:
            yield Namespace(
                name=namespace.metadata.name,
            )
