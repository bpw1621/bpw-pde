"""Module for the :class:`pandas.DataFrame` accessor class."""

import missingno
# noinspection PyUnresolvedReferences
import sidetable
from pandas import DataFrame
from pandas.api.extensions import register_dataframe_accessor

from bpw_pde import ACCESSOR_NAME
from bpw_pde.common import clean_name


class _MissignoAdapter:
    """
    Adapts the functional interface of the `missingno` package to the interface needed by :class:`DataframeAccessor`.

    Simply forwards the captured :class:`pandas.DataFrame` and any keyword arguments to the respective `missingno`
    function. This class is not intended to be used directly but through the :class:`DataframeAccessor`.
    """

    def __init__(self, df: DataFrame) -> None:
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
    """Accessor class for :class:`pandas.DataFrame`."""

    def __init__(self, df: DataFrame) -> None:
        self._df = df

    @property
    def clean_names(self) -> DataFrame:
        """
        Applies :meth:`bpw_pde.common.clean_name` to all column names of the captured :class:`pandas.DataFrame`.

        :return: A copy of the captured :class:`pandas.DataFrame` with cleaned column names.
        """

        df = self._df.copy()
        df.columns = [clean_name(column) for column in df.columns]
        return df

    def samp(self, n: int = 5) -> DataFrame:
        """
        Transposed random sample of the captured :class:`pandas.DataFrame`.

        It is common want to take a quick look at a couple of random samples of rows from a :class:`pandas.DataFrame`
        and have it all fit on screen without mucking with `pandas` display settings. This usually does a better job
        of that than just calling :meth:`pandas.DataFrame.sample` alone.

        :param n: The number of rows to sample, defaults to `5`.
        :return: A random sample of the captured :class:`pandas.DataFrame` rows transposed.
        """

        return self._df.sample(n).T

    @property
    def stb(self):
        """
        Alias to `sidetable` :class:`pandas.DataFrame` accessor `stb`.

        :return: The `stb` accessor on the captured :class:`pandas.DataFrame`.
        """

        return self._df.stb

    def freq(self, *args, **kwargs):
        """
        Alias to :meth:`sidetable.SideTableAccessor.freq`.

        :param args: ``args`` forwarded to :meth:`sidetable.SideTableAccessor.freq`.
        :param kwargs: ``kwargs`` forwarded to :meth:`sidetable.SideTableAccessor.freq`.
        :return: The result of calling :meth:`sidetable.SideTableAccessor.freq` on the captured :class:`pandas.DataFrame`.
        """

        return self._df.stb.freq(*args, **kwargs)

    @property
    def msno(self):
        """
        Adapted `missingno` interface to work as a nested accessor.

        :return: An adapter class that provides access to the functions in `missingno`.
        """

        return _MissignoAdapter(self._df)
