from pandas import Series
from pandas.api.extensions import register_series_accessor

from bpw_pde import ACCESSOR_NAME


@register_series_accessor(ACCESSOR_NAME)
class SeriesAccessor:
    def __init__(self, series: Series):
        self._validate(series)
        self._series = series

    @staticmethod
    def _validate(series: Series):
        pass
