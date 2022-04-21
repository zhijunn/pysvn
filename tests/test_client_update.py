import pysvn
import pytest

svn = pysvn.Client(repository_dir='./tests/test_svn')

def test_update_1():
    output = svn.update()
    assert 'At revision' in output
    
def test_update_2():
    output = svn.update(path='hello.txt')
    assert 'At revision' in output

def test_update_3():
    output = svn.update(path='hello.txt', revision=2)
    assert 'Updated to revision' in output

def test_update_4():
    output = svn.update(path='noice/', revision=3)
    assert "Updating 'noice':" in output and 'Updated to revision' in output

def test_update_5():
    with pytest.raises(pysvn.NoSuchRevisionError):
        svn.update(path='hello.txt', revision=999)

def test_update_6():
    output = svn.update(depth=pysvn.Depth.INFINITY)
    assert len(output.split('\n')) > 5

def test_update_7():
    output = svn.update(depth=pysvn.Depth.FILES)
    assert 'At revision' in output

def test_update_8():
    output = svn.update(path='8TN0DX')
    assert '8TN0DX' in output

def test_update_9():
    output = svn.update(path=['8TN0DX', 'PPF8HXI', 'noice/good_times.txt'], accept=pysvn.CRAction.THEIRS_CONFLICT)
    assert 'Summary of updates' in output and len(output.split('\n')) > 7

def test_update_10():
    output = svn.update()
    assert 'At revision' in output
