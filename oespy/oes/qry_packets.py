from ..utils import BaseStructure, BaseUnion
from ..utils.types import *
from ..spk.types import SPK_MAX_PATH_LEN
from .base_constants import (OES_BANK_NO_MAX_LEN, OES_CUST_LONG_NAME_MAX_LEN, OES_CLIENT_NAME_MAX_LEN,
                             OES_CLIENT_DESC_MAX_LEN, OES_SECURITY_ID_MAX_LEN, OES_SECURITY_NAME_MAX_LEN,
                             OES_CUST_NAME_MAX_LEN, OES_BROKER_NAME_MAX_LEN, OES_BROKER_PHONE_MAX_LEN,
                             OES_BROKER_WEBSITE_MAX_LEN, OES_VER_ID_MAX_LEN, OES_MAX_IP_LEN,
                             OES_APPL_UPGRADE_PROTOCOL_MAX_LEN, OES_PWD_MAX_LEN, OES_MAX_COMP_ID_LEN,
                             OES_APPL_DISCARD_VERSION_MAX_COUNT, OES_CLIENT_TAG_MAX_LEN)
from .base_model import (OES_CUST_ID_MAX_LEN, OES_INV_ACCT_ID_MAX_LEN, OES_CASH_ACCT_ID_MAX_LEN)
from .base_model import _OES_CUST_BASE_INFO_PKT, _OES_INV_ACCT_BASE_INFO_PKT, _OES_ETF_COMPONENT_BASE_INFO_PKT
from .base_model import (OesCustBaseInfoT, OesStockBaseInfoT, OesIssueBaseInfoT, OesEtfBaseInfoT, OesCashAssetReportT,
                         OesStkHoldingReportT, OesLotWinningBaseInfoT, OesOrdCnfmT, OesTrdCnfmT, OesFundTrsfReportT,
                         OesMarketStateInfoT, OesNotifyBaseInfoT)


OES_MAX_ORD_ITEM_CNT_PER_PACK = 30
OES_MAX_TRD_ITEM_CNT_PER_PACK = 30
OES_MAX_CASH_ASSET_ITEM_CNT_PER_PACK = 100
OES_MAX_HOLDING_ITEM_CNT_PER_PACK = 100
OES_MAX_CUST_ITEM_CNT_PER_PACK = 30
OES_MAX_INV_ACCT_ITEM_CNT_PER_PACK = 30
OES_MAX_COMMS_RATE_ITEM_CNT_PER_PACK = 50
OES_MAX_FUND_TRSF_ITEM_CNT_PER_PACK = 30
OES_MAX_LOG_WINNING_ITEM_CNT_PER_PACK = 30
OES_MAX_ISSUE_ITEM_CNT_PER_PACK = 30
OES_MAX_STOCK_ITEM_CNT_PER_PACK = 30
OES_MAX_ETF_ITEM_CNT_PER_PACK = 30
OES_MAX_ETF_COMPONENT_ITEM_CNT_PER_PACK = 30
OES_MAX_MKT_STATE_ITEM_CNT_PER_PACK = 30
OES_MAX_NOTIFY_INFO_ITEM_CNT_PER_PACK = 30
OES_MAX_CUST_PER_CLIENT = 1


class OesQryReqHeadT(BaseStructure):
    _fields_ = [
        ('maxPageSize', c_int32),
        ('lastPosition', c_int32),
    ]


class OesQryRspHeadT(BaseStructure):
    _fields_ = [
        ('itemCount', c_int32),
        ('lastPosition', c_int32),
        ('isEnd', c_int8),
        ('__filler', c_uint8 * 7),
        ('userInfo', c_int64),
    ]


class OesQryCursorT(BaseStructure):
    _fields_ = [
        ('seqNo', c_int32),
        ('isEnd', c_int8),
        ('__filler', c_int8 * 3),
        ('userInfo', c_int64),
    ]


class OesQryTradingDayRspT(BaseStructure):
    _fields_ = [
        ('tradingDay', c_int32),
        ('__filler', c_int32),
    ]


