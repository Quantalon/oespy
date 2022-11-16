
from ..spk.types import STimespec32T
from ..utils import BaseStructure, BaseUnion
from ..utils.types import *

from .base_constants import (OES_INV_ACCT_ID_MAX_LEN, OES_SECURITY_ID_MAX_LEN, OES_EXCH_ORDER_ID_MAX_LEN,
                             OES_CASH_ACCT_ID_MAX_LEN, OES_CREDIT_DEBT_ID_MAX_LEN, OES_SECURITY_NAME_MAX_LEN,
                             OES_PWD_MAX_LEN, OES_MAX_ERROR_INFO_LEN, OES_MAX_ALLOT_SERIALNO_LEN,
                             OES_CUST_ID_MAX_LEN, OES_NOTIFY_CONTENT_MAX_LEN)
from .base_model_credit import OesCrdCreditAssetBaseInfoT, OesCrdSecurityDebtStatsBaseInfoT


class _UserInfo(BaseUnion):
    _fields_ = [
        ('u64', c_uint64),
        ('i64', c_int64),
        ('u32', c_uint32),
        ('i32', c_int32),
        ('c8', c_char),
    ]


_OES_ORD_BASE_INFO_PKT = [
    ('clSeqNo', c_int32),
    ('mktId', c_uint8),
    ('ordType', c_uint8),
    ('bsType', c_uint8),
    ('__ORD_BASE_INFO_filler', c_uint8),
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

    ('ordQty', c_int32),
    ('ordPrice', c_int32),
    ('origClOrdId', c_int64),

    ('userInfo', _UserInfo),
]

_OES_ORD_CANCEL_BASE_INFO_PKT = [
    ('clSeqNo', c_int32),
    ('mktId', c_uint8),
    ('__ORD_CANCEL_BASE_INFO_filler1', c_uint8 * 3),
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

    ('origClSeqNo', c_int32),
    ('origClEnvId', c_int8),
    ('__ORD_CANCEL_BASE_INFO_filler2', c_uint8 * 3),
    ('origClOrdId', c_int64),

    ('userInfo', _UserInfo),
]


_OES_ORD_REQ_LATENCY_FIELDS_IMPL = [
    ('__ordReqOrigSendTime', STimespec32T),
]


_OES_ORD_CNFM_LATENCY_FIELDS_IMPL = [
    ('__ordReqOrigRecvTime', STimespec32T),
    ('__ordReqCollectedTime', STimespec32T),
    ('__ordReqActualDealTime', STimespec32T),
    ('__ordReqProcessedTime', STimespec32T),

    ('__ordCnfmOrigRecvTime', STimespec32T),
    ('__ordCnfmCollectedTime', STimespec32T),
    ('__ordCnfmActualDealTime', STimespec32T),
    ('__ordCnfmProcessedTime', STimespec32T),

    ('__ordDeclareTime', STimespec32T),
    ('__ordDeclareDoneTime', STimespec32T),

    ('__pushingTime', STimespec32T),
]

_OES_ORD_REQ_LATENCY_FIELDS = _OES_ORD_REQ_LATENCY_FIELDS_IMPL
_OES_ORD_CNFM_LATENCY_FIELDS = _OES_ORD_CNFM_LATENCY_FIELDS_IMPL

