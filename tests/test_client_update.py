import pysvn
import pytest

svn = pysvn.Client(repository_dir='./tests/test_svn')

def test_update_1():
    svn.update()
    
def test_update_2():
    svn.update(path='hello.txt')

def test_update_3():
    svn.update(path='hello.txt', revision=2)

def test_update_4():
    svn.update(path='noice/', revision=3)

def test_update_5():
    with pytest.raises(pysvn.NoSuchRevisionError):
        svn.update(path='hello.txt', revision=999)

def test_update_6():
    svn.update(depth=pysvn.Depth.INFINITY)
