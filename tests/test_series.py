import pandas as pd
from pandas.testing import assert_series_equal

from bpw_pde.common import clean_name

DATA = [1, 2, 3]


def make_test_series():
    series = pd.Series(DATA, name=' Foo!  ')
    expected_series = pd.Series(DATA, name='foo')
    return series, expected_series


def test_accessor_clean_names():
    series, expected_series = make_test_series()
    assert_series_equal(series.bpw.clean_name, expected_series)
