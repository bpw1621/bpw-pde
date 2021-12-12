from pandas import DataFrame
from pandas.api.extensions import register_dataframe_accessor

from bpw_pde import ACCESSOR_NAME


@register_dataframe_accessor(ACCESSOR_NAME)
class DataframeAccessor:
    def __init__(self, df: DataFrame):
        self._validate(df)
        self._df = df

    @staticmethod
    def _validate(df: DataFrame):
        pass
