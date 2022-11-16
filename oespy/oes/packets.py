from enum import Enum

from ..spk.types import STimespec32T
from ..utils import BaseStructure, BaseUnion
from ..utils.types import *
from .base_constants import (OES_MAX_TEST_REQ_ID_LEN, OES_MAX_SENDING_TIME_LEN, OES_CLIENT_NAME_MAX_LEN,
                             OES_PWD_MAX_LEN, OES_CUST_ID_MAX_LEN)
from .base_model import (OesOrdReqT, OesOrdCnfmT, OesOrdRejectT, OesTrdCnfmT, OesFundTrsfRejectT,
                         OesFundTrsfReportT, OesCashAssetReportT, OesStkHoldingReportT, OesNotifyInfoReportT,
                         OesCrdCashRepayReportT, OesOrdCancelReqT, OesCrdRepayReqT, OesCrdCashRepayReqT,
                         OesFundTrsfReqT, OesMarketStateInfoT)
from .base_model_credit import OesCrdDebtContractReportT, OesCrdDebtJournalReportT
from .base_model_option import (OesOptHoldingReportT, OesOptSettlementConfirmBaseInfoT, OesOptUnderlyingHoldingReportT,
                                OesOptSettlementConfirmReportT)
from .qry_packets import *
from .qry_packets_credit import *
from .qry_packets_option import *


OES_APPL_VER_ID = '0.17.6.3'
OES_APPL_VER_VALUE = 1001706031
OES_MIN_APPL_VER_ID = '0.15.5'
OES_APPL_NAME = 'OES'