class OesInvAcctOverviewT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),

        ('isValid', c_uint8),
        ('mktId', c_uint8),
        ('acctType', c_uint8),
        ('status', c_uint8),
        ('ownerType', c_uint8),
        ('optInvLevel', c_uint8),
        ('isTradeDisabled', c_uint8),
        ('__filler1', c_uint8),

        ('limits', c_uint64),
        ('permissions', c_uint64),

        ('pbuId', c_int32),
        ('subscriptionQuota', c_int32),
        ('kcSubscriptionQuota', c_int32),

        ('riskWarningSecurityBuyQtyLimit', c_int32),

        ('trdOrdCnt', c_int32),
        ('nonTrdOrdCnt', c_int32),
        ('cancelOrdCnt', c_int32),
        ('oesRejectOrdCnt', c_int32),
        ('exchRejectOrdCnt', c_int32),
        ('trdCnt', c_int32),

        ('__reserve', c_char * 64),
    ]


class OesCashAcctOverviewT(BaseStructure):
    _fields_ = [
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('bankId', c_char * OES_BANK_NO_MAX_LEN),

        ('isValid', c_uint8),
        ('cashType', c_uint8),
        ('cashAcctStatus', c_uint8),
        ('currType', c_uint8),
        ('isFundTrsfDisabled', c_uint8),
        ('__filler', c_uint8 * 3),

        ('__reserve', c_char * 64),
    ]


class OesCustOverviewT(BaseStructure):
    _fields_ = _OES_CUST_BASE_INFO_PKT + [
        ('cashAcct', OesCashAcctOverviewT),
        ('sseInvAcct', OesInvAcctOverviewT),
        ('szseInvAcct', OesInvAcctOverviewT),
        ('custName', c_char * OES_CUST_LONG_NAME_MAX_LEN),
        ('__reserve', c_char * 64),
    ]


class OesClientOverviewT(BaseStructure):
    _fields_ = [
        ('clientName', c_char * OES_CLIENT_NAME_MAX_LEN),
        ('clientMemo', c_char * OES_CLIENT_DESC_MAX_LEN),

        ('clientId', c_int16),
        ('clientType', c_uint8),
        ('clientStatus', c_uint8),
        ('isApiForbidden', c_uint8),
        ('isBlockTrader', c_uint8),
        ('businessScope', c_uint8),
        ('currentBusinessType', c_uint8),
        ('logonTime', c_int64),

        ('sseStkPbuId', c_int32),
        ('sseOptPbuId', c_int32),
        ('sseQualificationClass', c_uint8),
        ('__filler2', c_uint8 * 7),

        ('szseStkPbuId', c_int32),
        ('szseOptPbuId', c_int32),
        ('szseQualificationClass', c_uint8),
        ('__filler3', c_uint8 * 7),

        ('currOrdConnected', c_int32),
        ('currRptConnected', c_int32),
        ('currQryConnected', c_int32),
        ('maxOrdConnect', c_int32),
        ('maxRptConnect', c_int32),
        ('maxQryConnect', c_int32),

        ('ordTrafficLimit', c_int32),
        ('qryTrafficLimit', c_int32),
        ('maxOrdCount', c_int32),

        ('initialCashAssetRatio', c_uint8),
        ('isSupportInternalAllot', c_uint8),
        ('isCheckStkConcentrate', c_uint8),
        ('isSupportBankFundTrsf', c_uint8),

        ('__reserve', c_char * 124),

        ('associatedCustCnt', c_int32),
        ('custItems', OesCustOverviewT * OES_MAX_CUST_PER_CLIENT),
    ]


class OesQryCustFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('userInfo', c_int64),
    ]


OesCustItemT = OesCustBaseInfoT


class OesQryCustReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCustFilterT),
    ]


class OesQryCustRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCustItemT * OES_MAX_CUST_ITEM_CNT_PER_PACK),
    ]


class OesQryInvAcctFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('__filler', c_uint8 * 7),
        ('userInfo', c_int64),
    ]


class OesInvAcctItemT(BaseStructure):
    _fields_ = _OES_INV_ACCT_BASE_INFO_PKT + [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
    ]


class OesQryInvAcctReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryInvAcctFilterT),
    ]


class OesQryInvAcctRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesInvAcctItemT * OES_MAX_INV_ACCT_ITEM_CNT_PER_PACK),
    ]


