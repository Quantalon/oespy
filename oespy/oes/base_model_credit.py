from ..utils import BaseStructure
from ..utils.types import *
from .base_constants import (OES_CUST_ID_MAX_LEN, OES_SECURITY_ID_MAX_LEN, OES_CASH_ACCT_ID_MAX_LEN,
                             OES_INV_ACCT_ID_MAX_LEN, OES_CREDIT_DEBT_ID_MAX_LEN)


class OesCrdCreditAssetBaseInfoT(BaseStructure):
    _fields_ = [
        ('cashAcctId', c_char),
        ('custId', c_char),
        ('currType', c_uint8),
        ('cashType', c_uint8),
        ('cashAcctStatus', c_uint8),
        ('__filler1', c_uint8 * 5),

        ('totalAssetValue', c_int64),

        ('totalDebtValue', c_int64),
        ('maintenaceRatio', c_int32),
        ('__filler2', c_int32),
        ('marginAvailableBal', c_int64),

        ('cashBalance', c_int64),
        ('availableBal', c_int64),
        ('drawableBal', c_int64),
        ('buyCollateralAvailableBal', c_int64),
        ('repayStockAvailableBal', c_int64),
        ('shortSellGainedAmt', c_int64),
        ('shortSellGainedAvailableAmt', c_int64),
        ('totalRepaidAmt', c_int64),
        ('repayFrzAmt', c_int64),

        ('marginBuyMaxQuota', c_int64),
        ('shortSellMaxQuota', c_int64),
        ('creditTotalMaxQuota', c_int64),

        ('marginBuyUsedQuota', c_int64),
        ('marginBuyAvailableQuota', c_int64),

        ('shortSellUsedQuota', c_int64),
        ('shortSellAvailableQuota', c_int64),

        ('specialCashPositionAmt', c_int64),
        ('specialCashPositionAvailableBal', c_int64),
        ('publicCashPositionAmt', c_int64),
        ('publicCashPositionAvailableBal', c_int64),

        ('collateralHoldingMarketCap', c_int64),
        ('collateralUncomeSellMarketCap', c_int64),
        ('collateralTrsfOutMarketCap', c_int64),
        ('collateralRepayDirectMarketCap', c_int64),

        ('marginBuyDebtAmt', c_int64),
        ('marginBuyDebtFee', c_int64),
        ('marginBuyDebtInterest', c_int64),
        ('marginBuyUncomeAmt', c_int64),
        ('marginBuyUncomeFee', c_int64),
        ('marginBuyUncomeInterest', c_int64),
        ('marginBuyDebtMarketCap', c_int64),
        ('marginBuyDebtUsedMargin', c_int64),

        ('shortSellDebtAmt', c_int64),
        ('shortSellDebtFee', c_int64),
        ('shortSellDebtInterest', c_int64),
        ('shortSellUncomeAmt', c_int64),
        ('shortSellUncomeFee', c_int64),
        ('shortSellUncomeInterest', c_int64),
        ('shortSellDebtMarketCap', c_int64),
        ('shortSellDebtUsedMargin', c_int64),

        ('otherDebtAmt', c_int64),
        ('otherDebtInterest', c_int64),
        ('otherCreditFee', c_int64),
        ('creditTotalSpecialFee', c_int64),
        ('marginBuySpecialFee', c_int64),
        ('shortSellSpecialFee', c_int64),
        ('otherBackedAssetValue', c_int64),

        ('trsfOutAbleAssetValue', c_int64),

        ('underlyingMarketCap', c_int64),
        ('correctAssetValue', c_int64),

        ('__reserve', c_char * 8),
    ]


class OesCrdUnderlyingBaseInfoT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('productType', c_uint8),
        ('securityType', c_uint8),
        ('subSecurityType', c_uint8),

        ('isCrdCollateral', c_uint8),
        ('isCrdMarginTradeUnderlying', c_uint8),
        ('isCrdShortSellUnderlying', c_uint8),
        ('isCrdCollateralTradable', c_uint8),
        ('isIndividualCollateral', c_uint8),
        ('isIndividualUnderlying', c_uint8),
        ('__filler1', c_uint8 * 6),

        ('collateralRatio', c_int32),
        ('marginBuyRatio', c_int32),
        ('shortSellRatio', c_int32),
        ('__filler2', c_int32 * 3),
    ]


