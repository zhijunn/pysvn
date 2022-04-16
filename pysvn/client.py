from datetime import datetime
import subprocess
import os
import re
from typing import List, Union
import xml.etree.ElementTree
import pathlib

from errors import RepositoryDirDoesNotExistError, SVNNotInstalledError, NoSuchRevisionError, RevisionSyntaxError

from models import LogEntry, Revision

from utils import check_svn_installed

class Client:
    def __init__(self, repository_dir: str = os.getcwd()) -> None:
        self.diff_cache = {}

        if not check_svn_installed():
            raise SVNNotInstalledError('Is svn installed? If so, check that its in path.')

        repo_dir = pathlib.Path(repository_dir)
        if not repo_dir.exists():
            raise RepositoryDirDoesNotExistError('the repository_dir provided does not exist')
        if not repo_dir.is_dir():
            raise NotADirectoryError('the repository_dir provided is not a directory')

        self.cwd = str(repo_dir.resolve())
        

    def log(self, file: str = None, revision: Union[int, Revision, str] = Revision.HEAD) -> List[LogEntry]:
        revision = revision.name if type(revision) == Revision else revision
        log_cmd = f'svn log --xml --revision {revision}' if not file else f'svn log {file} --xml --revision {revision}'
        log_entries: List[LogEntry] = []
        cmd = subprocess.Popen(log_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.cwd)

        stderr = cmd.stderr.read()
        if stderr and 'No such revision' in stderr.decode('utf-8'):
            rev_num = err.split(' ')[-1]
            raise NoSuchRevisionError(f'no such revision {rev_num}')

        data = cmd.stdout.read()
        
        try:
            root = xml.etree.ElementTree.fromstring(data)

            for e in root.iter('logentry'):
                entry_info = {x.tag: x.text for x in list(e)}

                date = None
                if entry_info.get('date'):
                    date_str = entry_info.get('date').split('.', 1)[0]
                    date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')

                log_entry = LogEntry(
                    message=entry_info.get('msg'),
                    author=entry_info.get('author'),
                    revision=int(e.get('revision')),
                    date=date
                )

                log_entries.append(log_entry)

            return log_entries
        except xml.etree.ElementTree.ParseError:
            raise RevisionSyntaxError(f"with great power comes great responsibility, '{revision}' is not valid revision syntax")


    def diff(self, start_version, end_version = None, decoding = 'utf8', cache = False):
        if end_version is None:
            end_version = start_version
            start_version = end_version - 1

        diff_cmd = self.cmd + ["diff", "-r", "{0}:{1}".format(start_version, end_version)]

        if cache and self.diff_cache.setdefault(start_version, {})[end_version]:
            diff_content = self.diff_cache[start_version][end_version]
        else:
            diff_content = []
            data = subprocess.Popen(diff_cmd, stdout = self.stdout, cwd = self.cwd).stdout.read()
            for b in data.split(b'\n'):
                try:
                    diff_content.append(bytes.decode(b, decoding))
                except:
                    diff_content.append(bytes.decode(b))
                else:
                    pass

        diff_content = "\n".join(diff_content)

        if cache and self.diff_cache[start_version][end_version] is None:
            self.diff_cache[start_version][end_version] = diff_content

        return diff_content

    def numstat(self, start_version, end_version = None, decoding = 'utf8', cache = False):
        stat = []
        file_name = None

        diff_content = self.diff(start_version, end_version, decoding, cache)
        for s in diff_content.split('\n'):
            if s.startswith('+++'):
                if file_name:    
                    stat.append((added, removed, file_name))
                added = 0
                removed = 0
                file_name = re.match(r'\+\+\+ (\S+)', s).group(1)
            elif s.startswith('---'):
                pass
            elif s.startswith('+'):
                added = added + 1
            elif s.startswith('-'):
                removed = removed + 1

        if file_name:
            stat.append((added, removed, file_name))
        
        return stat


def main() -> None:
    svn = Client(repository_dir='../tests/test_svn')
    print(svn.log(revision='1:2'))

if __name__ == '__main__':
    main()