class OesQryStockFilterT(BaseStructure):
    _fields_ = [
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('securityType', c_uint8),
        ('subSecurityType', c_uint8),
        ('crdCollateralFlag', c_int8),
        ('crdMarginTradeUnderlyingFlag', c_int8),
        ('crdShortSellUnderlyingFlag', c_int8),
        ('__filler', c_uint8 * 2),

        ('userInfo', c_int64),
    ]


OesStockItemT = OesStockBaseInfoT


class OesQryStockReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryStockFilterT),
    ]


class OesQryStockRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesStockItemT * OES_MAX_STOCK_ITEM_CNT_PER_PACK),
    ]


class OesQryIssueFilterT(BaseStructure):
    _fields_ = [
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('productType', c_uint8),
        ('__filler', c_uint8 * 6),
        ('userInfo', c_int64),
    ]


OesIssueItemT = OesIssueBaseInfoT


class OesQryIssueReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryIssueFilterT),
    ]


class OesQryIssueRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesIssueItemT * OES_MAX_ISSUE_ITEM_CNT_PER_PACK),
    ]


class OesQryEtfFilterT(BaseStructure):
    _fields_ = [
        ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('__filler', c_uint8 * 7),
        ('userInfo', c_int64),
    ]


OesEtfItemT = OesEtfBaseInfoT


class OesQryEtfReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryEtfFilterT),
    ]


class OesQryEtfRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesEtfItemT * OES_MAX_ETF_ITEM_CNT_PER_PACK),
    ]


class OesQryEtfComponentFilterT(BaseStructure):
    _fields_ = [
        ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('fundMktId', c_uint8),
        ('__filler', c_uint8 * 7),
        ('userInfo', c_int64),
    ]


class OesEtfComponentItemT(BaseStructure):
    _fields_ = _OES_ETF_COMPONENT_BASE_INFO_PKT + [
        ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
        ('__reserve', c_char * 96),
    ]


class OesQryEtfComponentReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryEtfComponentFilterT),
    ]


class OesQryEtfComponentRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesEtfComponentItemT * OES_MAX_ETF_COMPONENT_ITEM_CNT_PER_PACK),
    ]


class OesQryCashAssetFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        ('userInfo', c_int64),
    ]


OesCashAssetItemT = OesCashAssetReportT


class OesQryCashAssetReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCashAssetFilterT),
    ]


class OesQryCashAssetRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCashAssetItemT * OES_MAX_CASH_ASSET_ITEM_CNT_PER_PACK),
    ]


class OesQryColocationPeerCashReqT(BaseStructure):
    _fields_ = [
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ]


class OesQryColocationPeerCashRspT(BaseStructure):
    _fields_ = [
        ('colocationPeerCashItem', OesCashAssetItemT),
    ]


class OesCounterCashItemT(BaseStructure):
    _fields_ = [
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('custName', c_char * OES_CUST_NAME_MAX_LEN),
        ('bankId', c_char * OES_BANK_NO_MAX_LEN),

        ('cashType', c_uint8),
        ('cashAcctStatus', c_uint8),
        ('currType', c_uint8),
        ('isFundTrsfDisabled', c_uint8),
        ('__filler', c_uint8 * 4),

        ('counterAvailableBal', c_int64),
        ('counterDrawableBal', c_int64),
        ('counterCashUpdateTime', c_int64),

        ('__reserve', c_char * 32),
    ]


class OesQryCounterCashReqT(BaseStructure):
    _fields_ = [
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ]


class OesQryCounterCashRspT(BaseStructure):
    _fields_ = [
        ('counterCashItem', OesCounterCashItemT),
    ]


class OesQryStkHoldingFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('securityType', c_uint8),
        ('productType', c_uint8),
        ('subSecurityType', c_uint8),
        ('__filler', c_uint8 * 4),

        ('userInfo', c_int64),
    ]


OesStkHoldingItemT = OesStkHoldingReportT


class OesQryStkHoldingReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryStkHoldingFilterT),
    ]


class OesQryStkHoldingRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesStkHoldingItemT * OES_MAX_HOLDING_ITEM_CNT_PER_PACK),
    ]


class OesQryLotWinningFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),

        ('mktId', c_uint8),

        ('lotType', c_uint8),
        ('__filler', c_uint8 * 6),
        ('startDate', c_int32),
        ('endDate', c_int32),
        ('userInfo', c_int64),
    ]


