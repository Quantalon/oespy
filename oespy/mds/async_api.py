from ctypes import byref, create_string_buffer

from ..spk.types import BOOL
from ..spk.general_endpoint_define import (SPK_ENDPOINT_MAX_REMOTE_CNT, SEndpointChannelCfgT, SEndpointIoThreadCfgT,
                                           SEndpointContextT, SEndpointChannelT)
from ..utils import BaseStructure
from ..utils.types import *
from .api import (F_MDSAPI_ONMSG_T, MdsApiRemoteCfgT, MdsApiSubscribeInfoT, MdsApi, MdsQryStockStaticInfoListFilterT,
                  F_MDSAPI_ON_QRY_MSG_T, MdsQrySnapshotListFilterT)


MDSAPI_ASYNC_MAX_REMOTE_CNT = SPK_ENDPOINT_MAX_REMOTE_CNT

MDSAPI_CFG_DEFAULT_SECTION_ASYNC_API = "async_api"
MDSAPI_CFG_DEFAULT_SECTION_CPUSET = "cpuset"

MDSAPI_CFG_DEFAULT_KEY_CPUSET_COMMUNICATION = "mdsapi_communication"
MDSAPI_CFG_DEFAULT_KEY_CPUSET_CALLBACK = "mdsapi_callback"
MDSAPI_CFG_DEFAULT_KEY_CPUSET_CONNECT = "mdsapi_connect"
MDSAPI_CFG_DEFAULT_KEY_CPUSET_IO_THREAD = "mdsapi_io_thread"


MdsAsyncApiChannelCfgT = SEndpointChannelCfgT
MdsAsyncApiIoThreadCfgT = SEndpointIoThreadCfgT
MdsAsyncApiContextT = SEndpointContextT
MdsAsyncApiChannelT = SEndpointChannelT


class MdsAsyncApiContextParamsT(BaseStructure):
    _fields_ = [
        ('asyncQueueSize', c_int32),

        ('isHugepageAble', c_uint8),
        ('isAsyncCallbackAble', c_uint8),
        ('isAsyncConnectAble', c_uint8),
        ('isBusyPollAble', c_uint8),
        ('isPreconnectAble', c_uint8),

        ('isCompressible', c_uint8),
        ('isUdpFilterable', c_uint8),
        ('isBuiltinQueryable', c_uint8),

        ('autoTimeSyncInterval', c_int16),
        ('__filler2', c_uint8 * 6),
        ('clockDriftBeginTime', c_int32),
    ]


F_MDSAPI_ASYNC_ON_MSG_T = F_MDSAPI_ONMSG_T

F_MDSAPI_ASYNC_ON_CONNECT_T = CFUNCTYPE(
    c_int32,
    POINTER(MdsAsyncApiChannelT),
    c_void_p
)

F_MDSAPI_ASYNC_ON_DISCONNECT_T = CFUNCTYPE(
    c_int32,
    POINTER(MdsAsyncApiChannelT),
    c_void_p
)

F_MDSAPI_ASYNC_ON_THREAD_START_T = CFUNCTYPE(
    c_int32,
    POINTER(MdsAsyncApiContextT),
    c_void_p
)


