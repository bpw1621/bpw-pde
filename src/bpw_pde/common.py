"""Common functions used across the index, series, and dataframe modules."""

import hashlib
import string
import unicodedata

PUNCTUATION_TO_SPACE_TRANSLATOR = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
DEFAULT_UNICODE_NORMALIZATION_FORM = 'NFKC'


def clean_name(name: str) -> str:
    """
    Applies lowercasing, whitespace tokenization, and rejoining tokens with underscore to ``name``.

    :param name: The name to be cleaned.
    :return: The cleaned name.
    """
    return '_'.join(name.lower().translate(PUNCTUATION_TO_SPACE_TRANSLATOR).split())


def md5(text: str) -> str:
    """
    Computes the MD5 hash of ``text``.

    :param text: The text to be hashed using the MD5 hashing algorithm.
    :return: The MD5 hash of the text.
    """
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def unicode_normalize(text: str, form: str = DEFAULT_UNICODE_NORMALIZATION_FORM) -> str:
    """
    Applies Unicode normalization on ``text`` using the form ``form``.

    :param text: The text to be normalized.
    :param form: The Unicode normalization form to use for normalization.
    :return: The Unicode normalized text.
    """
    return unicodedata.normalize(form, text)