class eOesMsgTypeT(Enum):
    OESMSG_ORD_NEW_ORDER = 0x01
    OESMSG_ORD_CANCEL_REQUEST = 0x02
    OESMSG_ORD_BATCH_ORDERS = 0x03
    OESMSG_ORD_CREDIT_REPAY = 0x04
    OESMSG_ORD_CREDIT_CASH_REPAY = 0x05

    OESMSG_NONTRD_FUND_TRSF_REQ = 0xC1
    OESMSG_NONTRD_CHANGE_PASSWORD = 0xC2
    OESMSG_NONTRD_OPT_CONFIRM_SETTLEMENT = 0xC3

    OESMSG_RPT_SERVICE_STATE = 0x0E
    OESMSG_RPT_MARKET_STATE = 0x10
    OESMSG_RPT_REPORT_SYNCHRONIZATION = 0x11

    OESMSG_RPT_BUSINESS_REJECT = 0x12
    OESMSG_RPT_ORDER_INSERT = 0x13
    OESMSG_RPT_ORDER_REPORT = 0x14
    OESMSG_RPT_TRADE_REPORT = 0x15

    OESMSG_RPT_FUND_TRSF_REJECT = 0x16
    OESMSG_RPT_FUND_TRSF_REPORT = 0x17

    OESMSG_RPT_CASH_ASSET_VARIATION = 0x18
    OESMSG_RPT_STOCK_HOLDING_VARIATION = 0x19
    OESMSG_RPT_OPTION_HOLDING_VARIATION = 0x1A
    OESMSG_RPT_OPTION_UNDERLYING_HOLDING_VARIATION = 0x1B
    OESMSG_RPT_OPTION_SETTLEMENT_CONFIRMED = 0x1C
    OESMSG_RPT_NOTIFY_INFO = 0x1E
    OESMSG_RPT_CREDIT_CASH_REPAY_REPORT = 0x20
    OESMSG_RPT_CREDIT_DEBT_CONTRACT_VARIATION = 0x21
    OESMSG_RPT_CREDIT_DEBT_JOURNAL = 0x22

    OESMSG_QRYMSG_OPT_HLD = 0x35
    OESMSG_QRYMSG_CUST = 0x36
    OESMSG_QRYMSG_COMMISSION_RATE = 0x38
    OESMSG_QRYMSG_FUND_TRSF = 0x39
    OESMSG_QRYMSG_ETF = 0x3B
    OESMSG_QRYMSG_OPTION = 0x3D
    OESMSG_QRYMSG_LOT_WINNING = 0x3F
    OESMSG_QRYMSG_TRADING_DAY = 0x40
    OESMSG_QRYMSG_MARKET_STATE = 0x41
    OESMSG_QRYMSG_COUNTER_CASH = 0x42
    OESMSG_QRYMSG_OPT_UNDERLYING_HLD = 0x43
    OESMSG_QRYMSG_NOTIFY_INFO = 0x44
    OESMSG_QRYMSG_OPT_POSITION_LIMIT = 0x45
    OESMSG_QRYMSG_OPT_PURCHASE_LIMIT = 0x46
    OESMSG_QRYMSG_BROKER_PARAMS = 0x48
    OESMSG_QRYMSG_COLOCATION_PEER_CASH = 0x49

    OESMSG_QRYMSG_INV_ACCT = 0x51
    OESMSG_QRYMSG_ORD = 0x54
    OESMSG_QRYMSG_TRD = 0x55
    OESMSG_QRYMSG_OPT_EXERCISE_ASSIGN = 0x56
    OESMSG_QRYMSG_ISSUE = 0x57
    OESMSG_QRYMSG_STOCK = 0x58
    OESMSG_QRYMSG_ETF_COMPONENT = 0x59
    OESMSG_QRYMSG_CLIENT_OVERVIEW = 0x5A
    OESMSG_QRYMSG_CASH_ASSET = 0x5B
    OESMSG_QRYMSG_STK_HLD = 0x5C

    OESMSG_QRYMSG_CRD_DEBT_CONTRACT = 0x80
    OESMSG_QRYMSG_CRD_CUST_SECU_DEBT_STATS = 0x81
    OESMSG_QRYMSG_CRD_CREDIT_ASSET = 0x82
    OESMSG_QRYMSG_CRD_CASH_REPAY_INFO = 0x83
    OESMSG_QRYMSG_CRD_CASH_POSITION = 0x84
    OESMSG_QRYMSG_CRD_SECURITY_POSITION = 0x85
    OESMSG_QRYMSG_CRD_EXCESS_STOCK = 0x86
    OESMSG_QRYMSG_CRD_DEBT_JOURNAL = 0x87
    OESMSG_QRYMSG_CRD_INTEREST_RATE = 0x88
    OESMSG_QRYMSG_CRD_UNDERLYING_INFO = 0x89
    OESMSG_QRYMSG_CRD_DRAWABLE_BALANCE = 0x90
    OESMSG_QRYMSG_CRD_COLLATERAL_TRANSFER_OUT_MAX_QTY = 0x91

    OESMSG_SESS_HEARTBEAT = 0xFA
    OESMSG_SESS_TEST_REQUEST = 0xFB
    OESMSG_SESS_LOGIN_EXTEND = 0xFC
    OESMSG_SESS_LOGOUT = 0xFE


class eOesSubscribeReportTypeT(Enum):
    OES_SUB_RPT_TYPE_DEFAULT = 0
    OES_SUB_RPT_TYPE_BUSINESS_REJECT = 0x01
    OES_SUB_RPT_TYPE_ORDER_INSERT = 0x02
    OES_SUB_RPT_TYPE_ORDER_REPORT = 0x04
    OES_SUB_RPT_TYPE_TRADE_REPORT = 0x08
    OES_SUB_RPT_TYPE_FUND_TRSF_REPORT = 0x10
    OES_SUB_RPT_TYPE_CASH_ASSET_VARIATION = 0x20
    OES_SUB_RPT_TYPE_HOLDING_VARIATION = 0x40
    OES_SUB_RPT_TYPE_MARKET_STATE = 0x80
    OES_SUB_RPT_TYPE_NOTIFY_INFO = 0x100
    OES_SUB_RPT_TYPE_SETTLEMETN_CONFIRMED = 0x200
    OES_SUB_RPT_TYPE_CREDIT_CASH_REPAY_REPORT = 0x400
    OES_SUB_RPT_TYPE_CREDIT_DEBT_CONTRACT_VARIATION = 0x800
    OES_SUB_RPT_TYPE_CREDIT_DEBT_JOURNAL = 0x1000
    OES_SUB_RPT_TYPE_ALL = 0xFFFF


