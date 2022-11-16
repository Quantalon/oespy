from ..utils import BaseStructure, BaseUnion
from ..utils.types import *
from .general_client_define import GENERAL_CLI_MAX_NAME_LEN, GENERAL_CLI_MAX_SESSION_EXTDATA_SIZE
from .general_client_define import SGeneralClientRemoteCfgT, SGeneralClientChannelT
from .types import SPK_MAX_PATH_LEN


SPK_ENDPOINT_MAX_REMOTE_CNT = 128


class _CustomData(BaseUnion):
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


# forward declaration
class SEndpointChannelT(BaseStructure):
    pass


F_GENERAL_CLI_ON_MSG_T = CFUNCTYPE(
    c_int32,
    POINTER(SGeneralClientChannelT),
    c_void_p,
    c_void_p
)

F_SPK_ENDPOINT_ON_CONNECT_T = CFUNCTYPE(
    c_int32,
    POINTER(SEndpointChannelT),
    c_void_p,
)

F_SPK_ENDPOINT_ON_DISCONNECT_T = CFUNCTYPE(
    c_int32,
    POINTER(SEndpointChannelT),
    c_void_p,
)


class SEndpointChannelCfgT(BaseStructure):
    _fields_ = [
        ('channelIndex', c_int32),
        ('channelType', c_int32),
        ('channelTag', c_char * GENERAL_CLI_MAX_NAME_LEN),

        ('remoteCfg', SGeneralClientRemoteCfgT),

        ('fnOnMsg', F_GENERAL_CLI_ON_MSG_T),
        ('pOnMsgParams', c_void_p),

        ('fnOnConnect', F_SPK_ENDPOINT_ON_CONNECT_T),
        ('pOnConnectParams', c_void_p),

        ('fnOnDisconnect', F_SPK_ENDPOINT_ON_DISCONNECT_T),
        ('pOnDisconnectParams', c_void_p),

        ('customData', _CustomData),
    ]


class SEndpointIoThreadCfgT(BaseStructure):
    _fields_ = [
        ('enable', c_uint8),
        ('isOutputSimplify', c_uint8),
        ('isAppendMode', c_uint8),
        ('isIoThreadBusyPollAble', c_uint8),
        ('dataOutputFormat', c_int32),
        ('dataOutputPath', c_char * SPK_MAX_PATH_LEN),
        ('statsOutputPath', c_char * SPK_MAX_PATH_LEN),
    ]


class SEndpointContextT(BaseStructure):
    _fields_ = [
        ('pInternalRefs', c_void_p),
        ('__filler', c_void_p),
        ('terminateFlag', c_uint8),
        ('__filler2', c_uint8 * 7),
    ]


SEndpointChannelT._fields_ = [
        ('pSessionInfo', POINTER(SGeneralClientChannelT)),
        ('pContext', POINTER(SEndpointContextT)),

        ('pChannelCfg', POINTER(SEndpointChannelCfgT)),
        ('pExtChannelCfg', c_void_p),

        ('isConnected', c_uint8),
        ('protocolType', c_uint8),
        ('isUdpChannel', c_uint8),
        ('__filler', c_uint8 * 5),

        ('lastInMsgSeq', c_int64),
        ('lastOutMsgSeq', c_int64),
    ]