OesLotWinningItemT = OesLotWinningBaseInfoT


class OesQryLotWinningReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryLotWinningFilterT),
    ]


class OesQryLotWinningRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesLotWinningItemT * OES_MAX_LOG_WINNING_ITEM_CNT_PER_PACK),
    ]


class OesQryOrdFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('isUnclosedOnly', c_uint8),
        ('clEnvId', c_int8),
        ('securityType', c_uint8),
        ('bsType', c_uint8),
        ('subSecurityType', c_uint8),
        ('__filler', c_uint8 * 2),

        ('clOrdId', c_int64),
        ('clSeqNo', c_int64),

        ('startTime', c_int32),
        ('endTime', c_int32),

        ('userInfo', c_int64),
    ]


OesOrdItemT = OesOrdCnfmT


class OesQryOrdReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryOrdFilterT),
    ]


class OesQryOrdRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesOrdItemT * OES_MAX_ORD_ITEM_CNT_PER_PACK),
    ]


class OesQryTrdFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('clEnvId', c_int8),
        ('securityType', c_uint8),
        ('bsType', c_uint8),
        ('subSecurityType', c_uint8),
        ('__filler', c_uint8 * 3),

        ('clOrdId', c_int64),
        ('clSeqNo', c_int64),

        ('startTime', c_int32),
        ('endTime', c_int32),

        ('userInfo', c_int64),
    ]


OesTrdItemT = OesTrdCnfmT


class OesQryTrdReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryTrdFilterT),
    ]


class OesQryTrdRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesTrdItemT * OES_MAX_TRD_ITEM_CNT_PER_PACK),
    ]


class OesQryFundTransferSerialFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        ('clSeqNo', c_int32),
        ('clEnvId', c_int8),
        ('__filler', c_uint8),
        ('userInfo', c_int64),
    ]


OesFundTransferSerialItemT = OesFundTrsfReportT


class OesQryFundTransferSerialReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryFundTransferSerialFilterT),
    ]


class OesQryFundTransferSerialRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesFundTransferSerialItemT * OES_MAX_FUND_TRSF_ITEM_CNT_PER_PACK),
    ]


class OesQryCommissionRateFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('securityType', c_uint8),
        ('bsType', c_uint8),
        ('__filler', c_uint8 * 5),
        ('userInfo', c_int64),
    ]


class OesCommissionRateItemT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('securityType', c_uint8),
        ('subSecurityType', c_uint8),
        ('bsType', c_uint8),

        ('feeType', c_uint8),
        ('currType', c_uint8),
        ('calcFeeMode', c_uint8),
        ('__filler', c_uint8),

        ('feeRate', c_int64),
        ('minFee', c_int32),
        ('maxFee', c_int32),
    ]


class OesQryCommissionRateReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCommissionRateFilterT),
    ]


class OesQryCommissionRateRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCommissionRateItemT * OES_MAX_COMMS_RATE_ITEM_CNT_PER_PACK),
    ]


class OesQryMarketStateFilterT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('platformId', c_uint8),
        ('__filler', c_uint8 * 6),
        ('userInfo', c_int64),
    ]


OesMarketStateItemT = OesMarketStateInfoT


class OesQryMarketStateReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryMarketStateFilterT),
    ]


class OesQryMarketStateRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesMarketStateItemT * OES_MAX_MKT_STATE_ITEM_CNT_PER_PACK),
    ]


class OesQryNotifyInfoFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('notifyLevel', c_uint8),
        ('__filler', c_uint8 * 7),
        ('userInfo', c_int64),
    ]


OesNotifyInfoItemT = OesNotifyBaseInfoT


class OesQryNotifyInfoReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryNotifyInfoFilterT),
    ]


class OesQryNotifyInfoRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesNotifyInfoItemT * OES_MAX_NOTIFY_INFO_ITEM_CNT_PER_PACK),
    ]


class _CreditExt(BaseStructure):
    _fields_ = [
        ('singleMarginBuyCeiling', c_int64),
        ('singleShortSellCeiling', c_int64),

        ('safetyLineRatio', c_int32),
        ('withdrawLineRatio', c_int32),
        ('warningLineRatio', c_int32),
        ('liqudationLineRatio', c_int32),

        ('isRepayInterestOnlyAble', c_uint8),
        ('__filler', c_uint8 * 7),
    ]


