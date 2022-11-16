from enum import Enum
from ctypes import cdll, byref, create_string_buffer

from ..spk.global_packet import SMsgHeadT
from ..spk.general_client_define import (SGeneralClientChannelT, SGeneralClientChannelGroupT, SGeneralClientAddrInfoT,
                                         SGeneralClientRemoteCfgT, SGeneralClientAddrCursorT, SSocketOptionConfigT)
from ..spk.types import BOOL
from ..utils import LIB_PATH, BaseStructure
from ..utils.types import *
from .mkt_packets import MDS_APPL_VER_ID
from .mkt_packets import MdsMktDataRequestReqBufT, MdsMktDataSnapshotT
from .qry_packets import (MdsQryCursorT, MdsQryStockStaticInfoListFilterT, MdsQryOptionStaticInfoListFilterT,
                          MdsQrySnapshotListFilterT)


MDSAPI_CFG_DEFAULT_SECTION = "mds_client"
MDSAPI_CFG_DEFAULT_SECTION_LOGGER = "log"

MDSAPI_CFG_DEFAULT_KEY_TCP_ADDR = "tcpServer"
MDSAPI_CFG_DEFAULT_KEY_QRY_ADDR = "qryServer"

MDSAPI_CFG_DEFAULT_KEY_UDP_ADDR_SNAP1 = "udpServer.Snap1"
MDSAPI_CFG_DEFAULT_KEY_UDP_ADDR_SNAP2 = "udpServer.Snap2"

MDSAPI_CFG_DEFAULT_KEY_UDP_ADDR_TICK1 = "udpServer.Tick1"
MDSAPI_CFG_DEFAULT_KEY_UDP_ADDR_TICK2 = "udpServer.Tick2"

MDSAPI_DEFAULT_HEARTBEAT_INTERVAL = 30
MDSAPI_DEFAULT_UDP_HEARTBEAT_INTERVAL = 10

MDSAPI_DEFAULT_STRING_DELIM = ",;| \t\r\n"


class eMdsApiChannelTypeT(Enum):
    MDSAPI_CHANNEL_TYPE_TCP = 11
    MDSAPI_CHANNEL_TYPE_UDP = 12
    MDSAPI_CHANNEL_TYPE_QUERY = 13


MdsApiSessionInfoT = SGeneralClientChannelT
MdsApiChannelGroupT = SGeneralClientChannelGroupT
MdsApiAddrInfoT = SGeneralClientAddrInfoT
MdsApiRemoteCfgT = SGeneralClientRemoteCfgT
MdsApiAddrCursorT = SGeneralClientAddrCursorT
MdsApiSubscribeInfoT = MdsMktDataRequestReqBufT


class MdsApiClientCfgT(BaseStructure):
    _fields_ = [
        ('tcpChannelCfg', MdsApiRemoteCfgT),
        ('qryChannelCfg', MdsApiRemoteCfgT),
        ('udpSnap1ChannelCfg', MdsApiRemoteCfgT),
        ('udpSnap2ChannelCfg', MdsApiRemoteCfgT),
        ('udpTick1ChannelCfg', MdsApiRemoteCfgT),
        ('udpTick2ChannelCfg', MdsApiRemoteCfgT),
        ('subscribeInfo', MdsApiSubscribeInfoT),
    ]


class MdsApiClientEnvT(BaseStructure):
    _fields_ = [
        ('tcpChannel', MdsApiSessionInfoT),
        ('qryChannel', MdsApiSessionInfoT),
        ('udpSnap1Channel', MdsApiSessionInfoT),
        ('udpSnap2Channel', MdsApiSessionInfoT),
        ('udpTick1Channel', MdsApiSessionInfoT),
        ('udpTick2Channel', MdsApiSessionInfoT),
        ('udpChannelGroup', MdsApiChannelGroupT),
    ]


F_MDSAPI_ONMSG_T = CFUNCTYPE(
    c_int32,
    POINTER(MdsApiSessionInfoT),
    POINTER(SMsgHeadT),
    c_void_p,
    c_void_p
)


