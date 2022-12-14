from enum import Enum


OES_CLIENT_NAME_MAX_LEN = 32
OES_CLIENT_DESC_MAX_LEN = 32
OES_CLIENT_TAG_MAX_LEN = 32
OES_PWD_MAX_LEN = 40
OES_VER_ID_MAX_LEN = 32
OES_MAX_COMP_ID_LEN = 32
OES_MAX_CLIENT_ENVID_COUNT = 128
OES_MAX_BATCH_ORDERS_COUNT = 500
OES_MAX_BATCH_ORDERS_SINGLE_COMMIT = 500
OES_MAX_BATCH_ORDERS_UPPER_LIMIT = 10000

OES_CUST_ID_MAX_LEN = 16
OES_CUST_ID_REAL_LEN = 12
OES_CUST_NAME_MAX_LEN = 64
OES_CUST_LONG_NAME_MAX_LEN = 128

OES_CASH_ACCT_ID_MAX_LEN = 16
OES_CASH_ACCT_ID_REAL_LEN = 12

OES_INV_ACCT_ID_MAX_LEN = 16
OES_INV_ACCT_ID_REAL_LEN = 10

OES_BRANCH_ID_MAX_LEN = 8
OES_BRANCH_ID_REAL_LEN = 5

OES_BANK_NO_MAX_LEN = 8
OES_BANK_NO_REAL_LEN = 4

OES_PBU_MAX_LEN = 8
OES_PBU_REAL_LEN = 6

OES_SECURITY_MAX_COUNT = 50000
OES_SECURITY_ID_MAX_LEN = 16
OES_STOCK_ID_REAL_LEN = 6

OES_SECURITY_NAME_MAX_LEN = 24
OES_SECURITY_NAME_REAL_LEN = 20
OES_SECURITY_LONG_NAME_MAX_LEN = 80
OES_SECURITY_ENGLISH_NAME_MAX_LEN = 48
OES_SECURITY_ISIN_CODE_MAX_LEN = 16

OES_EXCH_ORDER_ID_MAX_LEN = 17
OES_EXCH_ORDER_ID_SSE_LEN = 8
OES_EXCH_ORDER_ID_SZSE_LEN = 16

OES_MAX_IP_LEN = 16
OES_MAX_MAC_LEN = 20
OES_MAX_MAC_ALGIN_LEN = 24
OES_MAX_DRIVER_ID_LEN = 21
OES_MAX_DRIVER_ID_ALGIN_LEN = 24

OES_MAX_TEST_REQ_ID_LEN = 32
OES_MAX_SENDING_TIME_LEN = 22
OES_REAL_SENDING_TIME_LEN = 21

OES_MAX_ERROR_INFO_LEN = 64
OES_NOTIFY_CONTENT_MAX_LEN = 296
OES_MAX_ALLOT_SERIALNO_LEN = 64

OES_CASH_UNIT = 10000
OES_FUND_TRSF_UNIT = 100
OES_FEE_RATE_UNIT = 10000000
OES_ETF_CASH_RATIO_UNIT = 100000
OES_BOND_INTEREST_UNIT = 100000000
OES_STK_POSITION_LIMIT_UNIT = 1000000

OES_BASIS_POINT_RATIO_UNIT = 10000
OES_PERCENTAGE_RATIO_UNIT = 100
OES_PERMILLAGE_RATIO_UNIT = 1000

OES_AUCTION_UP_DOWN_RATE_UNIT = 100
OES_MAX_BS_PRICE = 10000 * OES_CASH_UNIT

OES_BROKER_NAME_MAX_LEN = 128
OES_BROKER_MARGIN_ACCT_MAX_LEN = 32
OES_BROKER_PHONE_MAX_LEN = 32
OES_BROKER_WEBSITE_MAX_LEN = 256

OES_APPL_DISCARD_VERSION_MAX_COUNT = 5
OES_APPL_UPGRADE_PROTOCOL_MAX_LEN = 32

OES_OPTION_MAX_COUNT = 10000
OES_OPTION_ID_REAL_LEN = 8
OES_SECURITY_STATUS_FLAG_MAX_LEN = 8
OES_CONTRACT_EXCH_ID_MAX_LEN = 24
OES_CONTRACT_EXCH_ID_REAL_LEN = 19
OES_CONTRACT_SYMBOL_MAX_LEN = 56

OES_MARGIN_RATIO_UNIT = 10000
OES_LINE_RATIO_UNIT = 10000

OES_OPTION_MARGIN_MAX_RATIO = 99999999

OES_CREDIT_COMPACT_ID_MAX_LEN = 32
OES_CREDIT_DEBT_ID_MAX_LEN = 32
OES_CREDIT_DEBT_ID_REAL_LEN = 32

OES_CREDIT_MARGIN_RATIO_UNIT = 10000
OES_CREDIT_INTEREST_RATIO_UNIT = 10000
OES_CREDIT_MAINTENANCE_RATIO_UNIT = 1000
OES_CREDIT_INTEREST_CALC_DAYS = 360

OES_CREDIT_MAINTENANCE_MAX_RATIO = 99999999

