import pysvn
import pytest

svn = pysvn.Client(repository_dir='./tests/test_svn')

def test_log_1():
    logs = svn.log()
    assert len(logs) > 0

def test_log_with_file():
    logs = svn.log('noice/good_times.txt')
    assert len(logs) > 0

def test_log_revision_int():
    logs = svn.log(revision=1)
    assert len(logs) > 0

def test_log_revision_int_raises_error():
    with pytest.raises(pysvn.NoSuchRevisionError):
        svn.log(revision=999)

def test_log_revision_enum():
    logs = svn.log(revision=pysvn.Revision.BASE)
    assert len(logs) > 0

def test_log_revision_string():
    logs = svn.log(revision='1:3')
    assert len(logs) > 0

def test_log_revision_string_error_1():
    with pytest.raises(pysvn.RevisionSyntaxError):
        svn.log(revision='23dgh3246')

def test_log_revision_string_error_2():
    with pytest.raises(pysvn.NoSuchRevisionError):
        svn.log(revision='1:999')