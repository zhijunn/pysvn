from dataclasses import dataclass
from datetime import datetime
from enum import Enum

@dataclass
class LogEntry:
    '''SVN log entry.'''
    message: str
    author: str
    revision: str
    date: datetime

class Revision(Enum):
    HEAD = 'HEAD'
    BASE = 'BASE'
    COMMITTED = 'COMMITTED'
    PREV = 'PREV'
