from ..utils import BaseStructure
from ..utils.types import *


class _SDataBufferVar(BaseStructure):
    _fields_ = [
        ('dataSize', c_int32),
        ('bufSize', c_int32),
        ('buffer', c_char_p),
        ('__ref', c_void_p),
    ]