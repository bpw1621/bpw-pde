import missingno
# noinspection PyUnresolvedReferences
import sidetable
from pandas import DataFrame
from pandas.api.extensions import register_dataframe_accessor

from bpw_pde import ACCESSOR_NAME
from bpw_pde.common import clean_name


class _MissignoAdapter:
    def __init__(self, df: DataFrame):
        self._df = df

    def matrix(self, **kwargs):
        return missingno.matrix(self._df, **kwargs)

    def bar(self, **kwargs):
        return missingno.bar(self._df, **kwargs)

    def heatmap(self, **kwargs):
        return missingno.heatmap(self._df, **kwargs)

    def dendrogram(self, **kwargs):
        return missingno.dendrogram(self._df, **kwargs)


@register_dataframe_accessor(ACCESSOR_NAME)
class DataframeAccessor:
    def __init__(self, df: DataFrame):
        self._df = df

    @property
    def clean_names(self):
        self._df.columns = [clean_name(column) for column in self._df.columns]
        return self._df

    def samp(self, n: int = 5):
        return self._df.sample(n).T

    @property
    def stb(self):
        return self._df.stb

    def freq(self, *args, **kwargs):
        return self._df.stb.freq(*args, **kwargs)

    @property
    def msno(self):
        return _MissignoAdapter(self._df)
