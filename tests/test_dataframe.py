import pandas as pd
from pandas.testing import assert_frame_equal

from tests.test_common import DATA, DIRTY_COLUMN_NAMES, CLEAN_COLUMN_NAMES


def make_test_dfs():
    df = pd.DataFrame(DATA).T
    expected_df = df.copy()
    df.columns = DIRTY_COLUMN_NAMES
    expected_df.columns = CLEAN_COLUMN_NAMES
    return df, expected_df


def test_accessor_clean_names():
    df, expected_df = make_test_dfs()
    assert_frame_equal(df.bpw.clean_names, expected_df)
