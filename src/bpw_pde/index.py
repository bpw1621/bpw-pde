from pandas.api.extensions import register_index_accessor


@register_index_accessor('bpw')
class IndexAccessor:
    def __init__(self, index):
        self._validate(index)
        self._index = index

    @staticmethod
    def _validate(index):
        pass