OES_LIMIT_BUY = 1 << 1
OES_LIMIT_SELL = 1 << 2
OES_LIMIT_RECALL_DESIGNATION = 1 << 3
OES_LIMIT_DESIGNATION = 1 << 4
OES_LIMIT_REPO = 1 << 5
OES_LIMIT_REVERSE_REPO = 1 << 6
OES_LIMIT_SUBSCRIPTION = 1 << 7
OES_LIMIT_CONVERTIBLE_BOND = 1 << 8
OES_LIMIT_MARKET_ORDER = 1 << 9

OES_LIMIT_BUY_OPEN = 1 << 10
OES_LIMIT_SELL_CLOSE = 1 << 11
OES_LIMIT_SELL_OPEN = 1 << 12
OES_LIMIT_BUY_CLOSE = 1 << 13
OES_LIMIT_COVERED_OPEN = 1 << 14
OES_LIMIT_COVERED_CLOSE = 1 << 15
OES_LIMIT_UNDERLYING_FREEZE = 1 << 16
OES_LIMIT_UNDERLYING_UNFREEZE = 1 << 17
OES_LIMIT_OPTION_EXERCISE = 1 << 18

OES_LIMIT_DEPOSIT = 1 << 21
OES_LIMIT_WITHDRAW = 1 << 22
OES_LIMIT_SSE_BOND_PLATFORM = 1 << 23
OES_LIMIT_ETF_CREATION = 1 << 24
OES_LIMIT_ETF_REDEMPTION = 1 << 25

OES_LIMIT_COLLATERAL_TRANSFER_IN = 1 << 31
OES_LIMIT_COLLATERAL_TRANSFER_OUT = 1 << 32
OES_LIMIT_MARGIN_BUY = 1 << 33
OES_LIMIT_REPAY_MARGIN_BY_SELL = 1 << 34
OES_LIMIT_REPAY_MARGIN_DIRECT = 1 << 35
OES_LIMIT_SHORT_SELL = 1 << 36

OES_LIMIT_REPAY_STOCK_BY_BUY = 1 << 37

OES_LIMIT_REPAY_STOCK_DIRECT = 1 << 38


class eOesExchangeIdT(Enum):
    OES_EXCH_UNDEFINE = 0
    OES_EXCH_SSE = 1
    OES_EXCH_SZSE = 2


class eOesMarketIdT(Enum):
    OES_MKT_UNDEFINE = 0
    OES_MKT_SH_ASHARE = 1
    OES_MKT_SZ_ASHARE = 2
    OES_MKT_SH_OPTION = 3
    OES_MKT_SZ_OPTION = 4
    OES_MKT_EXT_HK = 11
    OES_MKT_EXT_BJ = 12
    OES_MKT_EXT_OTHER = 99


class eOesPlatformIdT(Enum):
    OES_PLATFORM_UNDEFINE = 0
    OES_PLATFORM_CASH_AUCTION = 1
    OES_PLATFORM_FINANCIAL_SERVICES = 2
    OES_PLATFORM_NON_TRADE = 3
    OES_PLATFORM_DERIVATIVE_AUCTION = 4
    OES_PLATFORM_INTERNATIONAL_MARKET = 5
    OES_PLATFORM_BOND_TRADING = 6


class eOesMarketStateT(Enum):
    OES_MKT_STATE_UNDEFINE = 0
    OES_MKT_STATE_PRE_OPEN = 1
    OES_MKT_STATE_OPEN_UP_COMING = 2
    OES_MKT_STATE_OPEN = 3
    OES_MKT_STATE_HALT = 4
    OES_MKT_STATE_CLOSE = 5


class eOesTrdSessTypeT(Enum):
    OES_TRD_SESS_TYPE_O = 0
    OES_TRD_SESS_TYPE_T = 1
    OES_TRD_SESS_TYPE_C = 2


class eOesProductTypeT(Enum):
    OES_PRODUCT_TYPE_UNDEFINE = 0
    OES_PRODUCT_TYPE_EQUITY = 1
    OES_PRODUCT_TYPE_BOND_STD = 2
    OES_PRODUCT_TYPE_IPO = 3
    OES_PRODUCT_TYPE_ALLOTMENT = 4
    OES_PRODUCT_TYPE_OPTION = 5


class eOesSecurityTypeT(Enum):
    OES_SECURITY_TYPE_UNDEFINE = 0
    OES_SECURITY_TYPE_STOCK = 1
    OES_SECURITY_TYPE_BOND = 2
    OES_SECURITY_TYPE_ETF = 3
    OES_SECURITY_TYPE_FUND = 4
    OES_SECURITY_TYPE_OPTION = 5
    OES_SECURITY_TYPE_MGR = 9


