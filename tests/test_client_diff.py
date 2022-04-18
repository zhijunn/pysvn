import pysvn
import pytest

svn = pysvn.Client(repository_dir='./tests/test_svn')

def test_diff():
    diff = svn.diff(1)
    assert len(diff.paths) > 0

def test_diff_1():
    diff = svn.diff(1, 3)
    assert len(diff.paths) > 0

def test_diff_error():
    with pytest.raises(pysvn.NoSuchRevisionError):
        svn.diff(999)

def test_diff_error_1():
    with pytest.raises(pysvn.NoSuchRevisionError):
        svn.diff(1, 999)
