'''A command line svn client.
'''

from pysvn.client import Client
from pysvn.utils import *
from pysvn.models import *
from pysvn.errors import *
from pysvn.constants import *


name = "pysvn"

__doc__ = """
A Python package that can operate svn, provide log, diff, numstat operation.
"""