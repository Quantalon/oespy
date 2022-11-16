from ..utils import BaseStructure, BaseUnion
from ..utils.types import *

BOOL = c_int32
TRUE = 1
FALSE = 0

SPK_SOCKET = c_int32

SPK_CACHE_LINE_SIZE = 64


class STimespecT(BaseStructure):
    _fields_ = [
        ('tv_sec', c_int32),
        ('tv_nsec', c_int32),
    ]


class STimespec32T(BaseStructure):
    _fields_ = [
        ('tv_sec', c_int32),
        ('tv_nsec', c_int32),
    ]


SPK_MAX_PATH_LEN = 256