class eOesSubSecurityTypeT(Enum):
    OES_SUB_SECURITY_TYPE_UNDEFINE = 0
    OES_SUB_SECURITY_TYPE_STOCK_ASH = 11
    OES_SUB_SECURITY_TYPE_STOCK_SME = 12
    OES_SUB_SECURITY_TYPE_STOCK_GEM = 13
    OES_SUB_SECURITY_TYPE_STOCK_KSH = 14
    OES_SUB_SECURITY_TYPE_STOCK_KCDR = 15
    OES_SUB_SECURITY_TYPE_STOCK_CDR = 16
    OES_SUB_SECURITY_TYPE_STOCK_HLTCDR = 17
    OES_SUB_SECURITY_TYPE_STOCK_GEMCDR = 18

    OES_SUB_SECURITY_TYPE_BOND_GBF = 21
    OES_SUB_SECURITY_TYPE_BOND_CBF = 22
    OES_SUB_SECURITY_TYPE_BOND_CPF = 23
    OES_SUB_SECURITY_TYPE_BOND_CCF = 24
    OES_SUB_SECURITY_TYPE_BOND_FBF = 25
    OES_SUB_SECURITY_TYPE_BOND_PRP = 26
    OES_SUB_SECURITY_TYPE_BOND_STD = 27
    OES_SUB_SECURITY_TYPE_BOND_EXG = 28

    OES_SUB_SECURITY_TYPE_ETF_SINGLE_MKT = 31
    OES_SUB_SECURITY_TYPE_ETF_CROSS_MKT = 32
    OES_SUB_SECURITY_TYPE_ETF_BOND = 33
    OES_SUB_SECURITY_TYPE_ETF_CURRENCY = 34
    OES_SUB_SECURITY_TYPE_ETF_CROSS_BORDER = 35
    OES_SUB_SECURITY_TYPE_ETF_GOLD = 36
    OES_SUB_SECURITY_TYPE_ETF_COMMODITY_FUTURES = 37

    OES_SUB_SECURITY_TYPE_FUND_LOF = 41
    OES_SUB_SECURITY_TYPE_FUND_CEF = 42
    OES_SUB_SECURITY_TYPE_FUND_OEF = 43
    OES_SUB_SECURITY_TYPE_FUND_GRADED = 44
    OES_SUB_SECURITY_TYPE_FUND_REITS = 45

    OES_SUB_SECURITY_TYPE_OPTION_ETF = 51
    OES_SUB_SECURITY_TYPE_OPTION_STOCK = 52

    OES_SUB_SECURITY_TYPE_MGR_SSE_DESIGNATION = 91
    OES_SUB_SECURITY_TYPE_MGR_SSE_RECALL_DESIGNATION = 92
    OES_SUB_SECURITY_TYPE_MGR_SZSE_DESIGNATION = 93
    OES_SUB_SECURITY_TYPE_MGR_SZSE_CANCEL_DESIGNATION = 94
    OES_SUB_SECURITY_TYPE_MGR_OPT_EXERCISE_TRANSFER = 95
    OES_SUB_SECURITY_TYPE_MGR_CRD_COLLATERAL_TRANSFER = 96


class eOesSecurityLevelT(Enum):
    OES_SECURITY_LEVEL_UNDEFINE = 0
    OES_SECURITY_LEVEL_N = 1
    OES_SECURITY_LEVEL_XST = 2
    OES_SECURITY_LEVEL_ST = 3
    OES_SECURITY_LEVEL_P = 4
    OES_SECURITY_LEVEL_T = 5
    OES_SECURITY_LEVEL_U = 6


class eOesSecurityRiskLevelT(Enum):
    OES_RISK_LEVEL_VERY_LOW = 0
    OES_RISK_LEVEL_LOW = 1
    OES_RISK_LEVEL_MEDIUM_LOW = 2
    OES_RISK_LEVEL_MEDIUM = 3
    OES_RISK_LEVEL_MEDIUM_HIGH = 4
    OES_RISK_LEVEL_HIGH = 5
    OES_RISK_LEVEL_VERY_HIGH = 6


class eOesSecuritySuspFlagT(Enum):
    OES_SUSPFLAG_NONE = 0x0
    OES_SUSPFLAG_EXCHANGE = 0x1
    OES_SUSPFLAG_BROKER = 0x2
    OES_SUSPFLAG_MARKET_CLOSE = 0x4


class eOesSecurityStatusT(Enum):
    OES_SECURITY_STATUS_NONE = 0
    OES_SECURITY_STATUS_FIRST_LISTING = (1 << 0)
    OES_SECURITY_STATUS_RESUME_FIRST_LISTING = (1 << 1)
    OES_SECURITY_STATUS_NEW_LISTING = (1 << 2)
    OES_SECURITY_STATUS_EXCLUDE_RIGHT = (1 << 3)
    OES_SECURITY_STATUS_EXCLUDE_DIVIDEN = (1 << 4)
    OES_SECURITY_STATUS_SUSPEND = (1 << 5)
    OES_SECURITY_STATUS_SPECIAL_TREATMENT = (1 << 6)
    OES_SECURITY_STATUS_X_SPECIAL_TREATMENT = (1 << 7)
    OES_SECURITY_STATUS_DELIST_PERIOD = (1 << 8)
    OES_SECURITY_STATUS_DELIST_TRANSFER = (1 << 9)


class eOesSecurityAttributeT(Enum):
    OES_SECURITY_ATTR_NONE = 0
    OES_SECURITY_ATTR_INNOVATION = (1 << 0)
    OES_SECURITY_ATTR_KSH = (1 << 1)


class eOesAuctionLimitTypeT(Enum):
    OES_AUCTION_LIMIT_TYPE_NONE = 0
    OES_AUCTION_LIMIT_TYPE_RATE = 1
    OES_AUCTION_LIMIT_TYPE_ABSOLUTE = 2