_OES_ORD_CNFM_BASE_INFO_PKT = _OES_ORD_BASE_INFO_PKT + _OES_ORD_REQ_LATENCY_FIELDS + [
    ('clOrdId', c_int64),
    ('clientId', c_int16),
    ('clEnvId', c_int8),
    ('origClEnvId', c_int8),
    ('origClSeqNo', c_int32),

    ('ordDate', c_int32),
    ('ordTime', c_int32),
    ('ordCnfmTime', c_int32),

    ('ordStatus', c_uint8),
    ('ordCnfmSts', c_uint8),
    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),

    ('__platformId', c_uint8),
    ('__tgwGrpNo', c_uint8),
    ('__tgwPartitionNo', c_uint8),
    ('productType', c_uint8),
    ('exchOrdId', c_char * OES_EXCH_ORDER_ID_MAX_LEN),
    ('__declareFlag', c_uint8),
    ('__repeatFlag', c_uint8),
    ('ownerType', c_uint8),

    ('frzAmt', c_int64),
    ('frzInterest', c_int64),
    ('frzFee', c_int64),
    ('cumAmt', c_int64),
    ('cumInterest', c_int64),
    ('cumFee', c_int64),

    ('cumQty', c_int32),
    ('canceledQty', c_int32),

    ('ordRejReason', c_int32),
    ('exchErrCode', c_int32),
    ('pbuId', c_int32),
    ('branchId', c_int32),
    ('__rowNum', c_int32),
    ('__recNum', c_uint32),
] + _OES_ORD_CNFM_LATENCY_FIELDS


_OES_ORD_CNFM_EXT_INFO_PKT = [
    ('frzMargin', c_int64),
    ('cumMargin', c_int64),
    ('businessType', c_uint8),
    ('mandatoryFlag', c_uint8),
    ('repayMode', c_uint8),
    ('__ORD_CNFM_EXT_filler', c_uint8 * 5),
    ('__ORD_CNFM_EXT_reserve', c_char * 16),
]


class OesOrdReqT(BaseStructure):
    _fields_ = _OES_ORD_BASE_INFO_PKT + _OES_ORD_REQ_LATENCY_FIELDS


class OesOrdCancelReqT(BaseStructure):
    _fields_ = _OES_ORD_CANCEL_BASE_INFO_PKT + _OES_ORD_REQ_LATENCY_FIELDS


class OesOrdRejectT(BaseStructure):
    _fields_ = _OES_ORD_BASE_INFO_PKT + _OES_ORD_REQ_LATENCY_FIELDS + [
        ('origClSeqNo', c_int32),
        ('origClEnvId', c_int8),
        ('clEnvId', c_int8),
        ('clientId', c_int16),
        ('ordDate', c_int32),
        ('ordTime', c_int32),
        ('ordRejReason', c_int32),
        ('businessType', c_uint8),
        ('__filler', c_uint8 * 3),
    ]


class OesOrdCnfmT(BaseStructure):
    _fields_ = _OES_ORD_CNFM_BASE_INFO_PKT + _OES_ORD_CNFM_EXT_INFO_PKT


class OesCrdRepayReqT(BaseStructure):
    _fields_ = [
        ('ordReq', OesOrdReqT),
        ('repayMode', c_uint8),
        ('__filler', c_uint8 * 7),
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
    ]


_OES_CRD_CASH_REPAY_REQ_BASE_PKT = [
    ('clSeqNo', c_int32),
    ('repayMode', c_uint8),
    ('repayJournalType', c_uint8),
    ('__CRD_CASH_REPAY_REQ_BASE_filler', c_uint8 * 2),

    ('repayAmt', c_int64),

    ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
    ('userInfo', _UserInfo),
]


class OesCrdCashRepayReqT(BaseStructure):
    _fields_ = _OES_CRD_CASH_REPAY_REQ_BASE_PKT + _OES_ORD_REQ_LATENCY_FIELDS


class OesCrdCashRepayReportT(BaseStructure):
    _fields_ = _OES_CRD_CASH_REPAY_REQ_BASE_PKT + _OES_ORD_REQ_LATENCY_FIELDS + [
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('__filler1', c_uint8 * 7),
        ('ordPrice', c_int32),
        ('ordQty', c_int32),
        ('ordDate', c_int32),
        ('ordTime', c_int32),
        ('clOrdId', c_int64),
        ('clientId', c_int16),
        ('clEnvId', c_int8),
        ('mandatoryFlag', c_uint8),
        ('ordStatus', c_uint8),
        ('ownerType', c_uint8),
        ('__filler2', c_uint8 * 2),
        ('ordRejReason', c_int32),
        ('repaidQty', c_int32),
        ('repaidAmt', c_int64),
        ('repaidFee', c_int64),
        ('repaidInterest', c_int64),
        ('branchId', c_int32),
        ('__filler3', c_int32),
    ]