class OesReportSynchronizationReqT(BaseStructure):
    _fields_ = [
        ('lastRptSeqNum', c_int64),
        ('subscribeEnvId', c_int8),
        ('__filler', c_uint8 * 3),
        ('subscribeRptTypes', c_int32),
    ]


class OesReportSynchronizationRspT(BaseStructure):
    _fields_ = [
        ('lastRptSeqNum', c_int64),
        ('subscribeEnvId', c_int8),
        ('__filler', c_uint8 * 3),
        ('subscribeRptTypes', c_int32),
    ]


class OesTestRequestReqT(BaseStructure):
    _fields_ = [
        ('testReqId', c_char * OES_MAX_TEST_REQ_ID_LEN),
        ('sendTime', c_char * OES_MAX_SENDING_TIME_LEN),
        ('__filler', c_char * 2),
    ]


class OesTestRequestRspT(BaseStructure):
    _fields_ = [
        ('testReqId', c_char * OES_MAX_TEST_REQ_ID_LEN),
        ('origSendTime', c_char * OES_MAX_SENDING_TIME_LEN),
        ('__filler1', c_char * 2),
        ('respTime', c_char * OES_MAX_SENDING_TIME_LEN),
        ('__filler2', c_char * 2),

        ('__recvTime', STimespec32T),
        ('__collectedTime', STimespec32T),
        ('__pushingTime', STimespec32T),
    ]


class OesBatchOrdersHeadT(BaseStructure):
    _fields_ = [
        ('itemCount', c_int32),
        ('__filler', c_int32),
    ]


class OesBatchOrdersReqT(BaseStructure):
    _fields_ = [
        ('batchHead', OesBatchOrdersHeadT),
        ('items', OesOrdReqT * 1),
    ]


class _UserInfo(BaseUnion):
    _fields_ = [
        ('u64', c_uint64),
        ('i64', c_int64),
        ('u32', c_uint32 * 2),
        ('i32', c_int32 * 2),
        ('c8', c_char * 8),
    ]


class OesChangePasswordReqT(BaseStructure):
    _fields_ = [
        ('encryptMethod', c_int32),
        ('__filler', c_int32),
        ('username', c_char * OES_CLIENT_NAME_MAX_LEN),
        ('userInfo', _UserInfo),
        ('oldPassword', c_char * OES_PWD_MAX_LEN),
        ('newPassword', c_char * OES_PWD_MAX_LEN),
    ]


class OesChangePasswordRspT(BaseStructure):
    _fields_ = [
        ('encryptMethod', c_int32),
        ('__filler', c_int32),

        ('username', c_char * OES_CLIENT_NAME_MAX_LEN),
        ('userInfo', _UserInfo),

        ('clientId', c_int16),
        ('clEnvId', c_int8),
        ('__filler2', c_int8),

        ('transDate', c_int32),
        ('transTime', c_int32),
        ('rejReason', c_int32),
    ]


class OesOptSettlementConfirmReqT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('userInfo', _UserInfo),
    ]


OesOptSettlementConfirmRspT = OesOptSettlementConfirmBaseInfoT


class OesRptMsgHeadT(BaseStructure):
    _fields_ = [
        ('rptSeqNum', c_int64),

        ('rptMsgType', c_uint8),
        ('execType', c_uint8),
        ('bodyLength', c_int16),

        ('ordRejReason', c_int32),
    ]