class _OptionExt(BaseStructure):
    _fields_ = [
        ('withdrawLineRatio', c_int32),
        ('marginCallLineRatio', c_int32),
        ('liqudationLineRatio', c_int32),
        ('marginDisposalLineRatio', c_int32),
    ]


class _OesBrokerParamsInfoUnion(BaseUnion):
    _fields_ = [
        ('creditExt', _CreditExt),
        ('optionExt', _OptionExt),
        ('__extInfo', c_char * 192),
    ]


class OesBrokerParamsInfoT(BaseStructure):
    _fields_ = [
        ('brokerName', c_char * OES_BROKER_NAME_MAX_LEN),
        ('brokerPhone', c_char * OES_BROKER_PHONE_MAX_LEN),
        ('brokerWebsite', c_char * OES_BROKER_WEBSITE_MAX_LEN),

        ('apiVersion', c_char * OES_VER_ID_MAX_LEN),
        ('__filler1', c_char * 8),
        ('apiMinVersion', c_char * OES_VER_ID_MAX_LEN),
        ('__filler2', c_char * 8),
        ('clientVersion', c_char * OES_VER_ID_MAX_LEN),
        ('__filler3', c_char * 8),

        ('forbidChangePwdEndTime', c_int32),
        ('minClientPasswordLen', c_int32),
        ('clientPasswordStrength', c_int32),

        ('businessScope', c_uint32),
        ('currentBusinessType', c_uint8),
        ('isSupportInternalAllot', c_uint8),
        ('isSupportBankFundTrsf', c_uint8),
        ('__filler4', c_uint8),

        ('forbidChangePwdBeginTime', c_int32),

        ('custId', c_char * OES_CUST_ID_MAX_LEN),

        ('sseRiskWarningSecurityBuyQtyLimit', c_int64),
        ('szseRiskWarningSecurityBuyQtyLimit', c_int64),
        ('__reserve', c_char * 7),

        ('union', _OesBrokerParamsInfoUnion),
    ]


class OesQryBrokerParamsInfoRspT(BaseStructure):
    _fields_ = [
        ('brokerParams', OesBrokerParamsInfoT),
    ]


class OesApplUpgradeSourceT(BaseStructure):
    _fields_ = [
        ('ipAddress', c_char * OES_MAX_IP_LEN),
        ('protocol', c_char * OES_APPL_UPGRADE_PROTOCOL_MAX_LEN),
        ('username', c_char * OES_CLIENT_NAME_MAX_LEN),
        ('password', c_char * OES_PWD_MAX_LEN),
        ('encryptMethod', c_int32),
        ('__filler', c_int32),

        ('homePath', c_char * SPK_MAX_PATH_LEN),
        ('fileName', c_char * SPK_MAX_PATH_LEN),
    ]


class OesApplUpgradeItemT(BaseStructure):
    _fields_ = [
        ('applName', c_char * OES_MAX_COMP_ID_LEN),
        ('minApplVerId', c_char * OES_VER_ID_MAX_LEN),
        ('maxApplVerId', c_char * OES_VER_ID_MAX_LEN),
        ('discardApplVerId', c_char * OES_APPL_DISCARD_VERSION_MAX_COUNT * OES_VER_ID_MAX_LEN),

        ('discardVerCount', c_int32),

        ('newApplVerDate', c_int32),
        ('newApplVerId', c_char * OES_VER_ID_MAX_LEN),
        ('newApplVerTag', c_char * OES_CLIENT_TAG_MAX_LEN),

        ('primarySource', OesApplUpgradeSourceT),

        ('secondarySource', OesApplUpgradeSourceT),
    ]


class OesApplUpgradeInfoT(BaseStructure):
    _fields_ = [
        ('clientUpgradeInfo', OesApplUpgradeItemT),
        ('cApiUpgradeInfo', OesApplUpgradeItemT),
        ('javaApiUpgradeInfo', OesApplUpgradeItemT),
    ]


class OesQryApplUpgradeInfoRspT(BaseStructure):
    _fields_ = [
        ('applUpgradeInfo', OesApplUpgradeInfoT),
    ]