class eOesAuctionReferPriceTypeT(Enum):
    OES_AUCTION_REFER_PRICE_TYPE_LAST = 1
    OES_AUCTION_REFER_PRICE_TYPE_BEST = 2


class eOesLotTypeT(Enum):
    OES_LOT_TYPE_UNDEFINE = 0
    OES_LOT_TYPE_FAILED = 1
    OES_LOT_TYPE_ASSIGNMENT = 2
    OES_LOT_TYPE_LOTTERY = 3


class eOesLotRejReasonT(Enum):
    OES_LOT_REJ_REASON_DUPLICATE = 1
    OES_LOT_REJ_REASON_INVALID_DUPLICATE = 2
    OES_LOT_REJ_REASON_OFFLINE_FIRST = 3
    OES_LOT_REJ_REASON_BAD_RECORD = 4
    OES_LOT_REJ_REASON_UNKNOW = 5


class eOesSecurityIssueTypeT(Enum):
    OES_ISSUE_TYPE_UNDEFINE = 0
    OES_ISSUE_TYPE_MKT_QUOTA = 1
    OES_ISSUE_TYPE_CASH = 2
    OES_ISSUE_TYPE_CREDIT = 3


class eOesPricingMethodT(Enum):
    OES_PRICING_METHOD_UNDEFINE = 0
    OES_PRICING_METHOD_CLEAN = 1
    OES_PRICING_METHOD_DIRTY = 2


class eOesOrdStatusT(Enum):
    OES_ORD_STATUS_PENDING = 0
    OES_ORD_STATUS_NEW = 1
    OES_ORD_STATUS_DECLARED = 2
    OES_ORD_STATUS_PARTIALLY_FILLED = 3

    OES_ORD_STATUS_CANCEL_DONE = 5
    OES_ORD_STATUS_PARTIALLY_CANCELED = 6
    OES_ORD_STATUS_CANCELED = 7
    OES_ORD_STATUS_FILLED = 8

    OES_ORD_STATUS_INVALID_OES = 11
    OES_ORD_STATUS_INVALID_EXCHANGE = 12
    OES_ORD_STATUS_INVALID_TGW_REJECT = 13
    OES_ORD_STATUS_INVALID_TGW_COMM = 14
    OES_ORD_STATUS_INVALID_TGW_TRY_AGAIN = 18


class eOesOrdTypeT(Enum):
    OES_ORD_TYPE_LMT = 0
    OES_ORD_TYPE_LMT_FOK = 1
    OES_ORD_TYPE_MTL_BEST_5 = 10
    OES_ORD_TYPE_MTL_BEST = 11
    OES_ORD_TYPE_MTL_SAMEPARTY_BEST = 12
    OES_ORD_TYPE_MTL = 13
    OES_ORD_TYPE_FAK_BEST_5 = 20
    OES_ORD_TYPE_FAK = 21
    OES_ORD_TYPE_FOK = 30


class eOesOrdTypeShT(Enum):
    OES_ORD_TYPE_SH_LMT = eOesOrdTypeT.OES_ORD_TYPE_LMT.value
    OES_ORD_TYPE_SH_MTL_BEST_5 = eOesOrdTypeT.OES_ORD_TYPE_MTL_BEST_5.value
    OES_ORD_TYPE_SH_MTL_BEST = eOesOrdTypeT.OES_ORD_TYPE_MTL_BEST.value
    OES_ORD_TYPE_SH_MTL_SAMEPARTY_BEST = eOesOrdTypeT.OES_ORD_TYPE_MTL_SAMEPARTY_BEST.value
    OES_ORD_TYPE_SH_FAK_BEST_5 = eOesOrdTypeT.OES_ORD_TYPE_FAK_BEST_5.value


class eOesOrdTypeShOptT(Enum):
    OES_ORD_TYPE_SHOPT_LMT = eOesOrdTypeT.OES_ORD_TYPE_LMT.value
    OES_ORD_TYPE_SHOPT_LMT_FOK = eOesOrdTypeT.OES_ORD_TYPE_LMT_FOK.value
    OES_ORD_TYPE_SHOPT_MTL = eOesOrdTypeT.OES_ORD_TYPE_MTL.value
    OES_ORD_TYPE_SHOPT_FAK = eOesOrdTypeT.OES_ORD_TYPE_FAK.value
    OES_ORD_TYPE_SHOPT_FOK = eOesOrdTypeT.OES_ORD_TYPE_FOK.value


class eOesOrdTypeSzT(Enum):
    OES_ORD_TYPE_SZ_LMT = eOesOrdTypeT.OES_ORD_TYPE_LMT.value
    OES_ORD_TYPE_SZ_LMT_FOK = eOesOrdTypeT.OES_ORD_TYPE_LMT_FOK.value
    OES_ORD_TYPE_SZ_MTL_BEST = eOesOrdTypeT.OES_ORD_TYPE_MTL_BEST.value
    OES_ORD_TYPE_SZ_MTL_SAMEPARTY_BEST = eOesOrdTypeT.OES_ORD_TYPE_MTL_SAMEPARTY_BEST.value
    OES_ORD_TYPE_SZ_FAK_BEST_5 = eOesOrdTypeT.OES_ORD_TYPE_FAK_BEST_5.value
    OES_ORD_TYPE_SZ_FAK = eOesOrdTypeT.OES_ORD_TYPE_FAK.value
    OES_ORD_TYPE_SZ_FOK = eOesOrdTypeT.OES_ORD_TYPE_FOK.value


