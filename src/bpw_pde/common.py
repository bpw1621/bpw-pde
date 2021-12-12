import string

PUNCTUATION_TO_SPACE_TRANSLATOR = str.maketrans(string.punctuation, ' ' * len(string.punctuation))


def clean_name(name: str):
    return '_'.join(name.lower().translate(PUNCTUATION_TO_SPACE_TRANSLATOR).split())
