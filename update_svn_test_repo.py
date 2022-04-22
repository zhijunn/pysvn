import subprocess
import pathlib

def main():
    path = str(pathlib.Path('tests/test_repo').resolve())
    cwd = str(pathlib.Path('tests/test_svn').resolve())
    filepath = ['svn', 'relocate', f'file://{path}']
    subprocess.Popen(filepath, cwd=cwd)

if __name__ == '__main__':
    main()