import pysvn
import pytest

svn = pysvn.Client(repository_dir='./tests/test_svn')

def test_cleanup():
    svn.cleanup()