"""Top-level bpw_pde package."""

import logging
from logging import NullHandler

from .dataframe import DataframeAccessor
from .index import IndexAccessor
from .series import SeriesAccessor

__author__ = 'Bryan Patrick Wood'
__email__ = 'bpw1621@gmail.com'
__version__ = '0.0a0'

logging.getLogger(__name__).addHandler(NullHandler())

ACCESSOR_NAME = 'bpw'
