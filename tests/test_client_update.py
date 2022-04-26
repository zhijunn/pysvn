import subprocess
import pysvn
import pytest

svn = pysvn.Client(repository_dir='./tests/test_svn')

def test_update_1():
    output = svn.update()
    assert 'At revision' in output or 'Updated to' in output
    
def test_update_2():
    output = svn.update(path='hello.txt')
    assert 'At revision' in output

def test_update_3():
    output = svn.update(path='PPF8HXI', revision=22)
    assert 'Updated to revision' in output or 'At revision' in output

def test_update_4():
    output = svn.update(path='noice/Q68R9F6', revision=20)
    assert "Updating 'noice/Q68R9F6':" in output

def test_update_5():
    with pytest.raises(pysvn.NoSuchRevisionError):
        svn.update(path='hello.txt', revision=999)

def test_update_9():
    output = svn.update(path=['8TN0DX', 'PPF8HXI', 'noice/good_times.txt'], accept=pysvn.CRAction.THEIRS_CONFLICT)
    assert 'Summary of updates' in output and len(output.split('\n')) > 7

def test_update_10():
    output = svn.update()
    assert 'At revision' in output
