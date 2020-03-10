from enum import Enum


class EnumUpdateRequestStatus(Enum):
    pending = 1
    cancelled = 2
    finished = 3
