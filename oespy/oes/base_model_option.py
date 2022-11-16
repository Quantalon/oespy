from ..utils import BaseStructure, BaseUnion
from ..utils.types import *
from .base_constants import (OES_SECURITY_ID_MAX_LEN, OES_CONTRACT_EXCH_ID_MAX_LEN, OES_CONTRACT_SYMBOL_MAX_LEN,
                             OES_SECURITY_STATUS_FLAG_MAX_LEN, OES_INV_ACCT_ID_MAX_LEN, OES_SECURITY_NAME_MAX_LEN,
                             OES_CUST_ID_MAX_LEN)


_OES_OPTION_BASE_INFO_PKT = [
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),

    ('productType', c_uint8),
    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),
    ('contractType', c_uint8),
    ('exerciseType', c_uint8),
    ('deliveryType', c_uint8),
    ('isDayTrading', c_uint8),

    ('limitOpenFlag', c_uint8),
    ('suspFlag', c_uint8),
    ('temporarySuspFlag', c_uint8),
    ('__OPTION_BASE_filler1', c_uint8 * 5),

    ('contractUnit', c_int32),
    ('exercisePrice', c_int32),
    ('deliveryDate', c_int32),
    ('deliveryMonth', c_int32),

    ('listDate', c_int32),
    ('lastTradeDay', c_int32),
    ('exerciseBeginDate', c_int32),
    ('exerciseEndDate', c_int32),

    ('contractPosition', c_int64),
    ('prevClosePrice', c_int32),
    ('prevSettlPrice', c_int32),
    ('underlyingClosePrice', c_int32),

    ('priceTick', c_int32),
    ('upperLimitPrice', c_int32),
    ('lowerLimitPrice', c_int32),

    ('buyQtyUnit', c_int32),
    ('lmtBuyMaxQty', c_int32),
    ('lmtBuyMinQty', c_int32),
    ('mktBuyMaxQty', c_int32),
    ('mktBuyMinQty', c_int32),

    ('sellQtyUnit', c_int32),
    ('lmtSellMaxQty', c_int32),
    ('lmtSellMinQty', c_int32),
    ('mktSellMaxQty', c_int32),
    ('mktSellMinQty', c_int32),

    ('sellMargin', c_int64),
    ('originalSellMargin', c_int64),
    ('marginRatioParam1', c_int32),
    ('marginRatioParam2', c_int32),
    ('increasedMarginRatio', c_int32),
    ('expireDays', c_int32),

    ('contractId', c_char * OES_CONTRACT_EXCH_ID_MAX_LEN),
    ('securityName', c_char * OES_CONTRACT_SYMBOL_MAX_LEN),

    ('securityStatusFlag', c_char * OES_SECURITY_STATUS_FLAG_MAX_LEN),

    ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('underlyingMktId', c_uint8),
    ('underlyingSecurityType', c_uint8),
    ('__OPTION_BASE_filler3', c_uint8 * 6),
]


class OesOptionBaseInfoT(BaseStructure):
    _fields_ = _OES_OPTION_BASE_INFO_PKT


_OES_OPT_HOLDING_BASE_INFO_PKT = [
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),
    ('positionType', c_uint8),

    ('productType', c_uint8),
    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),
    ('contractType', c_uint8),
    ('hedgeFlag', c_uint8),
    ('__HOLD_BASE_filler', c_uint8),

    ('originalQty', c_int64),
    ('originalAvlQty', c_int64),
    ('originalCostAmt', c_int64),
    ('originalCarryingAmt', c_int64),

    ('totalOpenQty', c_int64),
    ('uncomeQty', c_int64),
    ('totalCloseQty', c_int64),
    ('closeFrzQty', c_int64),

    ('manualFrzQty', c_int64),

    ('totalInPremium', c_int64),
    ('totalOutPremium', c_int64),
    ('totalOpenFee', c_int64),
    ('totalCloseFee', c_int64),

    ('exerciseFrzQty', c_int64),
    ('positionMargin', c_int64),

    ('__OPT_HOLDING_BASE_reserve', c_char * 32),
]


_OES_OPT_HOLDING_RPT_INFO_PKT = [
    ('closeAvlQty', c_int64),
    ('exerciseAvlQty', c_int64),
    ('sumQty', c_int64),
    ('costPrice', c_int64),
    ('carryingAvgPrice', c_int64),
    ('coveredAvlUnderlyingQty', c_int64),

    ('availableLongPositionLimit', c_int32),
    ('availableTotalPositionLimit', c_int32),
    ('availableDailyBuyOpenLimit', c_int32),
    ('__OPT_HOLDING_EXT_filler2', c_int32),
    ('__OPT_HOLDING_EXT_reserve', c_char * 32),
]


class OesOptHoldingBaseInfoT(BaseStructure):
    _fields_ = _OES_OPT_HOLDING_BASE_INFO_PKT


