from ctypes import byref, create_string_buffer
from ..spk.types import BOOL
from ..spk.general_endpoint_define import (SPK_ENDPOINT_MAX_REMOTE_CNT, SEndpointChannelCfgT, SEndpointIoThreadCfgT,
                                           SEndpointContextT, SEndpointChannelT)
from ..utils import BaseStructure
from ..utils.types import *
from .base_model import *
from .api import OesApi, F_OESAPI_ON_RPT_MSG_T, F_OESAPI_ON_QRY_MSG_T, OesApiSubscribeInfoT
from .qry_packets import *
from .qry_packets_credit import *
from .qry_packets_option import *


OESAPI_ASYNC_MAX_REMOTE_CNT = SPK_ENDPOINT_MAX_REMOTE_CNT
OESAPI_CFG_DEFAULT_SECTION_ASYNC_API = "async_api"
OESAPI_CFG_DEFAULT_SECTION_CPUSET = "cpuset"
OESAPI_CFG_DEFAULT_KEY_CPUSET_COMMUNICATION = "oesapi_report"
OESAPI_CFG_DEFAULT_KEY_CPUSET_CALLBACK = "oesapi_callback"
OESAPI_CFG_DEFAULT_KEY_CPUSET_CONNECT = "oesapi_connect"
OESAPI_CFG_DEFAULT_KEY_CPUSET_IO_THREAD = "oesapi_io_thread"


OesAsyncApiChannelCfgT = SEndpointChannelCfgT
OesAsyncApiIoThreadCfgT = SEndpointIoThreadCfgT
OesAsyncApiContextT = SEndpointContextT
OesAsyncApiChannelT = SEndpointChannelT


class OesAsyncApiContextParamsT(BaseStructure):
    _fields_ = [
        ('asyncQueueSize', c_int32),
        ('isHugepageAble', c_uint8),
        ('isAsyncCallbackAble', c_uint8),
        ('isAsyncConnectAble', c_uint8),
        ('isBusyPollAble', c_uint8),
        ('isPreconnectAble', c_uint8),
        ('isBuiltinQueryable', c_uint8),
        ('__filler', c_uint8 * 6),
    ]


F_OESAPI_ASYNC_ON_MSG_T = F_OESAPI_ON_RPT_MSG_T

F_OESAPI_ASYNC_ON_CONNECT_T = CFUNCTYPE(
    c_int32,
    POINTER(OesAsyncApiChannelT),
    c_void_p
)

F_OESAPI_ASYNC_ON_DISCONNECT_T = CFUNCTYPE(
    c_int32,
    POINTER(OesAsyncApiChannelT),
    c_void_p
)

F_OESAPI_ASYNC_ON_THREAD_START_T = CFUNCTYPE(
    c_int32,
    POINTER(OesAsyncApiContextT),
    c_void_p
)


