import pysvn
import pytest

def test_client():
    svn = pysvn.Client(cwd='./test_svn')
    print(svn.log())
    assert 1 == 1