class OesRptMsgBodyT(BaseUnion):
    _fields_ = [
        ('ordInsertRsp', OesOrdCnfmT),
        ('ordRejectRsp', OesOrdRejectT),

        ('ordCnfm', OesOrdCnfmT),
        ('trdCnfm', OesTrdCnfmT),

        ('fundTrsfRejectRsp', OesFundTrsfRejectT),
        ('fundTrsfCnfm', OesFundTrsfReportT),

        ('cashAssetRpt', OesCashAssetReportT),
        ('stkHoldingRpt', OesStkHoldingReportT),
        ('optHoldingRpt', OesOptHoldingReportT),
        ('optUnderlyingHoldingRpt', OesOptUnderlyingHoldingReportT),

        ('notifyInfoRpt', OesNotifyInfoReportT),
        ('optSettlementConfirmRpt', OesOptSettlementConfirmReportT),

        ('crdDebtCashRepayRpt', OesCrdCashRepayReportT),
        ('crdDebtContractRpt', OesCrdDebtContractReportT),
        ('crdDebtJournalRpt', OesCrdDebtJournalReportT),
    ]


class OesRptMsgT(BaseStructure):
    _fields_ = [
        ('rptHead', OesRptMsgHeadT),
        ('rptBody', OesRptMsgBodyT),
    ]


class OesReqMsgBodyT(BaseUnion):
    _fields_ = [
        ('ordReq', OesOrdReqT),
        ('ordCancelReq', OesOrdCancelReqT),
        ('batchOrdersReq', OesBatchOrdersReqT),
        ('crdRepayReq', OesCrdRepayReqT),
        ('crdCashRepayReq', OesCrdCashRepayReqT),
        ('fundTrsfReq', OesFundTrsfReqT),
        ('changePasswordReq', OesChangePasswordReqT),
        ('optSettlementConfirmReq', OesOptSettlementConfirmReqT),
        ('testRequestReq', OesTestRequestReqT),
        ('rptSyncReq', OesReportSynchronizationReqT),
    ]


class OesRspMsgBodyT(BaseUnion):
    _fields_ = [
        ('rptMsg', OesRptMsgT),
        ('mktStateRpt', OesMarketStateInfoT),
        ('testRequestRsp', OesTestRequestRspT),
        ('reportSynchronizationRsp', OesReportSynchronizationRspT),
        ('changePasswordRsp', OesChangePasswordRspT),
        ('optSettlementConfirmRsp', OesOptSettlementConfirmRspT),
    ]


class OesQryReqMsgT(BaseUnion):
    _fields_ = [
        ('qryOrd', OesQryOrdReqT),
        ('qryTrd', OesQryTrdReqT),
        ('qryCashAsset', OesQryCashAssetReqT),
        ('qryColoPeerCash', OesQryColocationPeerCashReqT),
        ('qryStkHolding', OesQryStkHoldingReqT),
        ('qryOptHolding', OesQryOptHoldingReqT),
        ('qryCust', OesQryCustReqT),
        ('qryInvAcct', OesQryInvAcctReqT),
        ('qryComms', OesQryCommissionRateReqT),
        ('qryFundTrsf', OesQryFundTransferSerialReqT),
        ('qryLotWinning', OesQryLotWinningReqT),
        ('qryIssue', OesQryIssueReqT),
        ('qryStock', OesQryStockReqT),
        ('qryEtf', OesQryEtfReqT),
        ('qryEtfComponent', OesQryEtfComponentReqT),
        ('qryOption', OesQryOptionReqT),
        ('qryMktState', OesQryMarketStateReqT),
        ('qryNotifyInfo', OesQryNotifyInfoReqT),
        ('qryCounterCash', OesQryCounterCashReqT),
        ('qryOptPositionLimit', OesQryOptPositionLimitReqT),
        ('qryOptPurchaseLimit', OesQryOptPurchaseLimitReqT),
        ('qryOptUnderlyingHolding', OesQryOptUnderlyingHoldingReqT),
        ('qryOptExerciseAssign', OesQryOptExerciseAssignReqT),

        ('qryCrdDebtContract', OesQryCrdDebtContractReqT),
        ('qryCrdCustSecuDebtStats', OesQryCrdSecurityDebtStatsReqT),
        ('qryCrdCreditAsset', OesQryCrdCreditAssetReqT),
        ('qryCrdCashRepay', OesQryCrdCashRepayReqT),
        ('qryCrdCashPosition', OesQryCrdCashPositionReqT),
        ('qryCrdSecurityPosition', OesQryCrdSecurityPositionReqT),
        ('qryCrdExcessStock', OesQryCrdExcessStockReqT),
        ('qryCrdDebtJournal', OesQryCrdDebtJournalReqT),
        ('qryCrdInterestRateReq', OesQryCrdInterestRateReqT),
        ('qryCrdUnderlyingInfoReq', OesQryCrdUnderlyingInfoReqT),
        ('qryCrdDrawableBalanceReq', OesQryCrdDrawableBalanceReqT),
        ('qryCrdTransferOutMaxQtyReq', OesQryCrdCollateralTransferOutMaxQtyReqT),
    ]


