from ..spk.types import SPK_SOCKET, SPK_CACHE_LINE_SIZE, STimespecT
from ..spk.data_buffer_define import _SDataBufferVar
from ..spk.socket_base_define import SPK_MAX_URI_LEN, SSocketChannelInfoT, SSocketOptionConfigT

from ..utils import BaseStructure, BaseUnion
from ..utils.types import *


GENERAL_CLI_MAX_REMOTE_CNT = 8
GENERAL_CLI_MAX_CHANNEL_GROUP_SIZE = 256
GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE = 128
GENERAL_CLI_MAX_NAME_LEN = 32
GENERAL_CLI_MAX_PWD_LEN = 40
GENERAL_CLI_MAX_COMP_ID_LEN = 32


class _SocketFd(BaseUnion):
    _fields_ = [
        ('socketFd', SPK_SOCKET),
        ('__socket_fd_filler', c_uint64),
    ]


class _ReserveData(BaseUnion):
    _fields_ = [
        ('buf', c_char * GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE),
        ('i8', c_int8 * GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE),
        ('u8', c_uint8 * GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE),
        ('i16', c_int16 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 2)),
        ('u16', c_uint16 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 2)),
        ('i32', c_int32 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 4)),
        ('u32', c_uint32 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 4)),
        ('i64', c_int64 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 8)),
        ('u64', c_uint64 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 8)),
        ('ptr', c_void_p * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 8)),
        ('__padding', c_char * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE + SPK_CACHE_LINE_SIZE)),
    ]


class _ExtData(BaseUnion):
    _fields_ = [
        ('buf', c_char * GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE),
        ('i8', c_int8 * GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE),
        ('u8', c_uint8 * GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE),
        ('i16', c_int16 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 2)),
        ('u16', c_uint16 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 2)),
        ('i32', c_int32 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 4)),
        ('u32', c_uint32 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 4)),
        ('i64', c_int64 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 8)),
        ('u64', c_uint64 * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 8)),
        ('ptr', c_void_p * (GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE // 8)),
    ]


class SGeneralClientChannelT(BaseStructure):
    _fields_ = [
        ('socketFd', _SocketFd),

        ('heartBtInt', c_int32),
        ('testReqInt', c_int32),
        ('protocolType', c_uint8),
        ('remoteSetNum', c_uint8),
        ('remoteHostNum', c_uint8),
        ('remoteIsLeader', c_uint8),
        ('leaderHostNum', c_uint8),
        ('__filler1', c_uint8 * 3),

        ('__codecBuf', _SDataBufferVar),
        ('__recvBuf', _SDataBufferVar),
        ('__pDataStartPoint', c_char_p),
        ('__contextPtr', c_void_p),
        ('__monitorPtr', c_void_p),
        ('__customPtr', c_void_p),
        ('__reavedSize', c_int32),
        ('__customFlag', c_int32),
        ('__totalInMsgSize', c_int64),
        ('__totalCompressedSize', c_int64),
        ('__totalDecompressSize', c_int64),

        ('firstInMsgSeq', c_uint64),
        ('lastInMsgSeq', c_uint64),
        ('nextInMsgSeq', c_uint64),
        ('lastRecvTime', STimespecT),

        ('channel', SSocketChannelInfoT),
        ('nextOutMsgSeq', c_uint64),
        ('lastOutMsgSeq', c_uint64),
        ('lastSendTime', STimespecT),

        ('senderCompId', c_char * GENERAL_CLI_MAX_COMP_ID_LEN),
        ('targetCompId', c_char * GENERAL_CLI_MAX_COMP_ID_LEN),

        ('__magicNumber', c_int32),  # 标识会话结构是否已经正确初始化过
        ('__clientId', c_int32),  # 客户端编号
        ('__channelType', c_uint8),  # 通道类型
        ('__clEnvId', c_int8),  # 客户端环境号
        ('__groupFlag', c_uint8),  # 通道组标志
        ('__protocolHints', c_uint8),  # 协议约定信息
        ('__businessType', c_uint8),  # 通道对应的业务类型
        ('__lastConnectAddrIdx', c_uint8),  # 最近一次连接的主机地址顺序号
        ('__filler', c_uint8 * 2),  # 按64位对齐填充域
        ('__reserveData', _ReserveData),
        ('__extData', _ExtData),
    ]


class _SPollfdT(BaseStructure):
    _fields_ = [
        ('fd', c_int32),
        ('events', c_int16),
        ('revents', c_int16),
    ]


class SGeneralClientChannelGroupT(BaseStructure):
    _fields_ = [
        ('channelCount', c_int32),
        ('__customFlag', c_int32),
        ('channelList', POINTER(SGeneralClientChannelT) * GENERAL_CLI_MAX_CHANNEL_GROUP_SIZE),

        ('__maxFd', c_int32),
        ('__maxFdCnt', c_int16),
        ('__groupFlag', c_uint8),
        ('__filler', c_uint8),
        ('__fdArray', _SPollfdT * GENERAL_CLI_MAX_CHANNEL_GROUP_SIZE),
    ]


class SGeneralClientAddrInfoT(BaseStructure):
    _fields_ = [
        ('uri', c_char * SPK_MAX_URI_LEN),
        ('targetCompId', c_char * GENERAL_CLI_MAX_COMP_ID_LEN),
        ('username', c_char * GENERAL_CLI_MAX_NAME_LEN),
        ('password', c_char * GENERAL_CLI_MAX_PWD_LEN),
        ('hostNum', c_uint8),
        ('__filler', c_uint8 * 7),
    ]


class SGeneralClientRemoteCfgT(BaseStructure):
    _fields_ = [
        ('addrCnt', c_int32),
        ('heartBtInt', c_int32),
        ('clusterType', c_uint8),
        ('clEnvId', c_int8),
        ('targetSetNum', c_uint8),
        ('businessType', c_uint8),
        ('__filler', c_uint8 * 4),

        ('senderCompId', c_char * GENERAL_CLI_MAX_COMP_ID_LEN),
        ('targetCompId', c_char * GENERAL_CLI_MAX_COMP_ID_LEN),
        ('username', c_char * GENERAL_CLI_MAX_NAME_LEN),
        ('password', c_char * GENERAL_CLI_MAX_PWD_LEN),

        ('addrList', SGeneralClientAddrInfoT * GENERAL_CLI_MAX_REMOTE_CNT),
        ('socketOpt', SSocketOptionConfigT),
    ]


class SGeneralClientAddrCursorT(BaseStructure):
    _fields_ = [
        ('addrCnt', c_int32),
        ('lastConnectIdx', c_int32),
        ('lastConnectResult', c_int32),
        ('lastHostNum', c_uint8),
        ('isLast', c_uint8),
        ('__filler1', c_uint8 * 2),
        ('socketFd', _SocketFd),
        ('pLastAddrInfo', POINTER(SGeneralClientAddrInfoT)),
        ('__filler2', c_void_p),
    ]
