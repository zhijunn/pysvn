import pysvn
import time

svn = pysvn.Client(repository_dir='./tests/test_svn')

def test_revert():
    with open('./tests/test_svn/noice/good_times.txt', 'a') as f:
        f.write('\n' * 10)
        f.write('test')
    out = svn.revert('noice/good_times.txt')
    assert len(out) > 0
    
def test_revert_recursive():
    with open('tests/test_svn/noice/5SNAX1ED', 'a') as f:
        f.write('\n' * 10)
        f.write('test')
    with open('tests/test_svn/noice/CHVRYXG', 'a') as f:
        f.write('\n' * 10)
        f.write('test')
    out = svn.revert('noice', recursive=True)
    time.sleep(3)
    assert len(out.split('\n')) > 0
    