class eOesBuySellTypeT(Enum):
    OES_BS_TYPE_UNDEFINE = 0

    OES_BS_TYPE_BUY = 1
    OES_BS_TYPE_SELL = 2
    OES_BS_TYPE_CREATION = 3
    OES_BS_TYPE_REDEMPTION = 4
    OES_BS_TYPE_REVERSE_REPO = 6
    OES_BS_TYPE_SUBSCRIPTION = 7
    OES_BS_TYPE_ALLOTMENT = 8

    OES_BS_TYPE_BUY_OPEN = 11
    OES_BS_TYPE_SELL_CLOSE = 12
    OES_BS_TYPE_SELL_OPEN = 13
    OES_BS_TYPE_BUY_CLOSE = 14
    OES_BS_TYPE_COVERED_OPEN = 15
    OES_BS_TYPE_COVERED_CLOSE = 16
    OES_BS_TYPE_OPTION_EXERCISE = 17
    OES_BS_TYPE_UNDERLYING_FREEZE = 18
    OES_BS_TYPE_UNDERLYING_UNFREEZE = 19

    OES_BS_TYPE_CANCEL = 30

    OES_BS_TYPE_COLLATERAL_BUY = OES_BS_TYPE_BUY
    OES_BS_TYPE_COLLATERAL_SELL = OES_BS_TYPE_SELL
    OES_BS_TYPE_COLLATERAL_TRANSFER_IN = 31
    OES_BS_TYPE_COLLATERAL_TRANSFER_OUT = 32

    OES_BS_TYPE_MARGIN_BUY = 33
    OES_BS_TYPE_REPAY_MARGIN_BY_SELL = 34

    OES_BS_TYPE_SHORT_SELL = 35
    OES_BS_TYPE_REPAY_STOCK_BY_BUY = 36
    OES_BS_TYPE_REPAY_STOCK_DIRECT = 37


class eOesOrdDirT(Enum):
    OES_ORD_DIR_BUY = 0
    OES_ORD_DIR_SELL = 1


class eOesOrdMandatoryFlagT(Enum):
    OES_ORD_MANDATORY_FLAG_NONE = 0
    OES_ORD_MANDATORY_FLAG_DELEGATE = 1
    OES_ORD_MANDATORY_FLAG_LIQUDATION = 11
    OES_ORD_MANDATORY_FLAG_MANAGEMENT = 12


class eOesTrdCnfmTypeT(Enum):
    OES_TRDCNFM_TYPE_NORMAL = 0

    OES_TRDCNFM_TYPE_ETF_FIRST = 1
    OES_TRDCNFM_TYPE_ETF_CMPOENT = 2
    OES_TRDCNFM_TYPE_ETF_CASH = 3
    OES_TRDCNFM_TYPE_ETF_LAST = 4

    OES_TRDCNFM_TYPE_OPT_QP1 = 11
    OES_TRDCNFM_TYPE_OPT_CV1 = 12


class eOesEtfSubFlagT(Enum):
    OES_ETF_SUBFLAG_FORBID_SUB = 0
    OES_ETF_SUBFLAG_ALLOW_SUB = 1
    OES_ETF_SUBFLAG_MUST_SUB = 2
    OES_ETF_SUBFLAG_SZ_REFUND_SUB = 3
    OES_ETF_SUBFLAG_SZ_MUST_SUB = 4
    OES_ETF_SUBFLAG_OTHER_REFUND_SUB = 5
    OES_ETF_SUBFLAG_OTHER_MUST_SUB = 6
    OES_ETF_SUBFLAG_HK_REFUND_SUB = 7
    OES_ETF_SUBFLAG_HK_MUST_SUB = 8


class eOesEtfCashTypeT(Enum):
    OES_ETF_CASH_TYPE_UNUSABLE = 0
    OES_ETF_CASH_TYPE_SSE_HK = 1
    OES_ETF_CASH_TYPE_NORMAL = 11
    OES_ETF_CASH_TYPE_SSE_SH = 12
    OES_ETF_CASH_TYPE_SSE_SZ = 13
    OES_ETF_CASH_TYPE_SSE_OTHER = 14


class eOesEtfAllCashFlagT(Enum):
    OES_ETF_ALL_CASH_FLAG_UNDERLYING = 0
    OES_ETF_ALL_CASH_FLAG_CASH = 1


class eOesExecTypeT(Enum):
    OES_EXECTYPE_UNDEFINE = 0
    OES_EXECTYPE_INSERT = 1
    OES_EXECTYPE_CONFIRMED = 2
    OES_EXECTYPE_CANCELLED = 3
    OES_EXECTYPE_AUTO_CANCELLED = 4
    OES_EXECTYPE_REJECT = 5
    OES_EXECTYPE_TRADE = 6
    OES_EXECTYPE_REPAY = 7


