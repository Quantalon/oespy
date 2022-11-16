from enum import Enum

from ..utils import BaseStructure
from ..utils.types import *


class eSMsgProtocolTypeT(Enum):
    SMSG_PROTO_BINARY = 0x00
    SMSG_PROTO_JSON = 0x01
    SMSG_PROTO_FIX = 0x02
    SMSG_PROTO_PROTOBUF = 0x03


class eSMsgFlagT(Enum):
    SMSG_MSGFLAG_NONE = 0x00
    SMSG_MSGFLAG_REQ = 0x00
    SMSG_MSGFLAG_RSP = 0x50
    SMSG_MSGFLAG_NESTED = 0x20
    SMSG_MSGFLAG_COMPRESSED = 0x80

    SMSG_MSGFLAG_MASK_RSPFLAG = 0xF0
    SMSG_MSGFLAG_MASK_PROTOCOL = 0x0F


class SMsgHeadT(BaseStructure):
    _fields_ = [
        ('msgFlag', c_uint8),
        ('msgId', c_uint8),
        ('status', c_uint8),
        ('detailStatus', c_uint8),
        ('msgSize', c_int32),
    ]
