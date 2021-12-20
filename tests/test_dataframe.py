import pandas as pd
from pandas.testing import assert_frame_equal

from test_common import CLEAN_NAME_DATA, DIRTY_COLUMN_NAMES, CLEAN_COLUMN_NAMES


def make_test_dfs():
    df = pd.DataFrame(CLEAN_NAME_DATA).T
    expected_df = df.copy()
    df.columns = DIRTY_COLUMN_NAMES
    expected_df.columns = CLEAN_COLUMN_NAMES
    return df, expected_df


def test_accessor_clean_names():
    df, expected_df = make_test_dfs()
    assert_frame_equal(df.bpw.clean_names, expected_df)


def test_accessor_samp():
    df = pd.DataFrame(CLEAN_NAME_DATA).T
    df.columns = CLEAN_COLUMN_NAMES
    df_samp = df.bpw.samp(2)
    assert_frame_equal(df.loc[df_samp.columns.tolist(), :].T, df_samp)
