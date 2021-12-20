import functools

from pandas import Series
from pandas.api.extensions import register_series_accessor

from bpw_pde import ACCESSOR_NAME
from bpw_pde.common import clean_name, md5, unicode_normalize, DEFAULT_UNICODE_NORMALIZATION_FORM


@register_series_accessor(ACCESSOR_NAME)
class SeriesAccessor:
    def __init__(self, series: Series):
        self._series = series

    @property
    def clean_name(self):
        self._series.name = clean_name(self._series.name)
        return self._series

    @property
    def hashify(self):
        return self._series.apply(md5)

    def normalize(self, form: str = DEFAULT_UNICODE_NORMALIZATION_FORM):
        return self._series.apply(functools.partial(unicode_normalize, form=form))