class eOesCurrTypeT(Enum):
    OES_CURR_TYPE_RMB = 0
    OES_CURR_TYPE_HKD = 1
    OES_CURR_TYPE_USD = 2


class eOesFeeTypeT(Enum):
    OES_FEE_TYPE_EXCHANGE_STAMP = 0x1
    OES_FEE_TYPE_EXCHANGE_TRANSFER = 0x2
    OES_FEE_TYPE_EXCHANGE_SETTLEMENT = 0x3
    OES_FEE_TYPE_EXCHANGE_TRADE_RULE = 0x4
    OES_FEE_TYPE_EXCHANGE_EXCHANGE = 0x5
    OES_FEE_TYPE_EXCHANGE_ADMINFER = 0x6
    OES_FEE_TYPE_EXCHANGE_OTHER = 0x7
    OES_FEE_TYPE_BROKER_BACK_END = 0x11
    OES_FEE_TYPE_BROKER_CREDIT_INTEREST = 0x21


class eOesCalcFeeModeT(Enum):
    OES_CALC_FEE_MODE_AMOUNT = 0
    OES_CALC_FEE_MODE_QTY = 1
    OES_CALC_FEE_MODE_ORD = 2


class eOesFundTrsfDirectT(Enum):
    OES_FUND_TRSF_DIRECT_IN = 0
    OES_FUND_TRSF_DIRECT_OUT = 1


class eOesFundTrsfTypeT(Enum):
    OES_FUND_TRSF_TYPE_OES_BANK = 0
    OES_FUND_TRSF_TYPE_OES_COUNTER = 1
    OES_FUND_TRSF_TYPE_COUNTER_BANK = 2
    OES_FUND_TRSF_TYPE_OES_TO_OES = 3


class eOesFundTrsfStatusT(Enum):
    OES_FUND_TRSF_STS_UNDECLARED = 0
    OES_FUND_TRSF_STS_DECLARED = 1
    OES_FUND_TRSF_STS_WAIT_DONE = 2
    OES_FUND_TRSF_STS_DONE = 3
    OES_FUND_TRSF_STS_UNDECLARED_ROLLBACK = 6
    OES_FUND_TRSF_STS_DECLARED_ROLLBACK = 7
    OES_FUND_TRSF_STS_INVALID_OES = 11
    OES_FUND_TRSF_STS_INVALID_COUNTER = 12
    OES_FUND_TRSF_STS_SUSPENDED = 13


class eOesFundTrsfSourceTypeT(Enum):
    OES_FUND_TRSF_SOURCE_UNDEFINE = 0
    OES_FUND_TRSF_SOURCE_CUST = 1
    OES_FUND_TRSF_SOURCE_TIMER = 2
    OES_FUND_TRSF_SOURCE_COLO_PEER = 3


class eOesBusinessTypeT(Enum):
    OES_BUSINESS_TYPE_UNDEFINE = 0x0
    OES_BUSINESS_TYPE_STOCK = 0x01
    OES_BUSINESS_TYPE_OPTION = 0x02
    OES_BUSINESS_TYPE_CREDIT = 0x04
    OES_BUSINESS_TYPE_ALL = 0xFF


class eOesAcctTypeT(Enum):
    OES_ACCT_TYPE_NORMAL = 0
    OES_ACCT_TYPE_CREDIT = 1
    OES_ACCT_TYPE_OPTION = 2


class eOesAcctStatusT(Enum):
    OES_ACCT_STATUS_NORMAL = 0
    OES_ACCT_STATUS_DISABLED = 1
    OES_ACCT_STATUS_LOCKED = 2


class eOesTradingPermissionT(Enum):
    OES_PERMIS_MARKET_ORDER = 1 << 1
    OES_PERMIS_STRUCTURED_FUND = 1 << 2
    OES_PERMIS_BOND_QUALIFIED_INVESTOR = 1 << 3

    OES_PERMIS_DELISTING = 1 << 5
    OES_PERMIS_RISK_WARNING = 1 << 6

    OES_PERMIS_SINGLE_MARKET_ETF = 1 << 7
    OES_PERMIS_CROSS_BORDER_ETF = 1 << 8
    OES_PERMIS_CROSS_MARKET_ETF = 1 << 9
    OES_PERMIS_CURRENCY_ETF = 1 << 10

    OES_PERMIS_GEMCDR = 1 << 11
    OES_PERMIS_GEM_REGISTRATION = 1 << 12
    OES_PERMIS_GEM_UNREGISTRATION = 1 << 13
    OES_PERMIS_SH_HK_STOCK_CONNECT = 1 << 14
    OES_PERMIS_SZ_HK_STOCK_CONNECT = 1 << 15

    OES_PERMIS_HLTCDR = 1 << 16
    OES_PERMIS_CDR = 1 << 17
    OES_PERMIS_INNOVATION = 1 << 18
    OES_PERMIS_KSH = 1 << 19

    OES_PERMIS_BOND_ETF = 1 << 20
    OES_PERMIS_GOLD_ETF = 1 << 21
    OES_PERMIS_COMMODITY_FUTURES_ETF = 1 << 22
    OES_PERMIS_GEM_INNOVATION = 1 << 23

    OES_PERMIS_CONVERTIBLE_BOND = 1 << 24
    OES_PERMIS_REITS = 1 << 25
    OES_PERMIS_CORPORATE_BOND = 1 << 26


