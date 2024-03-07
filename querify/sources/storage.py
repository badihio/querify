from . import base_source


class Source(
    base_source.BaseSource,
):
    @property
    def name(
        self,
    ) -> str:
        return 'storage'
