import pysvn
import pytest

def test_client_creation():
    svn = pysvn.Client()
    assert svn != None

def test_client_creation_bad_url():
    with pytest.raises(pysvn.RepositoryDirDoesNotExistError):
        pysvn.Client(repository_dir='lkjsdfjsdfsfdkl')

def test_client_creation_not_a_dir_error():
    with pytest.raises(NotADirectoryError):
        pysvn.Client(repository_dir='./tests/test_svn/hello.txt')