class MdsAsyncApi(MdsApi):
    def __init__(self):
        super().__init__()

        self.async_context = MdsAsyncApiContextT()
        self.async_channel = MdsAsyncApiChannelT()

        self._MdsAsyncApi_GetApiVersion = self.api.MdsAsyncApi_GetApiVersion
        self._MdsAsyncApi_GetApiVersion.restype = c_char_p

        self._MdsAsyncApi_CreateContext = self.api.MdsAsyncApi_CreateContext
        self._MdsAsyncApi_CreateContext.restype = POINTER(MdsAsyncApiContextT)
        self._MdsAsyncApi_CreateContext.argtypes = [
            c_char_p,
        ]

        self._MdsAsyncApi_ReleaseContext = self.api.MdsAsyncApi_ReleaseContext
        self._MdsAsyncApi_ReleaseContext.argtypes = [
            POINTER(MdsAsyncApiContextT),
        ]

        self._MdsAsyncApi_AddChannelFromFile = self.api.MdsAsyncApi_AddChannelFromFile
        self._MdsAsyncApi_AddChannelFromFile.restype = POINTER(MdsAsyncApiChannelT)
        self._MdsAsyncApi_AddChannelFromFile.argtypes = [
            POINTER(MdsAsyncApiContextT),
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            F_MDSAPI_ASYNC_ON_MSG_T,
            c_void_p,
            F_MDSAPI_ASYNC_ON_CONNECT_T,
            c_void_p,
            F_MDSAPI_ASYNC_ON_DISCONNECT_T,
            c_void_p,
        ]

        self._MdsAsyncApi_AddChannel = self.api.MdsAsyncApi_AddChannel
        self._MdsAsyncApi_AddChannel.restype = POINTER(MdsAsyncApiChannelT)
        self._MdsAsyncApi_AddChannel.argtypes = [
            POINTER(MdsAsyncApiContextT),
            c_char_p,
            POINTER(MdsApiRemoteCfgT),
            POINTER(MdsApiSubscribeInfoT),
            F_MDSAPI_ASYNC_ON_MSG_T,
            c_void_p,
            F_MDSAPI_ASYNC_ON_CONNECT_T,
            c_void_p,
            F_MDSAPI_ASYNC_ON_DISCONNECT_T,
            c_void_p,
        ]

        self._MdsAsyncApi_Start = self.api.MdsAsyncApi_Start
        self._MdsAsyncApi_Start.restype = BOOL
        self._MdsAsyncApi_Start.argtypes = [
            POINTER(MdsAsyncApiContextT),
        ]

        self._MdsAsyncApi_IsRunning = self.api.MdsAsyncApi_IsRunning
        self._MdsAsyncApi_IsRunning.restype = BOOL
        self._MdsAsyncApi_IsRunning.argtypes = [
            POINTER(MdsAsyncApiContextT),
        ]

        self._MdsAsyncApi_GetTotalPicked = self.api.MdsAsyncApi_GetTotalPicked
        self._MdsAsyncApi_GetTotalPicked.restype = c_int64
        self._MdsAsyncApi_GetTotalPicked.argtypes = [
            POINTER(MdsAsyncApiContextT),
        ]

        self._MdsAsyncApi_Stop = self.api.MdsAsyncApi_Stop
        self._MdsAsyncApi_Stop.argtypes = [
            POINTER(MdsAsyncApiContextT),
        ]

        self._MdsAsyncApi_IsAllTerminated = self.api.MdsAsyncApi_IsAllTerminated
        self._MdsAsyncApi_IsAllTerminated.restype = BOOL
        self._MdsAsyncApi_IsAllTerminated.argtypes = [
            POINTER(MdsAsyncApiContextT),
        ]

        self._MdsAsyncApi_DefaultOnConnect = self.api.MdsAsyncApi_DefaultOnConnect
        self._MdsAsyncApi_DefaultOnConnect.restype = c_int32
        self._MdsAsyncApi_DefaultOnConnect.argtypes = [
            POINTER(MdsAsyncApiChannelT),
            c_void_p,
        ]

        self._MdsAsyncApi_SubscribeByString = self.api.MdsAsyncApi_SubscribeByString
        self._MdsAsyncApi_SubscribeByString.restype = BOOL
        self._MdsAsyncApi_SubscribeByString.argtypes = [
            POINTER(MdsAsyncApiChannelT),
            c_char_p,
            c_char_p,
            c_uint8,
            c_uint8,
            c_uint8,
            c_int32,
        ]

        self._MdsAsyncApi_SetBuiltinQueryable = self.api.MdsAsyncApi_SetBuiltinQueryable
        self._MdsAsyncApi_SetBuiltinQueryable.restype = BOOL
        self._MdsAsyncApi_SetBuiltinQueryable.argtypes = [
            POINTER(MdsAsyncApiContextT),
            BOOL
        ]

        self._MdsAsyncApi_QueryStockStaticInfoList = self.api.MdsAsyncApi_QueryStockStaticInfoList
        self._MdsAsyncApi_QueryStockStaticInfoList.restype = c_int32
        self._MdsAsyncApi_QueryStockStaticInfoList.argtypes = [
            POINTER(MdsAsyncApiContextT),
            c_char_p,
            c_char_p,
            POINTER(MdsQryStockStaticInfoListFilterT),
            F_MDSAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._MdsAsyncApi_QuerySnapshotList = self.api.MdsAsyncApi_QuerySnapshotList
        self._MdsAsyncApi_QuerySnapshotList.restype = c_int32
        self._MdsAsyncApi_QuerySnapshotList.argtypes = [
            POINTER(MdsAsyncApiContextT),
            c_char_p,
            c_char_p,
            POINTER(MdsQrySnapshotListFilterT),
            F_MDSAPI_ON_QRY_MSG_T,
            c_void_p,
        ]


    def MdsAsyncApi_GetApiVersion(self):
        return self._MdsAsyncApi_GetApiVersion().decode()

    def MdsAsyncApi_CreateContext(self, cfg_file):
        self.async_context = self._MdsAsyncApi_CreateContext(
            None if cfg_file is None else create_string_buffer(cfg_file.encode()),
        )

    def MdsAsyncApi_ReleaseContext(self, async_context):
        self._MdsAsyncApi_ReleaseContext(
            byref(self.async_context)
        )

    def MdsAsyncApi_AddChannelFromFile(self, async_context, channel_tag, cfg_file, cfg_section, addr_key,
                                       on_msg, on_msg_params,
                                       on_connect, on_connect_params,
                                       on_disconnect, on_disconnect_params):
        return self._MdsAsyncApi_AddChannelFromFile(
            byref(async_context),
            None if channel_tag is None else create_string_buffer(channel_tag),
            None if cfg_file is None else create_string_buffer(cfg_file),
            None if cfg_section is None else create_string_buffer(cfg_section),
            None if addr_key is None else create_string_buffer(addr_key),
            F_MDSAPI_ASYNC_ON_MSG_T(on_msg),
            None if on_msg_params is None else byref(on_msg_params),
            F_MDSAPI_ASYNC_ON_CONNECT_T(on_connect),
            None if on_connect_params is None else byref(on_connect_params),
            F_MDSAPI_ASYNC_ON_DISCONNECT_T(on_disconnect),
            None if on_disconnect_params is None else byref(on_disconnect_params),
        )

    def MdsAsyncApi_AddChannel(self, async_context, channel_tag, remote_cfg, subscribe_cfg,
                               on_msg, on_msg_params,
                               on_connect, on_connect_params,
                               on_disconnect, on_disconnect_params):
        return self._MdsAsyncApi_AddChannel(
            byref(async_context),
            None if channel_tag is None else create_string_buffer(channel_tag),
            byref(remote_cfg),
            None if subscribe_cfg is None else byref(subscribe_cfg),
            F_MDSAPI_ASYNC_ON_MSG_T(on_msg),
            None if on_msg_params is None else byref(on_msg_params),
            F_MDSAPI_ASYNC_ON_CONNECT_T(on_connect),
            None if on_connect_params is None else byref(on_connect_params),
            F_MDSAPI_ASYNC_ON_DISCONNECT_T(on_disconnect),
            None if on_disconnect_params is None else byref(on_disconnect_params),
        )

    def MdsAsyncApi_Start(self, async_context):
        return self._MdsAsyncApi_Start(
            byref(async_context),
        )

    def MdsAsyncApi_IsRunning(self, async_context):
        return self._MdsAsyncApi_IsRunning(
            byref(async_context),
        )

    def MdsAsyncApi_GetTotalPicked(self, async_context):
        return self._MdsAsyncApi_GetTotalPicked(
            byref(async_context),
        )

    def MdsAsyncApi_Stop(self, async_context):
        self._MdsAsyncApi_Stop(
            byref(async_context),
        )

    def MdsAsyncApi_IsAllTerminated(self, async_context):
        return self._MdsAsyncApi_IsAllTerminated(
            byref(async_context),
        )

    def MdsAsyncApi_DefaultOnConnect(self, async_channel):
        return self._MdsAsyncApi_DefaultOnConnect(
            byref(async_channel),
            None,
        )

    def MdsAsyncApi_SubscribeByString(self, async_channel, security_list_str, delim, exchange_id, md_product_type, sub_mode, data_types):
        return self._MdsAsyncApi_SubscribeByString(
            byref(async_channel),
            None if security_list_str is None else create_string_buffer(security_list_str),
            None if delim is None else create_string_buffer(delim),
            c_uint8(exchange_id),
            c_uint8(md_product_type),
            c_uint8(sub_mode),
            c_int32(data_types),
        )

    def MdsAsyncApi_SetBuiltinQueryable(self, async_context, is_builtin_queryable):
        return self._MdsAsyncApi_SetBuiltinQueryable(
            byref(async_context),
            BOOL(is_builtin_queryable),
        )

    def MdsAsyncApi_QueryStockStaticInfoList(self, async_context, security_list_str, delim, qry_filter, qry_msg_callback, callback_params):
        return self._MdsAsyncApi_QueryStockStaticInfoList(
            byref(async_context),
            None if security_list_str is None else create_string_buffer(security_list_str),
            None if delim is None else create_string_buffer(delim),
            byref(qry_filter),
            F_MDSAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def MdsAsyncApi_QuerySnapshotList(self, async_context, security_list_str, delim, qry_filter, qry_msg_callback, callback_params):
        return self._MdsAsyncApi_QuerySnapshotList(
            byref(async_context),
            None if security_list_str is None else create_string_buffer(security_list_str),
            None if delim is None else create_string_buffer(delim),
            byref(qry_filter),
            F_MDSAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

