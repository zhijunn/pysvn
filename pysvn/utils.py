'''pysvn utilities module.
'''
import subprocess

def check_svn_installed() -> bool:
    """Check if the current system has the svn cli client installed.

    Returns:
        bool: True if svn is installed, otherwise False
    """
    try:
        subprocess.run('svn', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False
