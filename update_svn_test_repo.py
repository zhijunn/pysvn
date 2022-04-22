import subprocess
import pathlib

def main():
    path = str(pathlib.Path('tests/test_repo').resolve())
    cwd = str(pathlib.Path('tests/test_svn').resolve())
    subprocess.Popen(f'svn relocate file://{path}', cwd=cwd)

if __name__ == '__main__':
    main()