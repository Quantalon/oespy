from ctypes import cdll, byref, create_string_buffer

from ..spk.types import BOOL
from ..spk.global_packet import SMsgHeadT
from ..spk.general_client_define import (SGeneralClientChannelT, SGeneralClientChannelGroupT, SGeneralClientAddrInfoT,
                                         SGeneralClientRemoteCfgT, SGeneralClientAddrCursorT)
from ..utils import LIB_PATH, BaseStructure
from ..utils.types import *
from .packets import *
from .base_model import *
from .base_model_option import *
from .base_model_credit import *
from .qry_packets import *
from .qry_packets_option import *
from .qry_packets_credit import *


OESAPI_CFG_DEFAULT_SECTION = "oes_client"
OESAPI_CFG_DEFAULT_SECTION_LOGGER = "log"
OESAPI_CFG_DEFAULT_KEY_ORD_ADDR = "ordServer"
OESAPI_CFG_DEFAULT_KEY_RPT_ADDR = "rptServer"
OESAPI_CFG_DEFAULT_KEY_QRY_ADDR = "qryServer"
OESAPI_DEFAULT_STRING_DELIM = ",;| \t\r\n"
OESAPI_DEFAULT_HEARTBEAT_INTERVAL = 30


class eOesApiChannelTypeT(Enum):
    OESAPI_CHANNEL_TYPE_ORDER = 1
    OESAPI_CHANNEL_TYPE_REPORT = 2
    OESAPI_CHANNEL_TYPE_QUERY = 3


OesApiSessionInfoT = SGeneralClientChannelT
OesApiChannelGroupT = SGeneralClientChannelGroupT
OesApiAddrInfoT = SGeneralClientAddrInfoT
OesApiRemoteCfgT = SGeneralClientRemoteCfgT
OesApiAddrCursorT = SGeneralClientAddrCursorT


class OesApiSubscribeInfoT(BaseStructure):
    _fields_ = [
        ('clEnvId', c_int8),
        ('__filler', c_uint8 * 3),
        ('rptTypes', c_int32),
    ]


class OesApiClientCfgT(BaseStructure):
    _fields_ = [
        ('ordChannelCfg', OesApiRemoteCfgT),
        ('rptChannelCfg', OesApiRemoteCfgT),
        ('qryChannelCfg', OesApiRemoteCfgT),
        ('subscribeInfo', OesApiSubscribeInfoT),
    ]


class OesApiClientEnvT(BaseStructure):
    _fields_ = [
        ('ordChannel', OesApiSessionInfoT),
        ('rptChannel', OesApiSessionInfoT),
        ('qryChannel', OesApiSessionInfoT),
    ]


F_OESAPI_ON_RPT_MSG_T = CFUNCTYPE(
    c_int32,
    POINTER(OesApiSessionInfoT),
    POINTER(SMsgHeadT),
    c_void_p,
    c_void_p
)


F_OESAPI_ON_QRY_MSG_T = CFUNCTYPE(
    c_int32,
    POINTER(OesApiSessionInfoT),
    POINTER(SMsgHeadT),
    c_void_p,
    POINTER(OesQryCursorT),
    c_void_p
)