_OES_TRD_BASE_INFO_PKT = [
    ('exchTrdNum', c_int64),
    ('mktId', c_uint8),
    ('trdSide', c_uint8),
    ('__platformId', c_uint8),
    ('__trdCnfmType', c_uint8),
    ('__etfTrdCnfmSeq', c_uint32),

    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

    ('trdDate', c_int32),
    ('trdTime', c_int32),
    ('trdQty', c_int32),
    ('trdPrice', c_int32),
    ('trdAmt', c_int64),

    ('clOrdId', c_int64),
    ('cumQty', c_int32),
    ('__rowNum', c_int32),

    ('__tgwGrpNo', c_uint8),
    ('__etfCashType', c_uint8),
    ('__tgwPartitionNo', c_uint8),
    ('productType', c_uint8),
    ('origOrdQty', c_int32),

    ('pbuId', c_int32),
    ('branchId', c_int32),
]


_OES_TRD_BASE_LATENCY_FIELDS = [
    ('__trdCnfmOrigRecvTime', STimespec32T),
    ('__trdCnfmCollectedTime', STimespec32T),
    ('__trdCnfmActualDealTime', STimespec32T),
    ('__trdCnfmProcessedTime', STimespec32T),
    ('__pushingTime', STimespec32T),
]


_OES_TRD_CNFM_LATENCY_FIELDS = _OES_TRD_BASE_LATENCY_FIELDS


_OES_TRD_CNFM_BASE_INFO_PKT = _OES_TRD_BASE_INFO_PKT + [
    ('clSeqNo', c_int32),
    ('clientId', c_int16),
    ('clEnvId', c_int8),
    ('subSecurityType', c_uint8),

    ('ordStatus', c_uint8),
    ('ordType', c_uint8),
    ('ordBuySellType', c_uint8),
    ('securityType', c_uint8),
    ('origOrdPrice', c_int32),

    ('cumAmt', c_int64),
    ('cumInterest', c_int64),
    ('cumFee', c_int64),
    ('userInfo', _UserInfo),
] + _OES_TRD_CNFM_LATENCY_FIELDS


_OES_TRD_CNFM_EXT_INFO_PKT = [
    ('trdInterest', c_int64),
    ('trdFee', c_int64),
    ('trdMargin', c_int64),
    ('cumMargin', c_int64),
    ('businessType', c_uint8),
    ('mandatoryFlag', c_uint8),
    ('ownerType', c_uint8),
    ('__TRD_CNFM_EXT_filler', c_uint8 * 5),
    ('__TRD_CNFM_EXT_reserve', c_char * 16),
]


class OesTrdBaseInfoT(BaseStructure):
    _fields_ = _OES_TRD_BASE_INFO_PKT


class OesTrdCnfmT(BaseStructure):
    _fields_ = _OES_TRD_CNFM_BASE_INFO_PKT + _OES_TRD_CNFM_EXT_INFO_PKT


_OES_LOT_WINNING_BASE_INFO_PKT = [
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),
    ('lotType', c_uint8),

    ('rejReason', c_uint8),
    ('__LOT_WINNING_BASE_INFO_filler', c_int8),
    ('lotDate', c_int32),

    ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),

    ('assignNum', c_int64),
    ('lotQty', c_int32),
    ('lotPrice', c_int32),
    ('lotAmt', c_int64),
]


class OesLotWinningBaseInfoT(BaseStructure):
    _fields_ = _OES_LOT_WINNING_BASE_INFO_PKT


