from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto

@dataclass
class LogEntry:
    message: str
    author: str
    revision: str
    date: datetime

class Revision(Enum):
    HEAD = auto()
    BASE = auto()
    COMMITTED = auto()
    PREV = auto()