_OES_CRD_CASH_POSITION_BASE_INFO_PKT = [
    ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ('cashGroupNo', c_int32),
    ('cashGroupProperty', c_uint8),
    ('currType', c_uint8),
    ('__CRD_CASH_POSITION_BASE_filler', c_uint8 * 2),

    ('positionAmt', c_int64),
    ('repaidPositionAmt', c_int64),
    ('usedPositionAmt', c_int64),
    ('frzPositionAmt', c_int64),

    ('originalBalance', c_int64),
    ('originalAvailable', c_int64),
    ('originalUsed', c_int64),

    ('__CRD_CASH_POSITION_BASE_reserve', c_char * 32),
]


class OesCrdCashPositionBaseInfoT(BaseStructure):
    _fields_ = _OES_CRD_CASH_POSITION_BASE_INFO_PKT


_OES_CRD_SECURITY_POSITION_BASE_INFO_PKT = [
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
    ('mktId', c_uint8),
    ('cashGroupProperty', c_uint8),
    ('__SECURITY_POSITION_BASE_filler', c_uint8 * 2),
    ('cashGroupNo', c_int32),

    ('positionQty', c_int64),
    ('repaidPositionQty', c_int64),
    ('usedPositionQty', c_int64),
    ('frzPositionQty', c_int64),

    ('originalBalanceQty', c_int64),
    ('originalAvailableQty', c_int64),
    ('originalUsedQty', c_int64),

    ('__SECURITY_POSITION_BASE_reserve', c_char * 32),
]


class OesCrdSecurityPositionBaseInfoT(BaseStructure):
    _fields_ = _OES_CRD_SECURITY_POSITION_BASE_INFO_PKT


_OES_CRD_DEBT_CONTRACT_BASE_INFO_PKT = [
    ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
    ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

    ('mktId', c_uint8),
    ('securityType', c_uint8),
    ('subSecurityType', c_uint8),
    ('securityProductType', c_uint8),

    ('debtType', c_uint8),
    ('debtStatus', c_uint8),
    ('originalDebtStatus', c_uint8),
    ('debtRepayMode', c_uint8),

    ('ordDate', c_int32),
    ('ordPrice', c_int32),
    ('ordQty', c_int32),
    ('trdQty', c_int32),

    ('ordAmt', c_int64),
    ('trdAmt', c_int64),
    ('trdFee', c_int64),

    ('currentDebtAmt', c_int64),
    ('currentDebtFee', c_int64),
    ('currentDebtInterest', c_int64),
    ('currentDebtQty', c_int32),

    ('uncomeDebtQty', c_int32),
    ('uncomeDebtAmt', c_int64),
    ('uncomeDebtFee', c_int64),
    ('uncomeDebtInterest', c_int64),

    ('totalRepaidAmt', c_int64),
    ('totalRepaidFee', c_int64),
    ('totalRepaidInterest', c_int64),

    ('totalRepaidQty', c_int32),
    ('__CRD_DEBT_CONTRACT_BASE_filler2', c_int32),

    ('originalDebtAmt', c_int64),
    ('originalDebtFee', c_int64),
    ('originalDebtInterest', c_int64),
    ('originalDebtQty', c_int32),

    ('originalRepaidQty', c_int32),

    ('originalRepaidAmt', c_int64),
    ('originalRepaidInterest', c_int64),

    ('punishInterest', c_int64),

    ('marginRatio', c_int32),
    ('interestRate', c_int32),
    ('repayEndDate', c_int32),
    ('cashGroupNo', c_int32),
    ('postponeTimes', c_int32),
    ('postponeStatus', c_uint8),
    ('__CRD_DEBT_CONTRACT_BASE_filler3', c_uint8 * 3),
    ('__CREDIT_DEBT_BASE_reserve', c_char * 32),
]


class OesCrdDebtContractBaseInfoT(BaseStructure):
    _fields_ = _OES_CRD_DEBT_CONTRACT_BASE_INFO_PKT


class OesCrdDebtContractReportT(BaseStructure):
    _fields_ = _OES_CRD_DEBT_CONTRACT_BASE_INFO_PKT + [
        ('securityRepayableDebtQty', c_int64),
        ('contractRepayableDebtQty', c_int32),
        ('__filler', c_int32),
        ('__reserve', c_char * 32),
    ]


