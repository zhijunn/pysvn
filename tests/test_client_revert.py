import pysvn
import pytest
import os
import pathlib
import subprocess

svn = pysvn.Client(repository_dir='./tests/test_svn')

def test_revert():
    with open('./tests/test_svn/noice/good_times.txt', 'a') as f:
        f.write('\n' * 10)
        f.write('test')
    try:
        out = svn.revert('noice/good_times.txt')
        assert len(out) > 0
    except pysvn.PreviousOperationNotFinishedError:
        subprocess.Popen(['svn', 'cleanup'], cwd='tests/test_svn', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.Popen(['svn', 'cleanup', '--vacuum-pristines'], cwd='tests/test_svn', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = svn.revert('noice/good_times.txt')
        assert len(out) > 0
    
def test_revert_recursive():
    with open('./tests/test_svn/noice/good_times.txt', 'a') as f:
        f.write('\n' * 10)
        f.write('test')
    with open('./tests/test_svn/noice/thing.txt', 'a') as f:
        f.write('\n' * 10)
        f.write('test')
    
    try:
        out = svn.revert('noice', recursive=True)
        assert len(out.split('\n')) > 0
    except pysvn.PreviousOperationNotFinishedError:
        subprocess.Popen(['svn', 'cleanup'], cwd='tests/test_svn', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.Popen(['svn', 'cleanup', '--vacuum-pristines'], cwd='tests/test_svn', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = svn.revert('noice', recursive=True)
        assert len(out.split('\n')) > 0
    