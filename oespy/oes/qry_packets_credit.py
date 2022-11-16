from ..utils import BaseStructure
from ..utils.types import *
from .base_constants import (OES_CUST_ID_MAX_LEN, OES_CASH_ACCT_ID_MAX_LEN, OES_SECURITY_ID_MAX_LEN,
                             OES_INV_ACCT_ID_MAX_LEN, OES_CREDIT_DEBT_ID_MAX_LEN)
from .base_model import OesCrdCashRepayReportT
from .base_model_credit import (OesCrdCreditAssetBaseInfoT, OesCrdUnderlyingBaseInfoT, OesCrdDebtContractReportT,
                                OesCrdDebtJournalBaseInfoT, OesCrdSecurityDebtStatsBaseInfoT, OesCrdExcessStockBaseInfoT,
                                )
from .base_model_credit import _OES_CRD_CASH_POSITION_BASE_INFO_PKT, _OES_CRD_SECURITY_POSITION_BASE_INFO_PKT
from .qry_packets import OesQryReqHeadT, OesQryRspHeadT, OesCommissionRateItemT


OES_MAX_CRD_DEBT_CONTRACT_ITEM_CNT_PER_PACK = 100
OES_MAX_CRD_DEBT_JOURNAL_ITEM_CNT_PER_PACK = 100
OES_MAX_CRD_CREDIT_ASSET_ITEM_CNT_PER_PACK = 100
OES_MAX_CRD_SECURITY_DEBT_STATS_ITEM_CNT_PER_PACK = 100
OES_MAX_CRD_CASH_REPAY_ITEM_CNT_PER_PACK = 100
OES_MAX_CRD_CASH_POSITION_ITEM_CNT_PER_PACK = 100
OES_MAX_CRD_SECURITY_POSITION_ITEM_CNT_PER_PACK = 100
OES_MAX_CRD_EXCESS_STOCK_ITEM_CNT_PER_PACK = 100
OES_MAX_CRD_INTEREST_RATE_ITEM_CNT_PER_PACK = 100
OES_MAX_CRD_UNDERLYING_INFO_ITEM_CNT_PER_PACK = 500


class OesQryCrdCreditAssetFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        ('userInfo', c_int64),
    ]


OesCrdCreditAssetItemT = OesCrdCreditAssetBaseInfoT


class OesQryCrdCreditAssetReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdCreditAssetFilterT),
    ]


class OesQryCrdCreditAssetRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdCreditAssetItemT * OES_MAX_CRD_CREDIT_ASSET_ITEM_CNT_PER_PACK),
    ]


class OesQryCrdUnderlyingInfoFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('crdMarginTradeUnderlyingFlag', c_uint8),
        ('crdShortSellUnderlyingFlag', c_uint8),
        ('__filler', c_uint8 * 5),

        ('userInfo', c_int64),
    ]


OesCrdUnderlyingInfoItemT = OesCrdUnderlyingBaseInfoT


class OesQryCrdUnderlyingInfoReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdUnderlyingInfoFilterT),
    ]


class OesQryCrdUnderlyingInfoRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdUnderlyingInfoItemT * OES_MAX_CRD_UNDERLYING_INFO_ITEM_CNT_PER_PACK),
    ]


class OesQryCrdCashPositionFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        ('cashGroupProperty', c_uint8),
        ('__filler', c_uint8 * 7),
        ('userInfo', c_int64),
    ]


class OesCrdCashPositionItemT(BaseStructure):
    _fields_ = _OES_CRD_CASH_POSITION_BASE_INFO_PKT + [
        ('availableBalance', c_int64),
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('__reserve', c_char * 16),
    ]


class OesQryCrdCashPositionReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdCashPositionFilterT),
    ]


class OesQryCrdCashPositionRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdCashPositionItemT * OES_MAX_CRD_CASH_POSITION_ITEM_CNT_PER_PACK),
    ]


class OesQryCrdSecurityPositionFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('cashGroupProperty', c_uint8),
        ('__filler', c_uint8 * 6),

        ('userInfo', c_int64),
    ]


class OesCrdSecurityPositionItemT(BaseStructure):
    _fields_ = _OES_CRD_SECURITY_POSITION_BASE_INFO_PKT + [
        ('availablePositionQty', c_int64),
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('__reserve', c_char * 32),
    ]


class OesQryCrdSecurityPositionReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdSecurityPositionFilterT),
    ]


class OesQryCrdSecurityPositionRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdSecurityPositionItemT * OES_MAX_CRD_SECURITY_POSITION_ITEM_CNT_PER_PACK)
    ]


class OesQryCrdDebtContractFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),

        ('mktId', c_uint8),

        ('isUnclosedOnly', c_uint8),
        ('debtType', c_uint8),
        ('historyContractFlag', c_uint8),
        ('__filler', c_uint8 * 4),

        ('startDate', c_int32),
        ('endDate', c_int32),

        ('userInfo', c_int64),
    ]


OesCrdDebtContractItemT = OesCrdDebtContractReportT


class OesQryCrdDebtContractReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdDebtContractFilterT),
    ]


class OesQryCrdDebtContractRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdDebtContractItemT * OES_MAX_CRD_DEBT_CONTRACT_ITEM_CNT_PER_PACK),
    ]


class OesQryCrdDebtJournalFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('debtType', c_uint8),
        ('__filler', c_uint8 * 6),

        ('startDate', c_int32),
        ('endDate', c_int32),

        ('userInfo', c_int64),
    ]


OesCrdDebtJournalItemT = OesCrdDebtJournalBaseInfoT


class OesQryCrdDebtJournalReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdDebtJournalFilterT),
    ]


class OesQryCrdDebtJournalRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdDebtJournalItemT * OES_MAX_CRD_DEBT_JOURNAL_ITEM_CNT_PER_PACK),
    ]


class OesQryCrdCashRepayFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),

        ('clSeqNo', c_int32),
        ('clEnvId', c_int8),
        ('__filler', c_uint8 * 3),

        ('userInfo', c_int64),
    ]


OesCrdCashRepayItemT = OesCrdCashRepayReportT


class OesQryCrdCashRepayReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdCashRepayFilterT),
    ]


class OesQryCrdCashRepayRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdCashRepayItemT * OES_MAX_CRD_CASH_REPAY_ITEM_CNT_PER_PACK),
    ]


class OesQryCrdSecurityDebtStatsFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('hasCreditDebtFlag', c_uint8),
        ('__filler', c_uint8 * 6),

        ('userInfo', c_int64),
    ]


OesCrdSecurityDebtStatsItemT = OesCrdSecurityDebtStatsBaseInfoT


class OesQryCrdSecurityDebtStatsReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdSecurityDebtStatsFilterT),
    ]


class OesQryCrdSecurityDebtStatsRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdSecurityDebtStatsItemT * OES_MAX_CRD_SECURITY_DEBT_STATS_ITEM_CNT_PER_PACK),
    ]


class OesQryCrdExcessStockFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('__filler', c_uint8 * 7),

        ('userInfo', c_int64),
    ]


OesCrdExcessStockItemT = OesCrdExcessStockBaseInfoT


class OesQryCrdExcessStockReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdExcessStockFilterT),
    ]


class OesQryCrdExcessStockRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdExcessStockItemT * OES_MAX_CRD_EXCESS_STOCK_ITEM_CNT_PER_PACK),
    ]


class OesQryCrdInterestRateFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('bsType', c_uint8),
        ('__filler', c_uint8 * 6),

        ('userInfo', c_int64),
    ]


OesCrdInterestRateItemT = OesCommissionRateItemT


class OesQryCrdInterestRateReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryCrdInterestRateFilterT),
    ]


class OesQryCrdInterestRateRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesCrdInterestRateItemT * OES_MAX_CRD_INTEREST_RATE_ITEM_CNT_PER_PACK),
    ]


class OesCrdDrawableBalanceItemT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),

        ('drawableBal', c_int64),
    ]


class OesQryCrdDrawableBalanceReqT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ]


class OesQryCrdDrawableBalanceRspT(BaseStructure):
    _fields_ = [
        ('drawableBalanceItem', OesCrdDrawableBalanceItemT),
    ]


class OesCrdCollateralTransferOutMaxQtyItemT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('__filler', c_uint8 * 7),
        ('collateralTransferOutMaxQty', ),
    ]


class OesQryCrdCollateralTransferOutMaxQtyReqT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('__filler', c_uint8 * 7),
    ]


class OesQryCrdCollateralTransferOutMaxQtyRspT(BaseStructure):
    _fields_ = [
        ('collateralTransferOutMaxQtyItem', OesCrdCollateralTransferOutMaxQtyItemT)
    ]