class OesOptHoldingReportT(BaseStructure):
    _fields_ = _OES_OPT_HOLDING_BASE_INFO_PKT + _OES_OPT_HOLDING_RPT_INFO_PKT


_OES_OPT_UNDERLYING_HOLDING_BASE_PKT = [
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),

    ('mktId', c_uint8),
    ('underlyingMktId', c_uint8),
    ('underlyingSecurityType', c_uint8),
    ('underlyingSubSecurityType', c_uint8),
    ('__OPT_UNDERLYING_HOLD_BASE_filler', c_uint8 * 4),

    ('originalHld', c_int64),
    ('originalAvlHld', c_int64),
    ('originalCoveredQty', c_int64),
    ('initialCoveredQty', c_int64),

    ('coveredQty', c_int64),
    ('coveredGapQty', c_int64),
    ('coveredAvlQty', c_int64),
    ('lockAvlQty', c_int64),

    ('sumHld', c_int64),

    ('maxReduceQuota', c_int64),
]


class OesOptUnderlyingHoldingBaseInfoT(BaseStructure):
    _fields_ = _OES_OPT_UNDERLYING_HOLDING_BASE_PKT


class OesOptUnderlyingHoldingReportT(BaseStructure):
    _fields_ = _OES_OPT_UNDERLYING_HOLDING_BASE_PKT


_OES_OPTION_POSITION_LIMIT_BASE_PKT = [
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),

    ('underlyingMktId', c_uint8),
    ('underlyingSecurityType', c_uint8),
    ('underlyingSubSecurityType', c_uint8),
    ('__POSITION_LIMIT_BASE_filler1', c_uint8 * 4),

    ('longPositionLimit', c_int32),
    ('totalPositionLimit', c_int32),
    ('dailyBuyOpenLimit', c_int32),
    ('__POSITION_LIMIT_BASE_filler2', c_int32),

    ('originalLongQty', c_int32),
    ('totalBuyOpenQty', c_int32),
    ('uncomeBuyOpenQty', c_int32),
    ('totalSellCloseQty', c_int32),

    ('originalShortQty', c_int32),
    ('totalSellOpenQty', c_int32),
    ('uncomeSellOpenQty', c_int32),
    ('totalBuyCloseQty', c_int32),

    ('originalCoveredQty', c_int32),
    ('totalCoveredOpenQty', c_int32),
    ('uncomeCoveredOpenQty', c_int32),
    ('totalCoveredCloseQty', c_int32),
]


class OesOptionPositionLimitBaseInfoT(BaseStructure):
    _fields_ = _OES_OPTION_POSITION_LIMIT_BASE_PKT


_OES_OPTION_EXERCISE_ASSIGN_BASE_PKT = [
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),
    ('positionType', c_uint8),

    ('productType', c_uint8),
    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),
    ('contractType', c_uint8),
    ('deliveryType', c_uint8),
    ('__OPTION_EXERCISE_ASSIGN_filler1', c_uint8),

    ('exercisePrice', c_int32),
    ('exerciseQty', c_int32),
    ('deliveryQty', c_int64),

    ('exerciseBeginDate', c_int32),
    ('exerciseEndDate', c_int32),
    ('clearingDate', c_int32),
    ('deliveryDate', c_int32),

    ('clearingAmt', c_int64),
    ('clearingFee', c_int64),
    ('settlementAmt', c_int64),

    ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('underlyingMktId', c_uint8),
    ('underlyingSecurityType', c_uint8),
    ('__OPTION_EXERCISE_ASSIGN_filler3', c_uint8 * 6),
    ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
    ('__OPTION_EXERCISE_ASSIGN_reserve', c_char * 16),
]


class OesOptionExerciseAssignBaseT(BaseStructure):
    _fields_ = _OES_OPTION_EXERCISE_ASSIGN_BASE_PKT


class _UserInfo(BaseUnion):
    _fields_ = [
        ('u64', c_uint64),
        ('i64', c_int64),
        ('u32', c_uint32 * 2),
        ('i32', c_int32 * 2),
        ('c8', c_char * 8),
    ]


_OES_OPT_SETTLEMENT_CONFIRM_BASE_PKT = [
    ('custId', c_char * OES_CUST_ID_MAX_LEN),
    ('userInfo', _UserInfo),
    ('clientId', c_int16),
    ('clEnvId', c_int8),
    ('__filler2', c_int8),
    ('transDate', c_int32),
    ('transTime', c_int32),
    ('rejReason', c_int32),
    ('__OPT_SETTLEMENT_CONFIRM_BASE_reserve', c_char * 24),
]


class OesOptSettlementConfirmBaseInfoT(BaseStructure):
    _fields_ = _OES_OPT_SETTLEMENT_CONFIRM_BASE_PKT


class OesOptSettlementConfirmReportT(BaseStructure):
    _fields_ = _OES_OPT_SETTLEMENT_CONFIRM_BASE_PKT
