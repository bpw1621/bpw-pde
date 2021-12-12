from pandas import Index
from pandas.api.extensions import register_index_accessor

from bpw_pde import ACCESSOR_NAME


@register_index_accessor(ACCESSOR_NAME)
class IndexAccessor:
    def __init__(self, index: Index):
        self._validate(index)
        self._index = index

    @staticmethod
    def _validate(index: Index):
        pass