_OES_FUND_TRSF_BASE_INFO_PKT = [
    ('clSeqNo', c_int32),
    ('direct', c_uint8),
    ('fundTrsfType', c_uint8),
    ('__FUND_TRSF_BASE_filler', c_uint8 * 2),

    ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ('trdPasswd', c_char * OES_PWD_MAX_LEN),
    ('trsfPasswd', c_char * OES_PWD_MAX_LEN),

    ('occurAmt', c_int64),
    ('userInfo', _UserInfo),
]


class OesFundTrsfBaseInfoT(BaseStructure):
    _fields_ = _OES_FUND_TRSF_BASE_INFO_PKT


class OesFundTrsfReqT(BaseStructure):
    _fields_ = _OES_FUND_TRSF_BASE_INFO_PKT


class OesFundTrsfRejectT(BaseStructure):
    _fields_ = _OES_FUND_TRSF_BASE_INFO_PKT + [
        ('ordDate', c_int32),
        ('ordTime', c_int32),

        ('clientId', c_int16),
        ('clEnvId', c_int8),
        ('__filler', c_int8),
        ('rejReason', c_int32),

        ('errorInfo', c_char * OES_MAX_ERROR_INFO_LEN),
    ]


class OesFundTrsfReportT(BaseStructure):
    _fields_ = [
        ('clSeqNo', c_int32),
        ('clientId', c_int16),
        ('clEnvId', c_int8),
        ('direct', c_uint8),
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),

        ('occurAmt', c_int64),
        ('userInfo', _UserInfo),

        ('fundTrsfId', c_int32),
        ('counterEntrustNo', c_int32),

        ('operDate', c_int32),
        ('operTime', c_int32),
        ('dclrTime', c_int32),
        ('doneTime', c_int32),

        ('fundTrsfType', c_uint8),
        ('trsfStatus', c_uint8),
        ('__hasCounterTransfered', c_uint8),
        ('fundTrsfSourceType', c_uint8),

        ('rejReason', c_int32),
        ('counterErrCode', c_int32),
        ('__filler', c_uint32),
        ('allotSerialNo', c_char * OES_MAX_ALLOT_SERIALNO_LEN),
        ('errorInfo', c_char * OES_MAX_ERROR_INFO_LEN),
    ]


_OES_CUST_BASE_INFO_PKT = [
    ('custId', c_char * OES_CUST_ID_MAX_LEN),

    ('custType', c_uint8),
    ('status', c_uint8),
    ('riskLevel', c_uint8),
    ('originRiskLevel', c_uint8),
    ('institutionFlag', c_uint8),
    ('investorClass', c_uint8),
    ('optSettlementCnfmFlag', c_uint8),
    ('__CUST_BASE_filler1', c_uint8),

    ('branchId', c_int32),
    ('__CUST_BASE_filler2', c_uint32),
]


class OesCustBaseInfoT(BaseStructure):
    _fields_ = _OES_CUST_BASE_INFO_PKT


_OES_INV_ACCT_BASE_INFO_PKT = [
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('mktId', c_uint8),

    ('acctType', c_uint8),
    ('status', c_uint8),
    ('ownerType', c_uint8),
    ('optInvLevel', c_uint8),
    ('isTradeDisabled', c_uint8),
    ('__INV_ACCT_BASE_filler', c_uint8 * 2),

    ('limits', c_uint64),
    ('permissions', c_uint64),

    ('pbuId', c_int32),
    ('stkPositionLimitRatio', c_int32),
    ('subscriptionQuota', c_int32),
    ('kcSubscriptionQuota', c_int32),
    ('riskWarningSecurityBuyQtyLimit', c_int32),

    ('__INV_ACCT_BASE_reserve', c_char * 28),
]


class OesInvAcctBaseInfoT(BaseStructure):
    _fields_ = _OES_INV_ACCT_BASE_INFO_PKT


class OesPriceLimitT(BaseStructure):
    _fields_ = [
        ('upperLimitPrice', c_int32),
        ('lowerLimitPrice', c_int32),
    ]


_OES_TRD_SESS_TYPE_MAX = 4


