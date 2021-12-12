from pandas import DataFrame
from pandas.api.extensions import register_dataframe_accessor

from bpw_pde import ACCESSOR_NAME
from bpw_pde.common import clean_name


@register_dataframe_accessor(ACCESSOR_NAME)
class DataframeAccessor:
    def __init__(self, df: DataFrame):
        self._df = df

    @property
    def clean_names(self):
        self._df.columns = [clean_name(column) for column in self._df.columns]
        return self._df