class OesQryRspMsgT(BaseUnion):
    _fields_ = [
        ('ordRsp', OesQryOrdRspT),
        ('trdRsp', OesQryTrdRspT),
        ('cashAssetRsp', OesQryCashAssetRspT),
        ('qryColoPeerCashRsp', OesQryColocationPeerCashRspT),
        ('stkHoldingRsp', OesQryStkHoldingRspT),
        ('optHoldingRsp', OesQryOptHoldingRspT),
        ('custRsp', OesQryCustRspT),
        ('invAcctRsp', OesQryInvAcctRspT),
        ('commsRateRsp', OesQryCommissionRateRspT),
        ('fundTrsfRsp', OesQryFundTransferSerialRspT),
        ('lotWinningRsp', OesQryLotWinningRspT),
        ('issueRsp', OesQryIssueRspT),
        ('stockRsp', OesQryStockRspT),
        ('etfRsp', OesQryEtfRspT),
        ('etfComponentRsp', OesQryEtfComponentRspT),
        ('optionRsp', OesQryOptionRspT),
        ('tradingDay', OesQryTradingDayRspT),
        ('mktStateRsp', OesQryMarketStateRspT),
        ('notifyInfoRsp', OesQryNotifyInfoRspT),
        ('clientOverview', OesClientOverviewT),
        ('counterCashRsp', OesQryCounterCashRspT),
        ('optPositionLimitRsp', OesQryOptPositionLimitRspT),
        ('optPurchaseLimitRsp', OesQryOptPurchaseLimitRspT),
        ('optUnderlyingHoldingRsp', OesQryOptUnderlyingHoldingRspT),
        ('optExerciseAssignRsp', OesQryOptExerciseAssignRspT),
        ('brokerParamsRsp', OesQryBrokerParamsInfoRspT),
        ('applUpgradeRsp', OesQryApplUpgradeInfoRspT),

        ('crdDebtContractRsp', OesQryCrdDebtContractRspT),
        ('crdCustSecuDebtStatsRsp', OesQryCrdSecurityDebtStatsRspT),
        ('crdCreditAssetRsp', OesQryCrdCreditAssetRspT),
        ('crdCashRepayRsp', OesQryCrdCashRepayRspT),
        ('crdCashPositionRsp', OesQryCrdCashPositionRspT),
        ('crdSecurityPositionRsp', OesQryCrdSecurityPositionRspT),
        ('crdExcessStockRsp', OesQryCrdExcessStockRspT),
        ('crdDebtJournalRsp', OesQryCrdDebtJournalRspT),
        ('crdInterestRateRsp', OesQryCrdInterestRateRspT),
        ('crdCustUnderlyingInfoRsp', OesQryCrdUnderlyingInfoRspT),
        ('crdDrawableBalanceRsp', OesQryCrdDrawableBalanceRspT),
        ('crdTransferOutMaxQtyRsp', OesQryCrdCollateralTransferOutMaxQtyRspT),
    ]