class OesApi:
    def __init__(self):
        self.api = cdll.LoadLibrary(LIB_PATH)
        self.client_env = OesApiClientEnvT()

        self.ord_channel = self.client_env.ordChannel
        self.rpt_channel = self.client_env.rptChannel
        self.qry_channel = self.client_env.qryChannel

        self._OesApi_GetErrorMsg = self.api.OesApi_GetErrorMsg
        self._OesApi_GetErrorMsg.restype = c_char_p
        self._OesApi_GetErrorMsg.argtypes = [
            c_int32,
        ]

        self._OesApi_GetApiVersion = self.api.OesApi_GetApiVersion
        self._OesApi_GetApiVersion.restype = c_char_p

        self._OesApi_GetTradingDay = self.api.OesApi_GetTradingDay
        self._OesApi_GetTradingDay.restype = c_int32
        self._OesApi_GetTradingDay.argtypes = [
            POINTER(OesApiSessionInfoT),
        ]

        self._OesApi_SetThreadUsername = self.api.OesApi_SetThreadUsername
        self._OesApi_SetThreadUsername.argtypes = [
            c_char_p,
        ]

        self._OesApi_SetThreadPassword = self.api.OesApi_SetThreadPassword
        self._OesApi_SetThreadPassword.argtypes = [
            c_char_p,
        ]

        self._OesApi_SetCustomizedDriverId = self.api.OesApi_SetCustomizedDriverId
        self._OesApi_SetCustomizedDriverId.restype = BOOL
        self._OesApi_SetCustomizedDriverId.argtypes = [
            c_char_p,
        ]

        self._OesApi_SetDefaultEntrustWay = self.api.OesApi_SetDefaultEntrustWay
        self._OesApi_SetDefaultEntrustWay.restype = BOOL
        self._OesApi_SetDefaultEntrustWay.argtypes = [
            c_char,
        ]

        self._OesApi_SetThreadBusinessType = self.api.OesApi_SetThreadBusinessType
        self._OesApi_SetThreadBusinessType.argtypes = [
            c_int32,
        ]

        self._OesApi_InitAll = self.api.OesApi_InitAll
        self._OesApi_InitAll.restype = BOOL
        self._OesApi_InitAll.argtypes = [
            POINTER(OesApiClientEnvT),
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            c_int64,
            POINTER(c_int32)
        ]

        self._OesApi_LogoutAll = self.api.OesApi_LogoutAll
        self._OesApi_LogoutAll.argtypes = [
            POINTER(OesApiClientEnvT),
            BOOL
        ]

        self._OesApi_DestoryAll = self.api.OesApi_DestoryAll
        self._OesApi_DestoryAll.argtypes = [
            POINTER(OesApiClientEnvT)
        ]

        self._OesApi_SendOrderReq = self.api.OesApi_SendOrderReq
        self._OesApi_SendOrderReq.restype = c_int32
        self._OesApi_SendOrderReq.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesOrdReqT)
        ]

        self._OesApi_SendOrderCancelReq = self.api.OesApi_SendOrderCancelReq
        self._OesApi_SendOrderCancelReq.restype = c_int32
        self._OesApi_SendOrderCancelReq.argtypes = [
            POINTER(OesApiSessionInfoT),
                                                    POINTER(OesOrdCancelReqT)
        ]

        self._OesApi_GetClientOverview = self.api.OesApi_GetClientOverview
        self._OesApi_GetClientOverview.restype = c_int32
        self._OesApi_GetClientOverview.argtypes = [
            POINTER(OesApiSessionInfoT),
                                                   POINTER(OesClientOverviewT)
        ]

        self._OesApi_HasStockStatus = self.api.OesApi_HasStockStatus
        self._OesApi_HasStockStatus.restype = BOOL
        self._OesApi_HasStockStatus.argtypes = [
            POINTER(OesStockItemT),
                                                c_uint32
        ]

        self._OesApi_QueryStock = self.api.OesApi_QueryStock
        self._OesApi_QueryStock.restype = c_int32
        self._OesApi_QueryStock.argtypes = [
            POINTER(OesApiSessionInfoT),
                                            POINTER(OesQryStockFilterT),
                                            F_OESAPI_ON_QRY_MSG_T,
                                            c_void_p
        ]

        self._OesApi_QueryCashAsset = self.api.OesApi_QueryCashAsset
        self._OesApi_QueryCashAsset.restype = c_int32
        self._OesApi_QueryCashAsset.argtypes = [
            POINTER(OesApiSessionInfoT),
                                                POINTER(OesQryCashAssetFilterT),
                                                F_OESAPI_ON_QRY_MSG_T,
                                                c_void_p
        ]

        self._OesApi_QueryStkHolding = self.api.OesApi_QueryStkHolding
        self._OesApi_QueryStkHolding.restype = c_int32
        self._OesApi_QueryStkHolding.argtypes = [
            POINTER(OesApiSessionInfoT),
                                                 POINTER(OesQryStkHoldingFilterT),
                                                 F_OESAPI_ON_QRY_MSG_T,
                                                 c_void_p
        ]

        self._OesApi_QueryMarketState = self.api.OesApi_QueryMarketState
        self._OesApi_QueryMarketState.restype = c_int32
        self._OesApi_QueryMarketState.argtypes = [
            POINTER(OesApiSessionInfoT),
                                                  POINTER(OesQryMarketStateFilterT),
                                                  F_OESAPI_ON_QRY_MSG_T,
                                                  c_void_p
        ]

        self._OesApi_GetLastRecvTime = self.api.OesApi_GetLastRecvTime
        self._OesApi_GetLastRecvTime.restype = c_int64
        self._OesApi_GetLastRecvTime.argtypes = [POINTER(OesApiSessionInfoT)]

        self._OesApi_WaitReportMsg = self.api.OesApi_WaitReportMsg
        self._OesApi_WaitReportMsg.restype = c_int32
        self._OesApi_WaitReportMsg.argtypes = [
            POINTER(OesApiSessionInfoT),
                                               c_int32,
                                               F_OESAPI_ON_RPT_MSG_T,
                                               c_void_p
        ]

        self._OesApi_SendOptSettlementConfirmReq = self.api.OesApi_SendOptSettlementConfirmReq
        self._OesApi_SendOptSettlementConfirmReq.restype = c_int32
        self._OesApi_SendOptSettlementConfirmReq.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesOptSettlementConfirmReqT),
            POINTER(OesOptSettlementConfirmRspT),
        ]

        self._OesApi_QueryOption = self.api.OesApi_QueryOption
        self._OesApi_QueryOption.restype = c_int32
        self._OesApi_QueryOption.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryOptionFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryOptHolding = self.api.OesApi_QueryOptHolding
        self._OesApi_QueryOptHolding.restype = c_int32
        self._OesApi_QueryOptHolding.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryOptHoldingFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryOptUnderlyingHolding = self.api.OesApi_QueryOptUnderlyingHolding
        self._OesApi_QueryOptUnderlyingHolding.restype = c_int32
        self._OesApi_QueryOptUnderlyingHolding.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryOptUnderlyingHoldingFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryOptPositionLimit = self.api.OesApi_QueryOptPositionLimit
        self._OesApi_QueryOptPositionLimit.restype = c_int32
        self._OesApi_QueryOptPositionLimit.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryOptPositionLimitFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryOptPurchaseLimit = self.api.OesApi_QueryOptPurchaseLimit
        self._OesApi_QueryOptPurchaseLimit.restype = c_int32
        self._OesApi_QueryOptPurchaseLimit.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryOptPurchaseLimitFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryOptSettlementStatement = self.api.OesApi_QueryOptSettlementStatement
        self._OesApi_QueryOptSettlementStatement.restype = c_int32
        self._OesApi_QueryOptSettlementStatement.argtypes = [
            POINTER(OesApiSessionInfoT),
            c_char_p,
            c_char_p,
            c_int32,
        ]

        self._OesApi_QueryOptExerciseAssign = self.api.OesApi_QueryOptExerciseAssign
        self._OesApi_QueryOptExerciseAssign.restype = c_int32
        self._OesApi_QueryOptExerciseAssign.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryOptExerciseAssignFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryNotifyInfo = self.api.OesApi_QueryNotifyInfo
        self._OesApi_QueryNotifyInfo.restype = c_int32
        self._OesApi_QueryNotifyInfo.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryNotifyInfoFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_ParseAddrListString = self.api.OesApi_ParseAddrListString
        self._OesApi_ParseAddrListString.restype = c_int32
        self._OesApi_ParseAddrListString.argtypes = [
            c_char_p,
            POINTER(OesApiAddrInfoT),
            c_int32,
        ]

        self._OesApi_QueryBrokerParamsInfo = self.api.OesApi_QueryBrokerParamsInfo
        self._OesApi_QueryBrokerParamsInfo.restype = c_int32
        self._OesApi_QueryBrokerParamsInfo.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesBrokerParamsInfoT)
        ]

        self._OesApi_QueryCounterCash = self.api.OesApi_QueryCounterCash
        self._OesApi_QueryCounterCash.restype = c_int32
        self._OesApi_QueryCounterCash.argtypes = [
            POINTER(OesApiSessionInfoT),
            c_char_p,
            POINTER(OesCounterCashItemT),
        ]

        self._OesApi_QuerySingleCashAsset = self.api.OesApi_QuerySingleCashAsset
        self._OesApi_QuerySingleCashAsset.restype = c_int32
        self._OesApi_QuerySingleCashAsset.argtypes = [
            POINTER(OesApiSessionInfoT),
            c_char_p,
            POINTER(OesCashAssetItemT)
        ]

        self._OesApi_QuerySingleStkHolding = self.api.OesApi_QuerySingleStkHolding
        self._OesApi_QuerySingleStkHolding.restype = c_int32
        self._OesApi_QuerySingleStkHolding.argtypes = [
            POINTER(OesApiSessionInfoT),
            c_char_p,
            c_char_p,
            POINTER(OesStkHoldingItemT),
        ]

        self._OesApi_QuerySingleOrder = self.api.OesApi_QuerySingleOrder
        self._OesApi_QuerySingleOrder.restype = c_int32
        self._OesApi_QuerySingleOrder.argtypes = [
            POINTER(OesApiSessionInfoT),
            c_int32,
            POINTER(OesOrdItemT),
        ]

        self._OesApi_QueryCustInfo = self.api.OesApi_QueryCustInfo
        self._OesApi_QueryCustInfo.restype = c_int32
        self._OesApi_QueryCustInfo.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCustFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryInvAcct = self.api.OesApi_QueryInvAcct
        self._OesApi_QueryInvAcct.restype = c_int32
        self._OesApi_QueryInvAcct.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryInvAcctFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryIssue = self.api.OesApi_QueryIssue
        self._OesApi_QueryIssue.restype = c_int32
        self._OesApi_QueryIssue.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryIssueFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryLotWinning = self.api.OesApi_QueryLotWinning
        self._OesApi_QueryLotWinning.restype = c_int32
        self._OesApi_QueryLotWinning.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryLotWinningFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryCommissionRate = self.api.OesApi_QueryCommissionRate
        self._OesApi_QueryCommissionRate.restype = c_int32
        self._OesApi_QueryCommissionRate.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCommissionRateFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryEtf = self.api.OesApi_QueryEtf
        self._OesApi_QueryEtf.restype = c_int32
        self._OesApi_QueryEtf.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryEtfFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryEtfComponent = self.api.OesApi_QueryEtfComponent
        self._OesApi_QueryEtfComponent.restype = c_int32
        self._OesApi_QueryEtfComponent.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryEtfComponentFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryOrder = self.api.OesApi_QueryOrder
        self._OesApi_QueryOrder.restype = c_int32
        self._OesApi_QueryOrder.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryOrdFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryTrade = self.api.OesApi_QueryTrade
        self._OesApi_QueryTrade.restype = c_int32
        self._OesApi_QueryTrade.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryTrdFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryFundTransferSerial = self.api.OesApi_QueryFundTransferSerial
        self._OesApi_QueryFundTransferSerial.restype = c_int32
        self._OesApi_QueryFundTransferSerial.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryFundTransferSerialFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QuerySingleOptHolding = self.api.OesApi_QuerySingleOptHolding
        self._OesApi_QuerySingleOptHolding.restype = c_int32
        self._OesApi_QuerySingleOptHolding.argtypes = [
            POINTER(OesApiSessionInfoT),
            c_char_p,
            c_char_p,
            c_uint8,
            c_uint8,
            POINTER(OesOptHoldingItemT),
        ]

        self._OesApi_SendCreditCashRepayReq = self.api.OesApi_SendCreditCashRepayReq
        self._OesApi_SendCreditCashRepayReq.restype = c_int32
        self._OesApi_SendCreditCashRepayReq.argtypes = [
            POINTER(OesApiSessionInfoT),
            c_int32,
            c_int64,
            c_uint32,
            c_char_p,
            c_void_p,
        ]

        self._OesApi_SendCreditRepayReq = self.api.OesApi_SendCreditRepayReq
        self._OesApi_SendCreditRepayReq.restype = c_int32
        self._OesApi_SendCreditRepayReq.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesOrdReqT),
            c_uint32,
            c_char_p,
        ]

        self._OesApi_QueryCrdDebtContract = self.api.OesApi_QueryCrdDebtContract
        self._OesApi_QueryCrdDebtContract.restype = c_int32
        self._OesApi_QueryCrdDebtContract.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCrdDebtContractFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryCrdSecurityDebtStats = self.api.OesApi_QueryCrdSecurityDebtStats
        self._OesApi_QueryCrdSecurityDebtStats.restype = c_int32
        self._OesApi_QueryCrdSecurityDebtStats.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCrdSecurityDebtStatsFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryCrdCreditAsset = self.api.OesApi_QueryCrdCreditAsset
        self._OesApi_QueryCrdCreditAsset.restype = c_int32
        self._OesApi_QueryCrdCreditAsset.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCrdCreditAssetFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryCrdCashPosition = self.api.OesApi_QueryCrdCashPosition
        self._OesApi_QueryCrdCashPosition.restype = c_int32
        self._OesApi_QueryCrdCashPosition.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCrdCashPositionFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryCrdSecurityPosition = self.api.OesApi_QueryCrdSecurityPosition
        self._OesApi_QueryCrdSecurityPosition.restype = c_int32
        self._OesApi_QueryCrdSecurityPosition.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCrdSecurityPositionFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_GetCrdDrawableBalance = self.api.OesApi_GetCrdDrawableBalance
        self._OesApi_GetCrdDrawableBalance.restype = c_int64
        self._OesApi_GetCrdDrawableBalance.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesCrdDrawableBalanceItemT),
        ]

        self._OesApi_GetCrdCollateralTransferOutMaxQty = self.api.OesApi_GetCrdCollateralTransferOutMaxQty
        self._OesApi_GetCrdCollateralTransferOutMaxQty.restype = c_int64
        self._OesApi_GetCrdCollateralTransferOutMaxQty.argtypes = [
            POINTER(OesApiSessionInfoT),
            c_char_p,
            c_uint8,
            POINTER(OesCrdCollateralTransferOutMaxQtyItemT),
        ]

        self._OesApi_QueryCrdDebtJournal = self.api.OesApi_QueryCrdDebtJournal
        self._OesApi_QueryCrdDebtJournal.restype = c_int32
        self._OesApi_QueryCrdDebtJournal.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCrdDebtJournalFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryCrdExcessStock = self.api.OesApi_QueryCrdExcessStock
        self._OesApi_QueryCrdExcessStock.restype = c_int32
        self._OesApi_QueryCrdExcessStock.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCrdExcessStockFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryCrdCashRepayOrder = self.api.OesApi_QueryCrdCashRepayOrder
        self._OesApi_QueryCrdCashRepayOrder.restype = c_int32
        self._OesApi_QueryCrdCashRepayOrder.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCrdCashRepayFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

        self._OesApi_QueryCrdInterestRate = self.api.OesApi_QueryCrdInterestRate
        self._OesApi_QueryCrdInterestRate.restype = c_int32
        self._OesApi_QueryCrdInterestRate.argtypes = [
            POINTER(OesApiSessionInfoT),
            POINTER(OesQryCrdInterestRateFilterT),
            F_OESAPI_ON_QRY_MSG_T,
            c_void_p,
        ]

    def OesApi_CheckApiVersion(self):
        return self.OesApi_GetApiVersion() == OES_APPL_VER_ID

    def OesApi_GetErrorMsg(self, err_code):
        return self._OesApi_GetErrorMsg(c_int32(err_code)).decode()

    def OesApi_GetApiVersion(self):
        return self._OesApi_GetApiVersion().decode()

    def OesApi_GetTradingDay(self):
        return self._OesApi_GetTradingDay(
            byref(self.qry_channel),
        )

    def OesApi_SetThreadUsername(self, username):
        self._OesApi_SetThreadUsername(
            create_string_buffer(username.encode()),
        )

    def OesApi_SetThreadPassword(self, password):
        self._OesApi_SetThreadPassword(
            create_string_buffer(password.encode()),
        )

    def OesApi_SetCustomizedDriverId(self, driver_id):
        return self._OesApi_SetCustomizedDriverId(
            create_string_buffer(driver_id.encode()),
        )

    def OesApi_SetDefaultEntrustWay(self, entrust_way):
        return self._OesApi_SetDefaultEntrustWay(
            c_char(entrust_way),
        )

    def OesApi_SetThreadBusinessType(self, business_type):
        self._OesApi_SetThreadBusinessType(
            c_int32(business_type),
        )

    def OesApi_InitAll(self, cfg_file, last_rpt_seq_num, last_cl_seq_no):
        return self._OesApi_InitAll(
            byref(self.client_env),
            None if cfg_file is None else create_string_buffer(cfg_file.encode()),
            create_string_buffer(OESAPI_CFG_DEFAULT_SECTION_LOGGER.encode()),
            create_string_buffer(OESAPI_CFG_DEFAULT_SECTION.encode()),
            create_string_buffer(OESAPI_CFG_DEFAULT_KEY_ORD_ADDR.encode()),
            create_string_buffer(OESAPI_CFG_DEFAULT_KEY_RPT_ADDR.encode()),
            create_string_buffer(OESAPI_CFG_DEFAULT_KEY_QRY_ADDR.encode()),
            last_rpt_seq_num,
            None if last_cl_seq_no is None else byref(last_cl_seq_no)
        )

    def OesApi_LogoutAll(self, is_destory):
        return self._OesApi_LogoutAll(
            byref(self.client_env),
            BOOL(is_destory)
        )

    def OesApi_DestoryAll(self):
        return self._OesApi_DestoryAll(
            byref(self.client_env)
        )

    def OesApi_SendOrderReq(self, ord_req):
        return self._OesApi_SendOrderReq(
            byref(self.ord_channel),
            None if ord_req is None else byref(ord_req)
        )

    def OesApi_SendOrderCancelReq(self, cancel_req):
        return self._OesApi_SendOrderCancelReq(
            byref(self.ord_channel),
            None if cancel_req is None else byref(cancel_req)
        )

    def OesApi_GetClientOverview(self, out_client_overview):
        return self._OesApi_GetClientOverview(
            byref(self.qry_channel),
                                              None if out_client_overview is None else byref(out_client_overview)
        )

    def OesApi_HasStockStatus(self, stock_item, status):
        return self._OesApi_HasStockStatus(
            None if stock_item is None else byref(stock_item),
                                           c_uint32(status)
        )

    def OesApi_QueryStock(self, qry_filter, fn_qry_msg_callback, callback_params):
        return self._OesApi_QueryStock(
            byref(self.qry_channel),
                                       None if qry_filter is None else byref(qry_filter),
                                       F_OESAPI_ON_QRY_MSG_T(fn_qry_msg_callback),
                                       None if callback_params is None else byref(callback_params)
        )

    def OesApi_QueryCashAsset(self, qry_filter, fn_qry_msg_callback, callback_params):
        return self._OesApi_QueryCashAsset(
            byref(self.qry_channel),
                                           None if qry_filter is None else byref(qry_filter),
                                           F_OESAPI_ON_QRY_MSG_T(fn_qry_msg_callback),
                                           None if callback_params is None else byref(callback_params)
        )

    def OesApi_QueryStkHolding(self, qry_filter, fn_qry_msg_callback, callback_params):
        return self._OesApi_QueryStkHolding(
            byref(self.qry_channel),
                                            None if qry_filter is None else byref(qry_filter),
                                            F_OESAPI_ON_QRY_MSG_T(fn_qry_msg_callback),
                                            None if callback_params is None else byref(callback_params)
        )

    def OesApi_QueryMarketState(self, qry_filter, fn_qry_msg_callback, callback_params):
        return self._OesApi_QueryMarketState(
            byref(self.qry_channel),
                                             None if qry_filter is None else byref(qry_filter),
                                             F_OESAPI_ON_QRY_MSG_T(fn_qry_msg_callback),
                                             None if callback_params is None else byref(callback_params)
        )

    def OesApi_GetLastRecvTime(self, session_info):
        return self._OesApi_GetLastRecvTime(None if session_info is None else byref(session_info))

    def OesApi_WaitReportMsg(self, timeout_ms, fn_on_msg_callback, callback_params):
        return self._OesApi_WaitReportMsg(
            byref(self.rpt_channel),
                                          c_int32(timeout_ms),
                                          F_OESAPI_ON_RPT_MSG_T(fn_on_msg_callback),
                                          None if callback_params is None else byref(callback_params)
        )

    def OesApi_SendOptSettlementConfirmReq(self, opt_settlement_confirm_req, out_settlement_confirm_rsp):
        return self._OesApi_SendOptSettlementConfirmReq(
            byref(self.ord_channel),
            byref(opt_settlement_confirm_req),
            byref(out_settlement_confirm_rsp)
        )

    def OesApi_QueryOption(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryOption(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryOptHolding(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryOptHolding(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryOptUnderlyingHolding(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryOptUnderlyingHolding(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryOptPositionLimit(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryOptPositionLimit(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryOptPurchaseLimit(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryOptPurchaseLimit(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryOptSettlementStatement(self, cust_id, out_settl_info_buf, buf_size):
        return self._OesApi_QueryOptSettlementStatement(
            byref(self.qry_channel),
            None if cust_id is None else create_string_buffer(cust_id.encode()),
            byref(out_settl_info_buf),
            c_int32(buf_size),
        )

    def OesApi_QueryOptExerciseAssign(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryOptExerciseAssign(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryNotifyInfo(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryNotifyInfo(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_ParseAddrListString(self, uri_list, out_addr_list, addr_list_length):
        return self._OesApi_ParseAddrListString(
            create_string_buffer(uri_list.encode()),
            byref(out_addr_list),
            c_int32(addr_list_length),
        )

    def OesApi_QueryBrokerParamsInfo(self, out_broker_params):
        return self._OesApi_QueryBrokerParamsInfo(
            byref(self.qry_channel),
            byref(out_broker_params),
        )

    def OesApi_QueryCounterCash(self, cash_acct_id, out_counter_cash_item):
        return self._OesApi_QueryCounterCash(
            byref(self.qry_channel),
            None if cash_acct_id is None else create_string_buffer(cash_acct_id.encode()),
            byref(out_counter_cash_item),
        )

    def OesApi_QuerySingleCashAsset(self, cash_acct_id, out_cash_asset_item):
        return self._OesApi_QuerySingleCashAsset(
            byref(self.qry_channel),
            None if cash_acct_id is None else create_string_buffer(cash_acct_id.encode()),
            byref(out_cash_asset_item),
        )

    def OesApi_QuerySingleStkHolding(self, inv_acct_id, security_id, out_holding_item):
        return self._OesApi_QuerySingleStkHolding(
            byref(self.qry_channel),
            create_string_buffer(inv_acct_id.encode()),
            create_string_buffer(security_id.encode()),
            byref(out_holding_item),
        )

    def OesApi_QuerySingleOrder(self, seq_no, out_ord_item):
        return self._OesApi_QuerySingleOrder(
            byref(self.qry_channel),
            c_int32(seq_no),
            byref(out_ord_item),
        )

    def OesApi_QueryCustInfo(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCustInfo(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryInvAcct(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryInvAcct(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryIssue(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryIssue(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryLotWinning(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryLotWinning(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryCommissionRate(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCommissionRate(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryEtf(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryEtf(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryEtfComponent(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryEtfComponent(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryOrder(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryOrder(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryTrade(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryTrade(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryFundTransferSerial(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryFundTransferSerial(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QuerySingleOptHolding(self, inv_acct_id, security_id, mkt_id, position_type, out_holding_item):
        return self._OesApi_QuerySingleOptHolding(
            byref(self.qry_channel),
            create_string_buffer(inv_acct_id.encode()),
            create_string_buffer(security_id.encode()),
            c_uint8(mkt_id),
            c_uint8(position_type),
            byref(out_holding_item),
        )

    def OesApi_SendCreditCashRepayReq(self, cl_seq_no, repay_amt, repay_mode, debt_id, user_info):
        return self._OesApi_SendCreditCashRepayReq(
            byref(self.ord_channel),
            c_int32(cl_seq_no),
            c_int64(repay_amt),
            c_uint32(repay_mode),
            None if debt_id is None else create_string_buffer(debt_id.encode()),
            None if user_info is None else byref(user_info),
        )

    def OesApi_SendCreditRepayReq(self, ord_req, repay_mode, debt_id):
        return self._OesApi_SendCreditRepayReq(
            byref(self.ord_channel),
            byref(ord_req),
            c_uint32(repay_mode),
            None if debt_id is None else create_string_buffer(debt_id.encode()),
        )

    def OesApi_QueryCrdDebtContract(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCrdDebtContract(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryCrdSecurityDebtStats(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCrdSecurityDebtStats(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryCrdCreditAsset(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCrdCreditAsset(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryCrdCashPosition(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCrdCashPosition(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryCrdSecurityPosition(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCrdSecurityPosition(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_GetCrdDrawableBalance(self, out_drawable_balance_item):
        return self._OesApi_GetCrdDrawableBalance(
            byref(self.qry_channel),
            byref(out_drawable_balance_item),
        )

    def OesApi_GetCrdCollateralTransferOutMaxQty(self, security_id, mkt_id, out_transfer_out_qty_item):
        return self._OesApi_GetCrdCollateralTransferOutMaxQty(
            byref(self.qry_channel),
            create_string_buffer(security_id.encode()),
            c_uint8(mkt_id),
            None if out_transfer_out_qty_item is None else byref(out_transfer_out_qty_item),
        )

    def OesApi_QueryCrdDebtJournal(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCrdDebtJournal(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryCrdExcessStock(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCrdExcessStock(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryCrdCashRepayOrder(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCrdCashRepayOrder(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )

    def OesApi_QueryCrdInterestRate(self, qry_filter, qry_msg_callback, callback_params):
        return self._OesApi_QueryCrdInterestRate(
            byref(self.qry_channel),
            None if qry_filter is None else byref(qry_filter),
            F_OESAPI_ON_QRY_MSG_T(qry_msg_callback),
            None if callback_params is None else byref(callback_params),
        )