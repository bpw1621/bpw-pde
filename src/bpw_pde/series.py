from pandas import Series
from pandas.api.extensions import register_series_accessor

from bpw_pde import ACCESSOR_NAME
from bpw_pde.common import clean_name


@register_series_accessor(ACCESSOR_NAME)
class SeriesAccessor:
    def __init__(self, series: Series):
        self._series = series

    @property
    def clean_name(self):
        self._series.name = clean_name(self._series.name)
        return self._series