class OesAsyncApi(OesApi):
    def __init__(self):
        super().__init__()

        self.async_context = OesAsyncApiContextT()
        self.async_channel = OesAsyncApiChannelT()

        self._OesAsyncApi_DefaultOnConnect = self.api.OesAsyncApi_DefaultOnConnect
        self._OesAsyncApi_DefaultOnConnect.restype = c_int32
        self._OesAsyncApi_DefaultOnConnect.argtypes = [
            POINTER(OesAsyncApiChannelT),
            c_void_p,
        ]

        self._OesAsyncApi_GetClientOverview = self.api.OesAsyncApi_GetClientOverview
        self._OesAsyncApi_GetClientOverview.restype = c_int32
        self._OesAsyncApi_GetClientOverview.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesClientOverviewT),
        ]

        self._OesAsyncApi_QuerySingleCashAsset = self.api.OesAsyncApi_QuerySingleCashAsset
        self._OesAsyncApi_QuerySingleCashAsset.restype = c_int32
        self._OesAsyncApi_QuerySingleCashAsset.argtypes = [
            POINTER(OesAsyncApiChannelT),
            c_char_p,
            POINTER(OesCashAssetItemT),
        ]

        self._OesAsyncApi_QueryStock = self.api.OesAsyncApi_QueryStock
        self._OesAsyncApi_QueryStock.restype = c_int32
        self._OesAsyncApi_QueryStock.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryStockFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesAsyncApi_QueryStkHolding = self.api.OesAsyncApi_QueryStkHolding
        self._OesAsyncApi_QueryStkHolding.restype = c_int32
        self._OesAsyncApi_QueryStkHolding.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryStkHoldingFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCrdDebtContract = self.api.OesAsyncApi_QueryCrdDebtContract
        self._OesAsyncApi_QueryCrdDebtContract.restype = c_int32
        self._OesAsyncApi_QueryCrdDebtContract.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCrdDebtContractFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCrdSecurityDebtStats = self.api.OesAsyncApi_QueryCrdSecurityDebtStats
        self._OesAsyncApi_QueryCrdSecurityDebtStats.restype = c_int32
        self._OesAsyncApi_QueryCrdSecurityDebtStats.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCrdSecurityDebtStatsFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCrdCreditAsset = self.api.OesAsyncApi_QueryCrdCreditAsset
        self._OesAsyncApi_QueryCrdCreditAsset.restype = c_int32
        self._OesAsyncApi_QueryCrdCreditAsset.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCrdCreditAssetFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCrdCashPosition = self.api.OesAsyncApi_QueryCrdCashPosition
        self._OesAsyncApi_QueryCrdCashPosition.restype = c_int32
        self._OesAsyncApi_QueryCrdCashPosition.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCrdCashPositionFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCrdSecurityPosition = self.api.OesAsyncApi_QueryCrdSecurityPosition
        self._OesAsyncApi_QueryCrdSecurityPosition.restype = c_int32
        self._OesAsyncApi_QueryCrdSecurityPosition.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCrdSecurityPositionFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCustInfo = self.api.OesAsyncApi_QueryCustInfo
        self._OesAsyncApi_QueryCustInfo.restype = c_int32
        self._OesAsyncApi_QueryCustInfo.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCustFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryInvAcct = self.api.OesAsyncApi_QueryInvAcct
        self._OesAsyncApi_QueryInvAcct.restype = c_int32
        self._OesAsyncApi_QueryInvAcct.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryInvAcctFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCashAsset = self.api.OesAsyncApi_QueryCashAsset
        self._OesAsyncApi_QueryCashAsset.restype = c_int32
        self._OesAsyncApi_QueryCashAsset.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCashAssetFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCrdExcessStock = self.api.OesAsyncApi_QueryCrdExcessStock
        self._OesAsyncApi_QueryCrdExcessStock.restype = c_int32
        self._OesAsyncApi_QueryCrdExcessStock.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCrdExcessStockFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCrdInterestRate = self.api.OesAsyncApi_QueryCrdInterestRate
        self._OesAsyncApi_QueryCrdInterestRate.restype = c_int32
        self._OesAsyncApi_QueryCrdInterestRate.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCrdInterestRateFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCrdDebtJournal = self.api.OesAsyncApi_QueryCrdDebtJournal
        self._OesAsyncApi_QueryCrdDebtJournal.restype = c_int32
        self._OesAsyncApi_QueryCrdDebtJournal.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCrdDebtJournalFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QuerySingleOrder = self.api.OesAsyncApi_QuerySingleOrder
        self._OesAsyncApi_QuerySingleOrder.restype = c_int32
        self._OesAsyncApi_QuerySingleOrder.argtypes = [
            POINTER(OesAsyncApiChannelT),
            c_int32,
            POINTER(OesOrdItemT),
        ]

        self._OesAsyncApi_QueryOrder = self.api.OesAsyncApi_QueryOrder
        self._OesAsyncApi_QueryOrder.restype = c_int32
        self._OesAsyncApi_QueryOrder.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryOrdFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryTrade = self.api.OesAsyncApi_QueryTrade
        self._OesAsyncApi_QueryTrade.restype = c_int32
        self._OesAsyncApi_QueryTrade.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryTrdFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryCrdCashRepayOrder = self.api.OesAsyncApi_QueryCrdCashRepayOrder
        self._OesAsyncApi_QueryCrdCashRepayOrder.restype = c_int32
        self._OesAsyncApi_QueryCrdCashRepayOrder.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCrdCashRepayFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_QueryBrokerParamsInfo = self.api.OesAsyncApi_QueryBrokerParamsInfo
        self._OesAsyncApi_QueryBrokerParamsInfo.restype = c_int32
        self._OesAsyncApi_QueryBrokerParamsInfo.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesBrokerParamsInfoT),
        ]

        self._OesAsyncApi_QueryCommissionRate = self.api.OesAsyncApi_QueryCommissionRate
        self._OesAsyncApi_QueryCommissionRate.restype = c_int32
        self._OesAsyncApi_QueryCommissionRate.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesQryCommissionRateFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p
        ]

        self._OesAsyncApi_GetCrdDrawableBalance = self.api.OesAsyncApi_GetCrdDrawableBalance
        self._OesAsyncApi_GetCrdDrawableBalance.restype = c_int64
        self._OesAsyncApi_GetCrdDrawableBalance.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesCrdDrawableBalanceItemT),
        ]

        self._OesAsyncApi_GetCrdCollateralTransferOutMaxQty = self.api.OesAsyncApi_GetCrdCollateralTransferOutMaxQty
        self._OesAsyncApi_GetCrdCollateralTransferOutMaxQty.restype = c_int64
        self._OesAsyncApi_GetCrdCollateralTransferOutMaxQty.argtypes = [
            POINTER(OesAsyncApiChannelT),
            c_char_p,
            c_uint8,
            POINTER(OesCrdCollateralTransferOutMaxQtyItemT),
        ]

        self._OesAsyncApi_CreateContext = self.api.OesAsyncApi_CreateContext
        self._OesAsyncApi_CreateContext.restype = POINTER(OesAsyncApiContextT),
        self._OesAsyncApi_CreateContext.argtypes = [
            c_char_p,
        ]

        self._OesAsyncApi_AddChannelFromFile = self.api.OesAsyncApi_AddChannelFromFile
        self._OesAsyncApi_AddChannelFromFile.restype = POINTER(OesAsyncApiChannelT)
        self._OesAsyncApi_AddChannelFromFile.argtypes = [
            POINTER(OesAsyncApiContextT),
            c_uint32,
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            F_OESAPI_ASYNC_ON_MSG_T,
            c_void_p,
            F_OESAPI_ASYNC_ON_CONNECT_T,
            c_void_p,
            F_OESAPI_ASYNC_ON_DISCONNECT_T,
            c_void_p,
        ]

        self._OesAsyncApi_GetChannelSubscribeCfg = self.api.OesAsyncApi_GetChannelSubscribeCfg
        self._OesAsyncApi_GetChannelSubscribeCfg.restype = POINTER(OesApiSubscribeInfoT)
        self._OesAsyncApi_GetChannelSubscribeCfg.argtypes = [
            POINTER(OesAsyncApiChannelT),
        ]

        self._OesAsyncApi_Start = self.api.OesAsyncApi_Start
        self._OesAsyncApi_Start.restype = BOOL
        self._OesAsyncApi_Start.argtypes = [
            POINTER(OesAsyncApiContextT)
        ]

        self._OesAsyncApi_GetChannel = self.api.OesAsyncApi_GetChannel
        self._OesAsyncApi_GetChannel.restype = POINTER(OesAsyncApiChannelT)
        self._OesAsyncApi_GetChannel.argtypes = [
            POINTER(OesAsyncApiContextT),
            c_int32,
            c_int32,
        ]

        self._OesAsyncApi_IsRunning = self.api.OesAsyncApi_IsRunning
        self._OesAsyncApi_IsRunning.restype = BOOL
        self._OesAsyncApi_IsRunning.argtypes = [
            POINTER(OesAsyncApiContextT),
        ]

        self._OesAsyncApi_Stop = self.api.OesAsyncApi_Stop
        self._OesAsyncApi_Stop.argtypes = [
            POINTER(OesAsyncApiContextT),
        ]

        self._OesAsyncApi_ReleaseContext = self.api.OesAsyncApi_ReleaseContext
        self._OesAsyncApi_ReleaseContext.argtypes = [
            POINTER(OesAsyncApiContextT),
        ]

        self._OesAsyncApi_SendOrderReq = self.api.OesAsyncApi_SendOrderReq
        self._OesAsyncApi_SendOrderReq.restype = c_int32
        self._OesAsyncApi_SendOrderReq.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesOrdReqT)
        ]

        self._OesAsyncApi_SendOrderCancelReq = self.api.OesAsyncApi_SendOrderCancelReq
        self._OesAsyncApi_SendOrderCancelReq.restype = c_int32
        self._OesAsyncApi_SendOrderCancelReq.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesOrdCancelReqT)
        ]

        self._OesAsyncApi_SendCreditCashRepayReq = self.api.OesAsyncApi_SendCreditCashRepayReq
        self._OesAsyncApi_SendCreditCashRepayReq.restype = c_int32
        self._OesAsyncApi_SendCreditCashRepayReq.argtypes = [
            POINTER(OesAsyncApiChannelT),
            c_int32,
            c_int64,
            c_uint32,
            c_char_p,
            c_void_p,
        ]

        self._OesAsyncApi_SendCreditRepayReq = self.api.OesAsyncApi_SendCreditRepayReq
        self._OesAsyncApi_SendCreditRepayReq.restype = c_int32
        self._OesAsyncApi_SendCreditRepayReq.argtypes = [
            POINTER(OesAsyncApiChannelT),
            POINTER(OesOrdReqT),
            c_uint32,
            c_char_p,
        ]


    def OesAsyncApi_DefaultOnConnect(self, callback_params):
        self._OesAsyncApi_DefaultOnConnect(
            byref(self.async_channel),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_GetClientOverview(self, out_client_overview):
        return self._OesAsyncApi_GetClientOverview(
            byref(self.async_channel),
            byref(out_client_overview),
        )

    def OesAsyncApi_QuerySingleCashAsset(self, cash_acct_id, out_cash_asset_item):
        return self._OesAsyncApi_QuerySingleCashAsset(
            byref(self.async_channel),
            None if cash_acct_id is None else create_string_buffer(cash_acct_id.encode()),
            byref(out_cash_asset_item),
        )

    def OesAsyncApi_QueryStock(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryStock(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryStkHolding(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryStkHolding(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCrdDebtContract(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCrdDebtContract(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCrdSecurityDebtStats(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCrdSecurityDebtStats(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCrdCreditAsset(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCrdCreditAsset(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCrdCashPosition(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCrdCashPosition(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCrdSecurityPosition(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCrdSecurityPosition(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCustInfo(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCustInfo(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryInvAcct(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryInvAcct(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCashAsset(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCashAsset(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCrdExcessStock(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCrdExcessStock(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCrdInterestRate(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCrdInterestRate(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCrdDebtJournal(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCrdDebtJournal(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QuerySingleOrder(self, cl_seq_no, out_ord_item):
        return self._OesAsyncApi_QuerySingleOrder(
            byref(self.async_channel),
            c_int32(cl_seq_no),
            byref(out_ord_item),
        )

    def OesAsyncApi_QueryOrder(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryOrder(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryTrade(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryTrade(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryCrdCashRepayOrder(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCrdCashRepayOrder(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_QueryBrokerParamsInfo(self, out_broker_params):
        return self._OesAsyncApi_QueryBrokerParamsInfo(
            byref(self.async_channel),
            byref(out_broker_params),
        )

    def OesAsyncApi_QueryCommissionRate(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesAsyncApi_QueryCommissionRate(
            byref(self.async_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesAsyncApi_GetCrdDrawableBalance(self, out_drawable_balance_item):
        return self._OesAsyncApi_GetCrdDrawableBalance(
            byref(self.async_channel),
            byref(out_drawable_balance_item),
        )

    def OesAsyncApi_GetCrdCollateralTransferOutMaxQty(self, security_id, mkt_id, out_transfer_out_qty_item):
        return self._OesAsyncApi_GetCrdCollateralTransferOutMaxQty(
            byref(self.async_channel),
            create_string_buffer(security_id.encode()),
            c_uint8(mkt_id),
            byref(out_transfer_out_qty_item),
        )

    def OesAsyncApi_CreateContext(self, cfg_file):
        self.async_context = self._OesAsyncApi_CreateContext(
            None if cfg_file is None else create_string_buffer(cfg_file.encode()),
        )

    def OesAsyncApi_AddChannelFromFile(self, channel_tag, cfg_file, cfg_section, addr_key,
                                       on_msg, on_msg_params,
                                       on_connect, on_connect_params,
                                       on_disconnect, on_disconnect_params):
        self.async_channel = self._OesAsyncApi_AddChannelFromFile(
            byref(self.async_context),
            None if channel_tag is None else create_string_buffer(channel_tag.encode()),
            None if cfg_file is None else create_string_buffer(cfg_file.encode()),
            None if cfg_section is None else create_string_buffer(cfg_section.encode()),
            None if addr_key is None else create_string_buffer(addr_key.encode()),
            F_OESAPI_ASYNC_ON_MSG_T(on_msg),
            None if on_msg_params is None else byref(on_msg_params),
            F_OESAPI_ASYNC_ON_CONNECT_T(on_connect),
            None if on_connect_params is None else byref(on_connect_params),
            F_OESAPI_ASYNC_ON_DISCONNECT_T(on_disconnect),
            None if on_disconnect_params is None else byref(on_disconnect_params),
        )

    def OesAsyncApi_GetChannelSubscribeCfg(self):
        return self._OesAsyncApi_GetChannelSubscribeCfg(
            byref(self.async_channel),
        )

    def OesAsyncApi_Start(self):
        return self._OesAsyncApi_Start(
            byref(self.async_context)
        )

    def OesAsyncApi_GetChannel(self, channel_type, channel_index):
        self.async_channel = self._OesAsyncApi_GetChannel(
            byref(self.async_context),
            c_int32(channel_type),
            c_int32(channel_index),
        )

    def OesAsyncApi_IsRunning(self):
        return self._OesAsyncApi_IsRunning(
            byref(self.async_context),
        )

    def OesAsyncApi_Stop(self):
        self._OesAsyncApi_Stop(
            byref(self.async_context),
        )

    def OesAsyncApi_ReleaseContext(self):
        self._OesAsyncApi_ReleaseContext(
            byref(self.async_context)
        )

    def OesAsyncApi_SendOrderReq(self, ord_req):
        return self._OesAsyncApi_SendOrderReq(
            byref(self.async_channel),
            byref(ord_req),
        )

    def OesAsyncApi_SendOrderCancelReq(self, cancel_req):
        return self._OesAsyncApi_SendOrderCancelReq(
            byref(self.async_channel),
            byref(cancel_req),
        )

    def OesAsyncApi_SendCreditCashRepayReq(self, cl_seq_no, repay_amt, repay_mode, debt_id, user_info):
        return self._OesAsyncApi_SendCreditCashRepayReq(
            byref(self.async_channel),
            c_int32(cl_seq_no),
            c_int64(repay_amt),
            c_uint32(repay_mode),
            None if debt_id is None else create_string_buffer(debt_id.encode()),
            None if user_info is None else byref(user_info),
        )

    def OesAsyncApi_SendCreditRepayReq(self, ord_req, repay_mode, debt_id):
        return self._OesAsyncApi_SendCreditRepayReq(
            byref(self.async_channel),
            byref(ord_req),
            c_uint32(repay_mode),
            None if debt_id is None else create_string_buffer(debt_id.encode()),
        )