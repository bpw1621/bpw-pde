import pytest

from bpw_pde.common import clean_name

DIRTY_COLUMN_NAMES = (' country      ', 'Phone Number', 'Dollar Amount (USD $)',)
CLEAN_COLUMN_NAMES = ('country', 'phone_number', 'dollar_amount_usd',)
DATA = [
    ['US', 'RU', 'TW', 'IS'],
    ['+01-301-555-8675', '+7 401 678 2741', '+886 4 5963 3071', '+354 276 5714'],
    ['12.34', '7.77', '123.45', '987.34']
]


@pytest.mark.parametrize('name,expected', zip(DIRTY_COLUMN_NAMES, CLEAN_COLUMN_NAMES))
def test_clean_name(name, expected):
    assert clean_name(name) == expected
