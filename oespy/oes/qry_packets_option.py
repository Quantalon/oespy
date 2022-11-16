from ..utils import BaseStructure, BaseUnion
from ..utils.types import *
from .base_constants import (OES_CUST_ID_MAX_LEN, OES_INV_ACCT_ID_MAX_LEN, OES_SECURITY_ID_MAX_LEN,
                             OES_CONTRACT_EXCH_ID_MAX_LEN, OES_SECURITY_NAME_MAX_LEN, OES_CASH_ACCT_ID_MAX_LEN,
                             )
from .base_model_option import OesOptionBaseInfoT, OesOptUnderlyingHoldingBaseInfoT, OesOptionExerciseAssignBaseT
from .base_model_option import _OES_OPT_HOLDING_BASE_INFO_PKT, _OES_OPT_HOLDING_RPT_INFO_PKT
from .qry_packets import OesQryReqHeadT, OesQryRspHeadT


OES_MAX_OPT_HOLDING_ITEM_CNT_PER_PACK = 30
OES_MAX_OPT_OPTION_ITEM_CNT_PER_PACK = 30
OES_MAX_OPT_UNDERLYING_ITEM_CNT_PER_PACK = 30
OES_MAX_OPT_PURCHASE_LIMIT_ITEM_CNT_PER_PACK = 30
OES_MAX_OPT_EXERCISE_ASSIGN_ITEM_CNT_PER_PACK = 30


class OesQryOptionFilterT(BaseStructure):
    _fields_ = [
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('__filler', c_uint8 * 7),
        ('userInfo', c_int64),
    ]


OesOptionItemT = OesOptionBaseInfoT


class OesQryOptionReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryOptionFilterT),
    ]


class OesQryOptionRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesOptionItemT * OES_MAX_OPT_OPTION_ITEM_CNT_PER_PACK),
    ]


class OesQryOptHoldingFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('positionType', c_uint8),
        ('__filler', c_uint8 * 6),

        ('userInfo', c_int64),
    ]


class OesOptHoldingItemT(BaseStructure):
    _fields_ = _OES_OPT_HOLDING_BASE_INFO_PKT + _OES_OPT_HOLDING_RPT_INFO_PKT + [
        ('contractId', c_char * OES_CONTRACT_EXCH_ID_MAX_LEN),
        ('contractSymbol', c_char * OES_SECURITY_NAME_MAX_LEN),
        ('prevSettlPrice', c_int64),
    ]


class OesQryOptHoldingReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryOptHoldingFilterT),
    ]


class OesQryOptHoldingRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesOptHoldingItemT * OES_MAX_OPT_HOLDING_ITEM_CNT_PER_PACK),
    ]


class OesQryOptUnderlyingHoldingFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('underlyingSecurityType', c_uint8),
        ('__filler', c_uint8 * 6),

        ('userInfo', c_int64),
    ]


OesOptUnderlyingHoldingItemT = OesOptUnderlyingHoldingBaseInfoT


class OesQryOptUnderlyingHoldingReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryOptUnderlyingHoldingFilterT),
    ]


class OesQryOptUnderlyingHoldingRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesOptUnderlyingHoldingItemT * OES_MAX_OPT_HOLDING_ITEM_CNT_PER_PACK),
    ]


class OesQryOptPositionLimitFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('underlyingSecurityType', c_uint8),
        ('__filler', c_uint8 * 6),

        ('userInfo', c_int64),
    ]


class OesOptPositionLimitItemT(BaseStructure):
    _fields_ = [
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),

        ('underlyingMktId', c_uint8),
        ('underlyingSecurityType', c_uint8),
        ('underlyingSubSecurityType', c_uint8),
        ('__filler1', c_uint8 * 4),

        ('longPositionLimit', c_int32),
        ('totalPositionLimit', c_int32),
        ('dailyBuyOpenLimit', c_int32),
        ('__filler2', c_int32),

        ('originalLongQty', c_int32),
        ('originalShortQty', c_int32),
        ('originalCoveredQty', c_int32),

        ('availableLongPositionLimit', c_int32),
        ('availableTotalPositionLimit', c_int32),
        ('availableDailyBuyOpenLimit', c_int32),

        ('__reserve', c_char * 8),
    ]


class OesQryOptPositionLimitReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryOptPositionLimitFilterT),
    ]


class OesQryOptPositionLimitRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesOptPositionLimitItemT * OES_MAX_OPT_UNDERLYING_ITEM_CNT_PER_PACK),
    ]


class OesQryOptPurchaseLimitFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('__filler', c_uint8 * 7),
        ('userInfo', c_int64),
    ]


class OesOptPurchaseLimitItemT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('custType', c_uint8),
        ('__filler', c_uint8 * 6),

        ('purchaseLimit', c_int64),
        ('originalUsedPurchaseAmt', c_int64),
        ('totalOpenPurchaseAmt', c_int64),
        ('frzPurchaseAmt', c_int64),
        ('totalClosePurchaseAmt', c_int64),
        ('availablePurchaseLimit', c_int64),
    ]


class OesQryOptPurchaseLimitReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryOptPurchaseLimitFilterT),
    ]


class OesQryOptPurchaseLimitRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesOptPurchaseLimitItemT * OES_MAX_OPT_PURCHASE_LIMIT_ITEM_CNT_PER_PACK),
    ]


class OesQryOptExerciseAssignFilterT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

        ('mktId', c_uint8),
        ('positionType', c_uint8),
        ('__filler', c_uint8 * 6),

        ('userInfo', c_int64),
    ]


OesOptExerciseAssignItemT = OesOptionExerciseAssignBaseT


class OesQryOptExerciseAssignReqT(BaseStructure):
    _fields_ = [
        ('reqHead', OesQryReqHeadT),
        ('qryFilter', OesQryOptExerciseAssignFilterT),
    ]


class OesQryOptExerciseAssignRspT(BaseStructure):
    _fields_ = [
        ('rspHead', OesQryRspHeadT),
        ('qryItems', OesOptExerciseAssignItemT * OES_MAX_OPT_EXERCISE_ASSIGN_ITEM_CNT_PER_PACK),
    ]