F_MDSAPI_ON_QRY_MSG_T = CFUNCTYPE(
    c_int32,
    POINTER(MdsApiSessionInfoT),
    POINTER(SMsgHeadT),
    c_void_p,
    POINTER(MdsQryCursorT),
    c_void_p
)


class MdsApi:
    def __init__(self):
        self.api = cdll.LoadLibrary(LIB_PATH)
        self.client_env = MdsApiClientEnvT()

        self.tcp_channel = self.client_env.tcpChannel
        self.qry_channel = self.client_env.qryChannel

        self.udp_channel_group = self.client_env.udpChannelGroup

        self._MdsApi_GetErrorMsg = self.api.MdsApi_GetErrorMsg
        self._MdsApi_GetErrorMsg.restype = c_char_p
        self._MdsApi_GetErrorMsg.argtypes = [c_int32]

        self._MdsApi_GetApiVersion = self.api.MdsApi_GetApiVersion
        self._MdsApi_GetApiVersion.restype = c_char_p

        self._MdsApi_InitAll = self.api.MdsApi_InitAll
        self._MdsApi_InitAll.restype = BOOL
        self._MdsApi_InitAll.argtypes = [
            POINTER(MdsApiClientEnvT),
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
        ]

        self._MdsApi_InitTcpChannel = self.api.MdsApi_InitTcpChannel
        self._MdsApi_InitTcpChannel.restype = BOOL
        self._MdsApi_InitTcpChannel.argtypes = [
            POINTER(MdsApiSessionInfoT),
            c_char_p,
            c_char_p,
            c_char_p,
        ]

        self._MdsApi_DestoryAll = self.api.MdsApi_DestoryAll
        self._MdsApi_DestoryAll.argtypes = [POINTER(MdsApiClientEnvT)]

        self._MdsApi_WaitOnMsg = self.api.MdsApi_WaitOnMsg
        self._MdsApi_WaitOnMsg.restype = c_int32
        self._MdsApi_WaitOnMsg.argtypes = [
            POINTER(MdsApiSessionInfoT),
            c_int32,
            F_MDSAPI_ONMSG_T,
            c_void_p
        ]

        self._MdsApi_GetLastRecvTime = self.api.MdsApi_GetLastRecvTime
        self._MdsApi_GetLastRecvTime.restype = c_int64
        self._MdsApi_GetLastRecvTime.argtypes = [POINTER(MdsApiSessionInfoT)]

        self._MdsApi_SetThreadSubscribeTickType = self.api.MdsApi_SetThreadSubscribeTickType
        self._MdsApi_SetThreadSubscribeTickType.argtypes = [c_int32]

        self._MdsApi_SetThreadSubscribeTickRebuildFlag = self.api.MdsApi_SetThreadSubscribeTickRebuildFlag
        self._MdsApi_SetThreadSubscribeTickRebuildFlag.argtypes = [c_int32]

        self._MdsApi_SetThreadSubscribeRequireInitMd = self.api.MdsApi_SetThreadSubscribeRequireInitMd
        self._MdsApi_SetThreadSubscribeRequireInitMd.argtypes = [BOOL]

        self._MdsApi_SubscribeByString = self.api.MdsApi_SubscribeByString
        self._MdsApi_SubscribeByString.restype = BOOL
        self._MdsApi_SubscribeByString.argtypes = [
            POINTER(MdsApiSessionInfoT),
            c_char_p,
            c_char_p,
            c_uint8,
            c_uint8,
            c_uint8,
            c_int32,
        ]

        self._MdsApi_SubscribeByStringAndPrefixes = self.api.MdsApi_SubscribeByStringAndPrefixes
        self._MdsApi_SubscribeByStringAndPrefixes.restype = BOOL
        self._MdsApi_SubscribeByStringAndPrefixes.argtypes = [
            POINTER(MdsApiSessionInfoT),
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            c_uint8,
            c_uint8,
            c_int32,
        ]

        self._MdsApi_QueryStockStaticInfoList = self.api.MdsApi_QueryStockStaticInfoList
        self._MdsApi_QueryStockStaticInfoList.restype = c_int32
        self._MdsApi_QueryStockStaticInfoList.argtypes = [
            POINTER(MdsApiSessionInfoT),
            c_char_p,
            c_char_p,
            POINTER(MdsQryStockStaticInfoListFilterT),
            F_MDSAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._MdsApi_QueryOptionStaticInfoList = self.api.MdsApi_QueryOptionStaticInfoList
        self._MdsApi_QueryOptionStaticInfoList.restype = c_int32
        self._MdsApi_QueryOptionStaticInfoList.argtypes = [
            POINTER(MdsApiSessionInfoT),
            c_char_p,
            c_char_p,
            POINTER(MdsQryOptionStaticInfoListFilterT),
            F_MDSAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._MdsApi_QuerySnapshotList = self.api.MdsApi_QuerySnapshotList
        self._MdsApi_QuerySnapshotList.restype = c_int32
        self._MdsApi_QuerySnapshotList.argtypes = [
            POINTER(MdsApiSessionInfoT),
            c_char_p,
            c_char_p,
            POINTER(MdsQrySnapshotListFilterT),
            F_MDSAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._MdsApi_QueryMktDataSnapshot = self.api.MdsApi_QueryMktDataSnapshot
        self._MdsApi_QueryMktDataSnapshot.restype = c_int32
        self._MdsApi_QueryMktDataSnapshot.argtypes = [
            POINTER(MdsApiSessionInfoT),
            c_uint8,
            c_uint8,
            c_int32,
            POINTER(MdsMktDataSnapshotT)
        ]

        self._MdsApi_WaitOnUdpChannelGroup = self.api.MdsApi_WaitOnUdpChannelGroup
        self._MdsApi_WaitOnUdpChannelGroup.restype = c_int32
        self._MdsApi_WaitOnUdpChannelGroup.argtypes = [
            POINTER(MdsApiChannelGroupT),
            c_int32,
            F_MDSAPI_ONMSG_T,
            c_void_p,
            POINTER(POINTER(MdsApiSessionInfoT)),
        ]

        self._MdsApi_GetChannelGroupLastRecvTime = self.api.MdsApi_GetChannelGroupLastRecvTime
        self._MdsApi_GetChannelGroupLastRecvTime.restype = c_int64
        self._MdsApi_GetChannelGroupLastRecvTime.argtypes = [
            POINTER(MdsApiChannelGroupT),
        ]

    def MdsApi_CheckApiVersion(self):
        return self.MdsApi_GetApiVersion() == MDS_APPL_VER_ID

    def MdsApi_GetErrorMsg(self, err_code):
        return self._MdsApi_GetErrorMsg(c_int32(err_code)).decode()

    def MdsApi_GetApiVersion(self):
        return self._MdsApi_GetApiVersion().decode()

    def MdsApi_InitAll(self, cfg_file):
        return self._MdsApi_InitAll(
            byref(self.client_env),
            None if cfg_file is None else create_string_buffer(cfg_file.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_SECTION_LOGGER.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_SECTION.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_KEY_TCP_ADDR.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_KEY_QRY_ADDR.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_KEY_UDP_ADDR_SNAP1.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_KEY_UDP_ADDR_SNAP2.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_KEY_UDP_ADDR_TICK1.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_KEY_UDP_ADDR_TICK2.encode()),
        )

    def MdsApi_InitTcpChannel(self, cfg_file):
        return self._MdsApi_InitTcpChannel(
            byref(self.tcp_channel),
            None if cfg_file is None else create_string_buffer(cfg_file.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_SECTION.encode()),
            create_string_buffer(MDSAPI_CFG_DEFAULT_KEY_TCP_ADDR.encode()),
        )

    def MdsApi_DestoryAll(self):
        self._MdsApi_DestoryAll(byref(self.client_env))

    def MdsApi_WaitOnMsg(self, timeout_ms, on_msg_callback, callback_params):
        return self._MdsApi_WaitOnMsg(
            byref(self.tcp_channel),
            c_int32(timeout_ms),
            F_MDSAPI_ONMSG_T(on_msg_callback),
            None if callback_params is None else byref(callback_params)
        )

    def MdsApi_GetLastRecvTime(self):
        return self._MdsApi_GetLastRecvTime(byref(self.tcp_channel))

    def MdsApi_SetThreadSubscribeTickType(self, tick_type):
        return self._MdsApi_SetThreadSubscribeTickType(c_int32(tick_type))

    def MdsApi_SetThreadSubscribeTickRebuildFlag(self, tick_rebuild_flag):
        return self._MdsApi_SetThreadSubscribeTickRebuildFlag(c_int32(tick_rebuild_flag))

    def MdsApi_SetThreadSubscribeRequireInitMd(self, is_require_initial_mkt_data):
        return self._MdsApi_SetThreadSubscribeRequireInitMd(BOOL(is_require_initial_mkt_data))

    def MdsApi_SubscribeByString(self, security_list_str, delim, exchange_id, md_product_type, sub_mode, data_types):
        return self._MdsApi_SubscribeByString(
            byref(self.tcp_channel),
            None if security_list_str is None else create_string_buffer(security_list_str),
            None if delim is None else create_string_buffer(delim),
            c_uint8(exchange_id),
            c_uint8(md_product_type),
            c_uint8(sub_mode),
            c_int32(data_types),
        )

    def MdsApi_SubscribeByStringAndPrefixes(self, security_list_str, delim, sse_code_prefixes, szse_code_prefixes, md_product_type, sub_mode, data_types):
        return self._MdsApi_SubscribeByStringAndPrefixes(
            byref(self.tcp_channel),
            None if security_list_str is None else create_string_buffer(security_list_str),
            None if delim is None else create_string_buffer(delim),
            None if sse_code_prefixes is None else create_string_buffer(sse_code_prefixes),
            None if szse_code_prefixes is None else create_string_buffer(szse_code_prefixes),
            c_uint8(md_product_type),
            c_uint8(sub_mode),
            c_int32(data_types),
        )

    def MdsApi_QueryStockStaticInfoList(self, security_list_str, delim, qry_filter, qry_msg_callback, callback_params):
        return self._MdsApi_QueryStockStaticInfoList(
            byref(self.qry_channel),
            None if security_list_str is None else create_string_buffer(security_list_str),
            None if delim is None else create_string_buffer(delim),
            None if qry_filter is None else byref(qry_filter),
            F_MDSAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params)
        )

    def MdsApi_QueryOptionStaticInfoList(self, security_list_str, delim, qry_filter, qry_msg_callback, callback_params):
        return self._MdsApi_QueryOptionStaticInfoList(
            byref(self.qry_channel),
            None if security_list_str is None else create_string_buffer(security_list_str),
            None if delim is None else create_string_buffer(delim),
            None if qry_filter is None else byref(qry_filter),
            F_MDSAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params)
        )

    def MdsApi_QuerySnapshotList(self, security_list_str, delim, qry_filter, qry_msg_callback, callback_params):
        return self._MdsApi_QuerySnapshotList(
            byref(self.qry_channel),
            None if security_list_str is None else create_string_buffer(security_list_str),
            None if delim is None else create_string_buffer(delim),
            None if qry_filter is None else byref(qry_filter),
            F_MDSAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params)
        )

    def MdsApi_QueryMktDataSnapshot(self, exchange_id, md_product_type, instr_id, rsp_buf):
        return self._MdsApi_QueryMktDataSnapshot(
            byref(self.qry_channel),
            c_uint8(exchange_id),
            c_uint8(md_product_type),
            c_int32(instr_id),
            byref(rsp_buf),
        )

    def MdsApi_WaitOnUdpChannelGroup(self, timeout_ms, on_msg_callback, callback_params, failed):
        return self._MdsApi_WaitOnUdpChannelGroup(
            byref(self.udp_channel_group),
            c_int32(timeout_ms),
            F_MDSAPI_ONMSG_T(on_msg_callback),
            None if callback_params is None else byref(callback_params),
            None if failed is None else byref(POINTER(failed)()),
        )

    def MdsApi_GetChannelGroupLastRecvTime(self):
        return self._MdsApi_GetChannelGroupLastRecvTime(byref(self.udp_channel_group))
