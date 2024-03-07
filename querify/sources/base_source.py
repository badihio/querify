import abc


class BaseSource(
    abc.ABC,
):
    @property
    @abc.abstractmethod
    def name(
        self,
    ) -> str:
        ...