class _CreditExt(BaseStructure):
    _fields_ = [
        ('collateralRatio', c_int32),
        ('marginBuyRatio', c_int32),
        ('shortSellRatio', c_int32),
        ('fairPrice', c_int32),
    ]


_OES_STOCK_BASE_INFO_PKT = [
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),

    ('productType', c_uint8),
    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),
    ('securityLevel', c_uint8),
    ('securityRiskLevel', c_uint8),
    ('currType', c_uint8),
    ('qualificationClass', c_uint8),

    ('securityStatus', c_uint32),
    ('securityAttribute', c_uint32),
    ('suspFlag', c_uint8),
    ('temporarySuspFlag', c_uint8),
    ('isDayTrading', c_uint8),

    ('isRegistration', c_uint8),
    ('isCrdCollateral', c_uint8),
    ('isCrdMarginTradeUnderlying', c_uint8),
    ('isCrdShortSellUnderlying', c_uint8),
    ('isNoProfit', c_uint8),
    ('isWeightedVotingRights', c_uint8),
    ('isVie', c_uint8),
    ('isHighLiquidity', c_uint8),
    ('isCrdCollateralTradable', c_uint8),

    ('pricingMethod', c_uint8),
    ('__STOCK_BASE_filler', c_uint8 * 3),

    ('priceLimit', OesPriceLimitT * _OES_TRD_SESS_TYPE_MAX),
    ('priceTick', c_int32),
    ('prevClose', c_int32),

    ('lmtBuyMaxQty', c_int32),
    ('lmtBuyMinQty', c_int32),
    ('lmtBuyQtyUnit', c_int32),
    ('mktBuyMaxQty', c_int32),
    ('mktBuyMinQty', c_int32),
    ('mktBuyQtyUnit', c_int32),

    ('lmtSellMaxQty', c_int32),
    ('lmtSellMinQty', c_int32),
    ('lmtSellQtyUnit', c_int32),
    ('mktSellMaxQty', c_int32),
    ('mktSellMinQty', c_int32),
    ('mktSellQtyUnit', c_int32),

    ('bondInterest', c_int64),
    ('parValue', c_int64),
    ('repoExpirationDays', c_int32),
    ('cashHoldDays', c_int32),

    ('auctionLimitType', c_uint8),
    ('auctionReferPriceType', c_uint8),
    ('__STOCK_BASE_filler1', c_uint8 * 2),
    ('auctionUpDownRange', c_int32),

    ('listDate', c_int32),
    ('maturityDate', c_int32),
    ('outstandingShare', c_int64),
    ('publicFloatShare', c_int64),

    ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
    ('__STOCK_BASE_reserve1', c_char * 80),
    ('creditExt', _CreditExt),
    ('__STOCK_BASE_reserve2', c_char * 48),
]


class OesStockBaseInfoT(BaseStructure):
    _fields_ = _OES_STOCK_BASE_INFO_PKT


_OES_ISSUE_BASE_INFO_PKT = [
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),

    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),
    ('productType', c_uint8),
    ('issueType', c_uint8),
    ('isCancelAble', c_uint8),
    ('isReApplyAble', c_uint8),
    ('suspFlag', c_uint8),

    ('securityAttribute', c_uint32),
    ('isRegistration', c_uint8),
    ('isNoProfit', c_uint8),
    ('isWeightedVotingRights', c_uint8),
    ('isVie', c_uint8),
    ('__ISSUE_BASE_filler', c_uint8 * 8),

    ('startDate', c_int32),
    ('endDate', c_int32),

    ('issuePrice', c_int32),
    ('upperLimitPrice', c_int32),
    ('lowerLimitPrice', c_int32),

    ('ordMaxQty', c_int32),
    ('ordMinQty', c_int32),
    ('qtyUnit', c_int32),

    ('issueQty', c_int64),
    ('alotRecordDay', c_int32),
    ('alotExRightsDay', c_int32),

    ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
    ('__ISSUE_BASE_reserve1', c_char * 56),
    ('__ISSUE_BASE_reserve2', c_char * 64),
]


