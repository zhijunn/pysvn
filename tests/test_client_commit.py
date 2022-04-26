import pysvn
import pytest
import random

svn = pysvn.Client(repository_dir='./tests/test_svn')

def test_commit():
    output = svn.commit(f'a great automated commit message! Number {random.randint(1, 99999)}')
    print(output)

def test_commit_1():
    output = svn.commit(f'Automated second commit!', path='hello.txt')
    print(output)

def test_commit_2():
    with open('tests/test_svn/8TN0DX', 'a') as f:
        f.write(f'\nAutomated test commit 2 number {random.randint(1, 99999)}\n')
    output = svn.commit('Automated hello second commit', path='8TN0DX')
    print(output)

def test_commit_3():
    with open('tests/test_svn/CWTMNBGK', 'a') as f:
        f.write(f'\nAutomated test commit 3 number {random.randint(1, 99999)}\n')
    output = svn.commit('Automated hello third commit', path='CWTMNBGK', no_unlock=True)
    print(output)

def test_commit_4():
    output = svn.commit('Automated commit test 4', include_externals=True, depth=pysvn.Depth.IMMEDIATES)
    print(output)
