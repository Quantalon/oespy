from ..spk.types import SPK_SOCKET

from ..utils import BaseStructure, BaseUnion
from ..utils.types import *


SPK_MAX_IP_LEN = 16
SPK_MAX_URI_LEN = 128

SPK_DEFAULT_SO_TIMEOUT_MS = 15000


class _SocketFd(BaseUnion):
    _fields_ = [
        ('socketFd', SPK_SOCKET),
        ('__socket_fd_filler', c_uint64),
    ]


class SSocketChannelInfoT(BaseStructure):
    _fields_ = [
        ('socketFd', _SocketFd),
        ('remotePort', c_int32),
        ('origRemoteIp', c_uint32),
        ('protocolType', c_uint8),
        ('_isNetByteOrder', c_uint8),
        ('_isBroken', c_uint8),
        ('_isSendBroken', c_uint8),
        ('_isTryConnecting', c_uint8),
        ('__filler', c_uint8 * 3),
        ('connectTime', c_int64),
        ('remoteAddr', c_char * SPK_MAX_URI_LEN),
    ]


class SSocketOptionConfigT(BaseStructure):
    _fields_ = [
        ('soRcvbuf', c_int32),
        ('soSndbuf', c_int32),

        ('tcpNodelay', c_int8),
        ('quickAck', c_int8),

        ('mcastTtlNum', c_int8),
        ('mcastLoopbackDisabled', c_int8),

        ('soBacklog', c_uint16),
        ('connTimeoutMs', c_uint16),

        ('keepIdle', c_int16),
        ('keepIntvl', c_int16),
        ('keepalive', c_int8),
        ('keepCnt', c_int8),

        ('disableReuseAddr', c_int8),
        ('enableReusePort', c_int8),
        ('__filler', c_int8 * 4),

        ('localSendingPort', c_int32),
        ('localSendingIp', c_char * (SPK_MAX_IP_LEN + 4)),
        ('mcastInterfaceIp', c_char * (SPK_MAX_IP_LEN + 4)),
    ]