class eOesQualificationClassT(Enum):
    OES_QUALIFICATION_PUBLIC_INVESTOR = 0
    OES_QUALIFICATION_QUALIFIED_INVESTOR = 1
    OES_QUALIFICATION_QUALIFIED_INSTITUTIONAL = 2


class eOesInvestorClassT(Enum):
    OES_INVESTOR_CLASS_NORMAL = 0
    OES_INVESTOR_CLASS_PROFESSIONAL_A = 1
    OES_INVESTOR_CLASS_PROFESSIONAL_B = 2
    OES_INVESTOR_CLASS_PROFESSIONAL_C = 3
    OES_INVESTOR_CLASS_PROFESSIONAL = 4


class eOesCustTypeT(Enum):
    OES_CUST_TYPE_PERSONAL = 0
    OES_CUST_TYPE_INSTITUTION = 1
    OES_CUST_TYPE_PROPRIETARY = 2
    OES_CUST_TYPE_PRODUCT = 3
    OES_CUST_TYPE_MKT_MAKER = 4
    OES_CUST_TYPE_OTHERS = 5


class eOesOwnerTypeT(Enum):
    OES_OWNER_TYPE_UNDEFINE = 0
    OES_OWNER_TYPE_PERSONAL = 1
    OES_OWNER_TYPE_EXCHANGE = 101
    OES_OWNER_TYPE_MEMBER = 102
    OES_OWNER_TYPE_INSTITUTION = 103
    OES_OWNER_TYPE_PROPRIETARY = 104
    OES_OWNER_TYPE_MKT_MAKER = 105
    OES_OWNER_TYPE_SETTLEMENT = 106


class eOesClientTypeT(Enum):
    OES_CLIENT_TYPE_UNDEFINED = 0
    OES_CLIENT_TYPE_INVESTOR = 1
    OES_CLIENT_TYPE_VIRTUAL = 2


class eOesClientStatusT(Enum):
    OES_CLIENT_STATUS_UNACTIVATED = 0
    OES_CLIENT_STATUS_ACTIVATED = 1
    OES_CLIENT_STATUS_PAUSE = 2
    OES_CLIENT_STATUS_SUSPENDED = 3
    OES_CLIENT_STATUS_CANCELLED = 4


class eOesNotifySourceT(Enum):
    OES_NOTIFY_SOURCE_UNDEFINE = 0
    OES_NOTIFY_SOURCE_OES = 1
    OES_NOTIFY_SOURCE_MON = 2
    OES_NOTIFY_SOURCE_BROKER = 3
    OES_NOTIFY_SOURCE_EXCHANGE = 4
    OES_NOTIFY_SOURCE_CSDC = 5


class eOesNotifyTypeT(Enum):
    OES_NOTIFY_TYPE_UNDEFINE = 0

    OES_NOTIFY_TYPE_CONTRACT_EXPIRE = 1
    OES_NOTIFY_TYPE_CONTRACT_ADJUSTED = 2
    OES_NOTIFY_TYPE_UNDERLYING_DR_PROXIMITY = 3
    OES_NOTIFY_TYPE_EXERCISE_DATE_PROXIMITY = 4
    OES_NOTIFY_TYPE_EXERCISED_POSSIBILITY = 5
    OES_NOTIFY_TYPE_EXERCISE_ASSIGNED = 6
    OES_NOTIFY_TYPE_COVERED_NOT_ENOUGH = 7
    OES_NOTIFY_TYPE_DELIVERY_NOT_ENOUGH = 8
    OES_NOTIFY_TYPE_MARGIN_CALL = 9
    OES_NOTIFY_TYPE_FORCED_CLOSE = 10

    OES_NOTIFY_TYPE_CRD_COLLATERAL_INFO_UPDATE = 61
    OES_NOTIFY_TYPE_CRD_UNDERLYING_INFO_UPDATE = 62
    OES_NOTIFY_TYPE_CRD_CASH_POSITION_UPDATE = 63
    OES_NOTIFY_TYPE_CRD_SECURITY_POSITION_UPDATE = 64
    OES_NOTIFY_TYPE_CRD_MAINTENANCE_RATIO_UPDATE = 65
    OES_NOTIFY_TYPE_CRD_LINE_OF_CERDIT_UPDATE = 66

    OES_NOTIFY_TYPE_OTHERS = 100


class eOesNotifyLevelT(Enum):
    OES_NOTIFY_LEVEL_UNDEFINE = 0
    OES_NOTIFY_LEVEL_LOW = 1
    OES_NOTIFY_LEVEL_GENERAL = 2
    OES_NOTIFY_LEVEL_IMPORTANT = 3
    OES_NOTIFY_LEVEL_URGENT = 4


class eOesNotifyScopeT(Enum):
    OES_NOTIFY_SCOPE_UNDEFINE = 0
    OES_NOTIFY_SCOPE_CUST = 1
    OES_NOTIFY_SCOPE_ALL = 2


class eOesOptContractTypeT(Enum):
    OES_OPT_CONTRACT_TYPE_UNDEFINE = 0
    OES_OPT_CONTRACT_TYPE_CALL = 1
    OES_OPT_CONTRACT_TYPE_PUT = 2


