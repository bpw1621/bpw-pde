from pandas.api.extensions import register_series_accessor


@register_series_accessor('bpw')
class SeriesAccessor:
    def __init__(self, series):
        self._validate(series)
        self._series = series

    @staticmethod
    def _validate(series):
        pass
