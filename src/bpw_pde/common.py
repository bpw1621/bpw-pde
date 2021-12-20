import hashlib
import string
import unicodedata

PUNCTUATION_TO_SPACE_TRANSLATOR = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
DEFAULT_UNICODE_NORMALIZATION_FORM = 'NFKC'


def clean_name(name: str):
    return '_'.join(name.lower().translate(PUNCTUATION_TO_SPACE_TRANSLATOR).split())


def md5(text: str):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def unicode_normalize(text: str, form: str = DEFAULT_UNICODE_NORMALIZATION_FORM):
    return unicodedata.normalize(form, text)