class OesIssueBaseInfoT(BaseStructure):
    _fields_ = _OES_ISSUE_BASE_INFO_PKT


_OES_ETF_BASE_INFO_PKT = [
    ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),

    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),
    ('isPublishIOPV', c_uint8),

    ('isCreationAble', c_uint8),
    ('isRedemptionAble', c_uint8),
    ('isDisabled', c_uint8),
    ('etfAllCashFlag', c_uint8),

    ('componentCnt', c_int32),
    ('creRdmUnit', c_int32),
    ('maxCashRatio', c_int32),
    ('nav', c_int32),

    ('navPerCU', c_int64),
    ('dividendPerCU', c_int64),

    ('tradingDay', c_int32),
    ('preTradingDay', c_int32),
    ('estiCashCmpoent', c_int64),
    ('cashCmpoent', c_int64),
    ('creationLimit', c_int64),
    ('redemLimit', c_int64),
    ('netCreationLimit', c_int64),
    ('netRedemLimit', c_int64),
]


class OesEtfBaseInfoT(BaseStructure):
    _fields_ = _OES_ETF_BASE_INFO_PKT


_OES_ETF_COMPONENT_BASE_INFO_PKT = [
    ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

    ('mktId', c_uint8),
    ('fundMktId', c_uint8),
    ('subFlag', c_uint8),
    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),

    ('isTrdComponent', c_uint8),
    ('__ETF_COMPONENT_BASE_filler', c_uint8 * 2),
    ('prevClose', c_int32),
    ('qty', c_int32),

    ('premiumRatio', c_int32),
    ('discountRatio', c_int32),
    ('creationSubCash', c_int64),
    ('redemptionSubCash', c_int64),
]


class OesEtfComponentBaseInfoT(BaseStructure):
    _fields_ = _OES_ETF_COMPONENT_BASE_INFO_PKT


_OES_CASH_ASSET_BASE_INFO_PKT = [
    ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ('custId', c_char * OES_CUST_ID_MAX_LEN),

    ('currType', c_uint8),
    ('cashType', c_uint8),
    ('cashAcctStatus', c_uint8),
    ('isFundTrsfDisabled', c_uint8),
    ('__CASH_ASSET_BASE_filler', c_uint8 * 4),

    ('beginningBal', c_int64),
    ('beginningAvailableBal', c_int64),
    ('beginningDrawableBal', c_int64),

    ('disableBal', c_int64),
    ('reversalAmt', c_int64),
    ('manualFrzAmt', c_int64),

    ('totalDepositAmt', c_int64),
    ('totalWithdrawAmt', c_int64),
    ('withdrawFrzAmt', c_int64),

    ('totalSellAmt', c_int64),
    ('totalBuyAmt', c_int64),
    ('buyFrzAmt', c_int64),

    ('totalFeeAmt', c_int64),
    ('feeFrzAmt', c_int64),

    ('marginAmt', c_int64),

    ('marginFrzAmt', c_int64),
]


_OES_CASH_ASSET_RPT_INFO_PKT = [
    ('currentTotalBal', c_int64),

    ('currentAvailableBal', c_int64),
    ('currentDrawableBal', c_int64),

    ('totalInternalAllotAmt', c_int64),
    ('internalAllotUncomeAmt', c_int64),

    ('ordTrafficFeeAmt', c_int64),
    ('__CASH_ASSET_RPT_reserve', c_char * 8),
]


class OesCashAssetBaseInfoT(BaseStructure):
    _fields_ = _OES_CASH_ASSET_BASE_INFO_PKT


class _OptionExt(BaseUnion):
    _fields_ = [
        ('initialMargin', c_int64),
        ('totalExerciseFrzAmt', c_int64),
        ('pendingSupplMargin', c_int64),

        ('sseAvailablePurchaseLimit', c_int64),
        ('szseAvailablePurchaseLimit', c_int64),

        ('totalMarketMargin', c_int64),
        ('totalNetMargin', c_int64),
    ]


