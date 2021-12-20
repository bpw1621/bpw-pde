import pandas as pd
from pandas.testing import assert_series_equal

from test_common import MD5_DATA, UNICODE_NORMALIZE_DATA


def make_clean_name_test_series():
    data = [1, 2, 3]
    series = pd.Series(data, name=' Foo!  ')
    expected_series = pd.Series(data, name='foo')
    return series, expected_series


def test_accessor_clean_names():
    series, expected_series = make_clean_name_test_series()
    assert_series_equal(series.bpw.clean_name, expected_series)


def test_accessor_md5():
    df = pd.DataFrame(MD5_DATA, columns=['text', 'expected'])
    assert_series_equal(df.text.bpw.hashify, df.expected, check_names=False)


def test_accessor_unicode_normalize():
    df = pd.DataFrame(UNICODE_NORMALIZE_DATA, columns=['text', 'expected'])
    assert_series_equal(df.text.bpw.normalize(), df.expected, check_names=False)