_OES_CRD_DEBT_JOURNAL_BASE_INFO_PKT = [
    ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
    ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
    ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),

    ('mktId', c_uint8),
    ('debtType', c_uint8),
    ('journalType', c_uint8),
    ('mandatoryFlag', c_uint8),
    ('seqNo', c_int32),

    ('occurAmt', c_int64),
    ('occurFee', c_int64),
    ('occurInterest', c_int64),
    ('occurQty', c_int32),
    ('postQty', c_int32),
    ('postAmt', c_int64),
    ('postFee', c_int64),
    ('postInterest', c_int64),

    ('shortSellTheoryOccurAmt', c_int64),
    ('useShortSellGainedAmt', c_int64),

    ('ordDate', c_int32),
    ('ordTime', c_int32),
    ('__CRD_DEBT_JOURNAL_BASE_reserve', c_char * 32),
]


class OesCrdDebtJournalBaseInfoT(BaseStructure):
    _fields_ = _OES_CRD_DEBT_JOURNAL_BASE_INFO_PKT


class OesCrdDebtJournalReportT(BaseStructure):
    _fields_ = _OES_CRD_DEBT_JOURNAL_BASE_INFO_PKT


class OesCrdSecurityDebtStatsBaseInfoT(BaseStructure):
    _fields_ = [
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('productType', c_uint8),
        ('securityType', c_uint8),
        ('subSecurityType', c_uint8),

        ('isCrdCollateral', c_uint8),
        ('isCrdMarginTradeUnderlying', c_uint8),
        ('isCrdShortSellUnderlying', c_uint8),
        ('isCrdCollateralTradable', c_uint8),
        ('collateralRatio', c_int32),
        ('marginBuyRatio', c_int32),
        ('shortSellRatio', c_int32),
        ('marketCapPrice', c_int32),

        ('sellAvlHld', c_int64),
        ('trsfOutAvlHld', c_int64),
        ('repayStockDirectAvlHld', c_int64),
        ('shortSellRepayableDebtQty', c_int64),

        ('specialSecurityPositionQty', c_int64),
        ('specialSecurityPositionUsedQty', c_int64),

        ('specialSecurityPositionAvailableQty', c_int64),
        ('publicSecurityPositionQty', c_int64),
        ('publicSecurityPositionAvailableQty', c_int64),

        ('collateralHoldingQty', c_int64),
        ('collateralUncomeBuyQty', c_int64),
        ('collateralUncomeTrsfInQty', c_int64),

        ('collateralUncomeSellQty', c_int64),
        ('collateralTrsfOutQty', c_int64),
        ('collateralRepayDirectQty', c_int64),

        ('marginBuyDebtAmt', c_int64),
        ('marginBuyDebtFee', c_int64),
        ('marginBuyDebtInterest', c_int64),
        ('marginBuyDebtQty', c_int64),

        ('marginBuyUncomeAmt', c_int64),
        ('marginBuyUncomeFee', c_int64),
        ('marginBuyUncomeInterest', c_int64),
        ('marginBuyUncomeQty', c_int64),

        ('marginBuyOriginDebtAmt', c_int64),
        ('marginBuyOriginDebtQty', c_int64),
        ('marginBuyRepaidAmt', c_int64),
        ('marginBuyRepaidQty', c_int64),

        ('shortSellDebtAmt', c_int64),
        ('shortSellDebtFee', c_int64),
        ('shortSellDebtInterest', c_int64),
        ('shortSellDebtQty', c_int64),

        ('shortSellUncomeAmt', c_int64),
        ('shortSellUncomeFee', c_int64),
        ('shortSellUncomeInterest', c_int64),
        ('shortSellUncomeQty', c_int64),

        ('shortSellOriginDebtQty', c_int64),
        ('shortSellRepaidQty', c_int64),
        ('shortSellUncomeRepaidQty', c_int64),
        ('shortSellRepaidAmt', c_int64),
        ('shortSellRealRepaidAmt', c_int64),

        ('otherDebtAmt', c_int64),
        ('otherDebtInterest', c_int64),

        ('__reserve', c_char * 32),
    ]


class OesCrdExcessStockBaseInfoT(BaseStructure):
    _fields_ = [
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        ('mktId', c_uint8),
        ('__filler', c_uint8 * 7),

        ('originExcessStockQty', c_int64),
        ('excessStockTotalQty', c_int64),
        ('excessStockUncomeTrsfQty', c_int64),
        ('excessStockTrsfAbleQty', c_int64),

        ('__reserve', c_char * 32),
    ]