class eOesOptLimitOpenFlagT(Enum):
    OES_OPT_LIMIT_OPEN_FLAG_NORMAL = 0
    OES_OPT_LIMIT_OPEN_FLAG_LIMITED = 1


class eOesOptExerciseTypeT(Enum):
    OES_OPT_EXERCISE_TYPE_E = 0
    OES_OPT_EXERCISE_TYPE_A = 1
    OES_OPT_EXERCISE_TYPE_B = 2


class eOesOptDeliveryTypeT(Enum):
    OES_OPT_DELIVERY_TYPE_UNDEFINE = 0
    OES_OPT_DELIVERY_TYPE_SECURITY = 1
    OES_OPT_DELIVERY_TYPE_CASH = 2


class eOesOptPositionTypeT(Enum):
    OES_OPT_POSITION_TYPE_UNDEFINE = 0
    OES_OPT_POSITION_TYPE_LONG = 1
    OES_OPT_POSITION_TYPE_SHORT = 2
    OES_OPT_POSITION_TYPE_COVERED = 3


class eOesOptInvLevelT(Enum):
    OES_OPT_INV_LEVEL_UNDEFINE = 0
    OES_OPT_INV_LEVEL_1 = 1
    OES_OPT_INV_LEVEL_2 = 2
    OES_OPT_INV_LEVEL_3 = 3


class eOesPositionEffectT(Enum):
    OES_POSITION_EFFECT_UNDEFINE = 0
    OES_POSITION_EFFECT_OPEN = 1
    OES_POSITION_EFFECT_CLOSE = 2


class eOesCrdDebtTypeT(Enum):
    OES_CRD_DEBT_TYPE_UNDEFINE = 0
    OES_CRD_DEBT_TYPE_MARGIN_BUY = 1
    OES_CRD_DEBT_TYPE_SHORT_SELL = 2
    OES_CRD_DEBT_TYPE_OTHER_DEBT = 3


class eOesCrdCashGroupPropertyT(Enum):
    OES_CRD_CASH_GROUP_PROP_UNDEFINE = 0
    OES_CRD_CASH_GROUP_PROP_PUBLIC = 1
    OES_CRD_CASH_GROUP_PROP_SPECIAL = 2


class eOesCrdDebtStatusT(Enum):
    OES_CRD_DEBT_STATUS_UNDEFINE = 0
    OES_CRD_DEBT_STATUS_NOT_TRADE = 1
    OES_CRD_DEBT_STATUS_NOT_REPAID = 2
    OES_CRD_DEBT_STATUS_PARTIALLY_REPAID = 3
    OES_CRD_DEBT_STATUS_EXPIRED = 4
    OES_CRD_DEBT_STATUS_REPAID = 5
    OES_CRD_DEBT_STATUS_MANNUAL_REPAID = 6
    OES_CRD_DEBT_STATUS_NOT_DEBT = 7


class eOesCrdDebtPostponeStatusT(Enum):
    OES_CRD_DEBT_POSTPONE_STATUS_UNDEFINE = 0
    OES_CRD_DEBT_POSTPONE_STATUS_APPLICABLE = 1
    OES_CRD_DEBT_POSTPONE_STATUS_APPLIED = 2
    OES_CRD_DEBT_POSTPONE_STATUS_APPROVED = 3
    OES_CRD_DEBT_POSTPONE_STATUS_UNAPPROVED = 4
    OES_CRD_DEBT_POSTPONE_STATUS_UNAPPLICABLE = 5


class eOesCrdDebtRepayModeT(Enum):
    OES_CRD_DEBT_REPAY_MODE_UNDEFINE = 0
    OES_CRD_DEBT_REPAY_MODE_MATCHING_PRINCIPAL = 1
    OES_CRD_DEBT_REPAY_MODE_INTEREST_FIRST = 2
    OES_CRD_DEBT_REPAY_MODE_PRINCIPAL_FIRST = 3


class eOesCrdAssignableRepayModeT(Enum):
    OES_CRD_ASSIGNABLE_REPAY_MODE_DEFAULT = 0
    OES_CRD_ASSIGNABLE_REPAY_MODE_INTEREST_ONLY = 10


class eOesCrdDebtJournalTypeT(Enum):
    OES_CRD_DEBT_JOURNAL_TYPE_OPEN_POSITION = 0
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_MARGIN_BY_SELL = 1
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_MARGIN_DIRECT = 2
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_STOCK_BY_BUY = 3
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_STOCK_DIRECT = 4
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_STOCK_BY_CASH = 5
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_STOCK_BY_OUTSIDE = 6
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_MARGIN_BY_OUTSIDE = 7
    OES_CRD_DEBT_JOURNAL_TYPE_CONTRACT_POST_PONE = 8
    OES_CRD_DEBT_JOURNAL_TYPE_OTHER = 9


class eOesCrdCustGuardStatusT(Enum):
    OES_CRD_CUST_GUARD_STATUS_NORMAL = 0
    OES_CRD_CUST_GUARD_STATUS_ALERT = 1
    OES_CRD_CUST_GUARD_STATUS_BLOCKLIST = 2
