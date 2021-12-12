from pandas.api.extensions import register_dataframe_accessor


@register_dataframe_accessor('bpw')
class DataframeAccessor:
    def __init__(self, df):
        self._validate(df)
        self._df = df

    @staticmethod
    def _validate(df):
        pass