class _OesCashAssetReportUnion(BaseUnion):
    _fields_ = [
        ('creditExt', OesCrdCreditAssetBaseInfoT),
        ('optionExt', _OptionExt),
        ('__CASH_ASSET_EXT_reserve', c_char * 512),
    ]


class OesCashAssetReportT(BaseStructure):
    _fields_ = _OES_CASH_ASSET_BASE_INFO_PKT + _OES_CASH_ASSET_RPT_INFO_PKT + [
        ('union', _OesCashAssetReportUnion)
    ]


_OES_STK_HOLDING_BASE_INFO_PKT = [
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),
    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),
    ('productType', c_uint8),
    ('isCreditHolding', c_uint8),
    ('__HOLD_BASE_filler', c_uint8 * 3),

    ('originalHld', c_int64),
    ('originalCostAmt', c_int64),

    ('totalBuyHld', c_int64),
    ('totalSellHld', c_int64),
    ('sellFrzHld', c_int64),
    ('manualFrzHld', c_int64),

    ('totalBuyAmt', c_int64),
    ('totalSellAmt', c_int64),
    ('totalBuyFee', c_int64),
    ('totalSellFee', c_int64),

    ('totalTrsfInHld', c_int64),

    ('totalTrsfOutHld', c_int64),

    ('trsfOutFrzHld', c_int64),

    ('originalLockHld', c_int64),
    ('totalLockHld', c_int64),
    ('totalUnlockHld', c_int64),

    ('originalAvlHld', c_int64),

    ('maxReduceQuota', c_int64),
]


_OES_STK_HOLDING_RPT_INFO_PKT = [
    ('sellAvlHld', c_int64),
    ('trsfOutAvlHld', c_int64),
    ('lockAvlHld', c_int64),
    ('__STK_HOLDING_RPT_filler', c_int64),
    ('sumHld', c_int64),
    ('costPrice', c_int64),
    ('__STK_HOLDING_RPT_reserve', c_char * 32),
]


class OesStkHoldingBaseInfoT(BaseStructure):
    _fields_ = _OES_STK_HOLDING_BASE_INFO_PKT


class _OesStkHoldingReportUnion(BaseUnion):
    _fields_ = [
        ('creditExt', OesCrdSecurityDebtStatsBaseInfoT),
        ('__STK_HOLDING_EXT_reserve', c_char * 432),
    ]


class OesStkHoldingReportT(BaseStructure):
    _fields_ = _OES_STK_HOLDING_BASE_INFO_PKT + _OES_STK_HOLDING_RPT_INFO_PKT + [
        ('union', _OesStkHoldingReportUnion),
    ]


class OesMarketStateInfoT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('platformId', c_uint8),
        ('mktId', c_uint8),
        ('mktState', c_uint8),
        ('__filler', c_uint8 * 4),
    ]


_OES_NOTIFY_BASE_INFO_PKT = [
    ('notifySeqNo', c_int32),
    ('notifySource', c_uint8),
    ('notifyType', c_uint8),
    ('notifyLevel', c_uint8),
    ('notifyScope', c_uint8),

    ('tranTime', c_int32),
    ('businessType', c_uint8),
    ('__NOTIFY_INFO_filler1', c_uint8 * 3),

    ('custId', c_char * OES_CUST_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),
    ('__NOTIFY_INFO_filler2', c_uint8),

    ('contentLen', c_int32),
    ('content', c_char * OES_NOTIFY_CONTENT_MAX_LEN),
]


class OesNotifyBaseInfoT(BaseStructure):
    _fields_ = _OES_NOTIFY_BASE_INFO_PKT


class OesNotifyInfoReportT(BaseStructure):
    _fields_ = _OES_NOTIFY_BASE_INFO_PKT
