import subprocess

def main():
    subprocess.Popen('svn relocate file:///home/runner/work/pysvn/pysvn/tests/test_repo', cwd='tests/test_svn')

if __name__ == '__main__':
    main()