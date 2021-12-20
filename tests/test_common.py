import pytest

from bpw_pde.common import clean_name, md5, unicode_normalize

DIRTY_COLUMN_NAMES = (' country      ', 'Phone Number', 'Dollar Amount (USD $)',)
CLEAN_COLUMN_NAMES = ('country', 'phone_number', 'dollar_amount_usd',)
CLEAN_NAME_DATA = [
    ['US', 'RU', 'TW', 'IS'],
    ['+01-301-555-8675', '+7 401 678 2741', '+886 4 5963 3071', '+354 276 5714'],
    ['12.34', '7.77', '123.45', '987.34'],
]
MD5_DATA = [
    ('Hello, I love you won\'t you tell me your name?', '41cfd1d06604733c5a40e89f71244537'),
    ('Riders on the storm ...', '206715483326fe890cd7151c0ff4e9aa'),
    ('Come on, baby, light my fire', 'feac31e22feec0a789bd98b0cebea8ad'),
]
UNICODE_NORMALIZE_DATA = [
    ('This should be a noop', 'This should be a noop'),
    ('Ⅷ', 'VIII'),
    ('ϔ', 'Ϋ'),
]


@pytest.mark.parametrize('name,expected', zip(DIRTY_COLUMN_NAMES, CLEAN_COLUMN_NAMES))
def test_clean_name(name: str, expected: str):
    assert clean_name(name) == expected


@pytest.mark.parametrize('text,expected', MD5_DATA)
def test_md5(text: str, expected: str):
    assert md5(text) == expected


@pytest.mark.parametrize('text,expected', UNICODE_NORMALIZE_DATA)
def test_unicode_normalize(text: str, expected: str):
    assert unicode_normalize(text) == expected
