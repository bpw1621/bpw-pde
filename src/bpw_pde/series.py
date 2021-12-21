"""Module for the :class:`pandas.Series` accessor class."""

import functools

from pandas import Series
from pandas.api.extensions import register_series_accessor

from bpw_pde import ACCESSOR_NAME
from bpw_pde.common import clean_name, md5, unicode_normalize, DEFAULT_UNICODE_NORMALIZATION_FORM


@register_series_accessor(ACCESSOR_NAME)
class SeriesAccessor:
    """Accessor class for :class:`pandas.Series`."""

    def __init__(self, series: Series) -> None:
        self._series = series

    @property
    def clean_name(self) -> Series:
        """
        Applies :meth:`bpw_pde.common.clean_name` to the name of the captured :class:`pandas.Series`.

        :return: The captured :class:`pandas.Series` with a cleaned name.
        """

        self._series.name = clean_name(self._series.name)
        return self._series

    @property
    def hashify(self) -> Series:
        """
        Applies :meth:`bpw_pde.common.md5` to the captured :class:`pandas.Series`.

        :return: The captured :class:`pandas.Series` MD5 hashes.
        """

        return self._series.apply(md5)

    def normalize(self, form: str = DEFAULT_UNICODE_NORMALIZATION_FORM) -> Series:
        """
        Applies :meth:`bpw_pde.common.normalize` to the captured :class:`pandas.Series`.

        :param form: Unicode normalization form, defaults to `'NFKC'`.
        :return: The Unicode normalized captured :class:`pandas.Series`.
        """

        return self._series.apply(functools.partial(unicode_normalize, form=form))
