"""Top-level bpw_pde package."""

import logging
from logging import NullHandler

from tqdm.autonotebook import tqdm

__author__ = 'Bryan Patrick Wood'
__email__ = 'bpw1621@gmail.com'
__version__ = '0.0a3'

logging.getLogger(__name__).addHandler(NullHandler())
tqdm.pandas()

ACCESSOR_NAME = 'bpw'

from .dataframe import DataframeAccessor
from .index import IndexAccessor
from .series import SeriesAccessor
