from enum import Enum
from ctypes import sizeof

from ..utils import BaseStructure, BaseUnion
from ..utils.types import *
from ..spk.types import STimespec32T


MDS_MAX_SECURITY_CNT_PER_SUBSCRIBE = 4000
MDS_MAX_OPTION_CNT_TOTAL_SUBSCRIBED = 2000

MDS_MAX_USERNAME_LEN = 32
MDS_MAX_PASSWORD_LEN = 40
MDS_CLIENT_TAG_MAX_LEN = 32
MDS_VER_ID_MAX_LEN = 32
MDS_MAX_TEST_REQ_ID_LEN = 32

MDS_MAX_IP_LEN = 16
MDS_MAX_MAC_LEN = 20
MDS_MAX_MAC_ALGIN_LEN = 24
MDS_MAX_DRIVER_ID_LEN = 21
MDS_MAX_DRIVER_ID_ALGIN_LEN = 24

MDS_MAX_INSTR_CODE_LEN = 9
MDS_REAL_STOCK_CODE_LEN = 6
MDS_REAL_OPTION_CODE_LEN = 8
MDS_MAX_POSTFIXED_INSTR_CODE_LEN = 12

MDS_MAX_SECURITY_NAME_LEN = 40
MDS_MAX_SECURITY_LONG_NAME_LEN = 80
MDS_MAX_SECURITY_ENGLISH_NAME_LEN = 48
MDS_MAX_SECURITY_ISIN_CODE_LEN = 16

MDS_MAX_CONTRACT_EXCH_ID_LEN = 24
MDS_REAL_CONTRACT_EXCH_ID_LEN = 19
MDS_MAX_CONTRACT_SYMBOL_LEN = 56

MDS_MAX_SENDING_TIME_LEN = 22
MDS_REAL_SENDING_TIME_LEN = 21

MDS_MAX_TRADE_DATE_LEN = 9
MDS_REAL_TRADE_DATE_LEN = 8

MDS_MAX_UPDATE_TIME_LEN = 9
MDS_REAL_UPDATE_TIME_LEN = 8

MDS_MAX_TRADING_SESSION_ID_LEN = 9
MDS_REAL_TRADING_SESSION_ID_LEN = 8

MDS_MAX_TRADING_PHASE_CODE_LEN = 9
MDS_REAL_TRADING_PHASE_CODE_LEN = 8

MDS_MAX_FINANCIAL_STATUS_LEN = 9
MDS_REAL_FINANCIAL_STATUS_LEN = 8

MDS_MAX_SECURITY_SWITCH_CNT = 40

MDS_UNIFIED_PRICE_UNIT = 10000
MDS_UNIFIED_MONEY_UNIT = 10000

MDS_TOTAL_VALUE_TRADED_UNIT = MDS_UNIFIED_MONEY_UNIT
MDS_INDEX_PRICE_UNIT = MDS_UNIFIED_PRICE_UNIT
MDS_STOCK_PRICE_UNIT = MDS_UNIFIED_PRICE_UNIT
MDS_OPTION_PRICE_UNIT = MDS_UNIFIED_PRICE_UNIT

MDS_MAX_ORDER_PRICE = 1999999999

MDS_MAX_STOCK_ID_SCOPE = 1000000
MDS_MAX_OPTION_ID_SCOPE = 100000000

MDS_MAX_COMP_ID_LEN = 32

MDS_APPL_DISCARD_VERSION_MAX_COUNT = 5
MDS_APPL_UPGRADE_PROTOCOL_MAX_LEN = 32

MDS_MAX_L2_PRICE_LEVEL_INCREMENTS = 40

MDS_MAX_L2_DISCLOSE_ORDERS_CNT = 50

MDS_MAX_L2_DISCLOSE_ORDERS_INCREMENTS = 152


class eMdsExchangeIdT(Enum):
    MDS_EXCH_UNDEFINE = 0
    MDS_EXCH_SSE = 1
    MDS_EXCH_SZSE = 2


class eMdsMsgSourceT(Enum):
    MDS_MSGSRC_UNDEFINED = 0
    MDS_MSGSRC_EZEI_TCP = 1
    MDS_MSGSRC_EZEI_UDP = 2
    MDS_MSGSRC_SSE_MDGW_BINARY = 10
    MDS_MSGSRC_SSE_MDGW_STEP = 11

    MDS_MSGSRC_VDE_LEVEL1 = 20
    MDS_MSGSRC_VDE_LEVEL1_BINARY = 21
    MDS_MSGSRC_VDE_LEVEL2 = 22
    MDS_MSGSRC_VDE_LEVEL2_REBUILD = 29

    MDS_MSGSRC_SZSE_MDGW_BINARY = 31
    MDS_MSGSRC_SZSE_MDGW_STEP = 32
    MDS_MSGSRC_SZSE_MDGW_MULTICAST = 33
    MDS_MSGSRC_SZSE_MDGW_REBUILD = 39

    MDS_MSGSRC_FILE_MKTDT = 90
    MDS_MSGSRC_MDS_TCP = 91
    MDS_MSGSRC_MDS_UDP = 92


class eMdsMdProductTypeT(Enum):
    MDS_MD_PRODUCT_TYPE_UNDEFINE = 0
    MDS_MD_PRODUCT_TYPE_STOCK = 1
    MDS_MD_PRODUCT_TYPE_INDEX = 2
    MDS_MD_PRODUCT_TYPE_OPTION = 3


class eMdsSubStreamTypeT(Enum):
    MDS_SUB_STREAM_TYPE_UNDEFINE = 0
    MDS_SUB_STREAM_TYPE_MARKET_STATUS = 1

    MDS_SUB_STREAM_TYPE_STOCK = 10
    MDS_SUB_STREAM_TYPE_BOND = 20
    MDS_SUB_STREAM_TYPE_BOND_NEGOTIATED = 21
    MDS_SUB_STREAM_TYPE_BOND_CLICK = 22
    MDS_SUB_STREAM_TYPE_BOND_INQUIRY = 23
    MDS_SUB_STREAM_TYPE_BOND_IOI = 24
    MDS_SUB_STREAM_TYPE_BOND_BIDDING = 25
    MDS_SUB_STREAM_TYPE_BOND_BLOCK_TRADE = 26

    MDS_SUB_STREAM_TYPE_FUND = 40
    MDS_SUB_STREAM_TYPE_OPTION = 50

    MDS_SUB_STREAM_TYPE_INDEX = 90
    MDS_SUB_STREAM_TYPE_TRADE_STATS = 91
    MDS_SUB_STREAM_TYPE_CN_INDEX = 92


class eMdsMdLevelT(Enum):
    MDS_MD_LEVEL_0 = 0
    MDS_MD_LEVEL_1 = 1
    MDS_MD_LEVEL_2 = 2


class eMdsL2PriceLevelOperatorT(Enum):
    MDS_L2_PX_OPERATOR_ADD = 1
    MDS_L2_PX_OPERATOR_UPDATE = 2
    MDS_L2_PX_OPERATOR_DELETE = 3


class eMdsL2TradeExecTypeT(Enum):
    MDS_L2_TRADE_EXECTYPE_CANCELED = '4'
    MDS_L2_TRADE_EXECTYPE_TRADE = 'F'


class eMdsL2TradeBSFlagT(Enum):
    MDS_L2_TRADE_BSFLAG_BUY = 'B'
    MDS_L2_TRADE_BSFLAG_SELL = 'S'
    MDS_L2_TRADE_BSFLAG_UNKNOWN = 'N'


class eMdsL2OrderSideT(Enum):
    MDS_L2_ORDER_SIDE_BUY = '1'
    MDS_L2_ORDER_SIDE_SELL = '2'
    MDS_L2_ORDER_SIDE_BORROW = 'G'
    MDS_L2_ORDER_SIDE_LEND = 'F'


class eMdsL2OrderTypeT(Enum):
    MDS_L2_ORDER_TYPE_MKT = '1'
    MDS_L2_ORDER_TYPE_LMT = '2'
    MDS_L2_ORDER_TYPE_SAMEPARTY_BEST = 'U'


class eMdsL2SseOrderTypeT(Enum):
    MDS_L2_SSE_ORDER_TYPE_ADD = 'A'
    MDS_L2_SSE_ORDER_TYPE_DELETE = 'D'
    MDS_L2_SSE_ORDER_TYPE_STATUS = 'S'


class eMdsClientTypeT(Enum):
    MDS_CLIENT_TYPE_UNDEFINED = 0
    MDS_CLIENT_TYPE_INVESTOR = 1
    MDS_CLIENT_TYPE_VIRTUAL = 2


class eMdsClientStatusT(Enum):
    MDS_CLIENT_STATUS_UNACTIVATED = 0
    MDS_CLIENT_STATUS_ACTIVATED = 1
    MDS_CLIENT_STATUS_PAUSE = 2
    MDS_CLIENT_STATUS_SUSPENDED = 3
    MDS_CLIENT_STATUS_CANCELLED = 4


class MdsTradingSessionStatusMsgT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('__isRepeated', c_int8),
        ('__origMdSource', c_uint8),

        ('tradeDate', c_int32),
        ('updateTime', c_int32),
        ('__exchSendingTime', c_int32),
        ('__mdsRecvTime', c_int32),

        ('TotNoRelatedSym', c_int32),

        ('TradingSessionID', c_char * MDS_MAX_TRADING_SESSION_ID_LEN),

        ('__filler3', c_uint8 * 3),
        ('__dataVersion', c_uint32),
        ('__origTickSeq', c_uint64),

        ('__origNetTime', STimespec32T),
        ('__recvTime', STimespec32T),
        ('__collectedTime', STimespec32T),
        ('__processedTime', STimespec32T),
        ('__pushingTime', STimespec32T),
    ]


class _Switch(BaseStructure):
    _fields_ = [
        ('switchFlag', c_uint8),
        ('switchStatus', c_uint8),
    ]


class MdsSecurityStatusMsgT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('__isRepeated', c_int8),
        ('__origMdSource', c_uint8),

        ('tradeDate', c_int32),
        ('updateTime', c_int32),
        ('__exchSendingTime', c_int32),
        ('__mdsRecvTime', c_int32),

        ('instrId', c_int32),

        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),

        ('FinancialStatus', c_char * MDS_MAX_FINANCIAL_STATUS_LEN),

        ('__filler2', c_uint8 * 2),
        ('__dataVersion', c_uint16),
        ('__filler', c_uint16),
        ('__origTickSeq', c_uint64),

        ('NoSwitch', c_int32),
        ('__filler4', c_int32),

        ('switches', _Switch * MDS_MAX_SECURITY_SWITCH_CNT),

        ('__origNetTime', STimespec32T),
        ('__recvTime', STimespec32T),
        ('__collectedTime', STimespec32T),
        ('__processedTime', STimespec32T),
        ('__pushingTime', STimespec32T),
    ]


class MdsPriceLevelEntryT(BaseStructure):
    _fields_ = [
        ('Price', c_int32),
        ('NumberOfOrders', c_int32),
        ('OrderQty', c_int64),
    ]


class MdsMktDataSnapshotHeadT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('__isRepeated', c_int8),
        ('__origMdSource', c_uint8),

        ('tradeDate', c_int32),
        ('updateTime', c_int32),

        ('instrId', c_int32),
        ('bodyLength', c_int16),
        ('bodyType', c_uint8),
        ('subStreamType', c_uint8),
        ('__channelNo', c_uint16),
        ('__dataVersion', c_uint16),
        ('__origTickSeq', c_uint32),
        ('__directSourceId', c_uint32),

        ('__origNetTime', STimespec32T),
        ('__recvTime', STimespec32T),
        ('__collectedTime', STimespec32T),
        ('__processedTime', STimespec32T),
        ('__pushingTime', STimespec32T),
    ]


class MdsIndexSnapshotBodyT(BaseStructure):
    _fields_ = [
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('TradingPhaseCode', c_char * MDS_MAX_TRADING_PHASE_CODE_LEN),
        ('__filler', c_char * 6),

        ('NumTrades', c_uint64),
        ('TotalVolumeTraded', c_uint64),
        ('TotalValueTraded', c_int64),

        ('PrevCloseIdx', c_int64),
        ('OpenIdx', c_int64),
        ('HighIdx', c_int64),
        ('LowIdx', c_int64),
        ('LastIdx', c_int64),
        ('CloseIdx', c_int64),

        ('StockNum', c_int32),
        ('__filler1', c_int32),
    ]


class MdsStockSnapshotBodyT(BaseStructure):
    _fields_ = [
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),

        ('TradingPhaseCode', c_char * MDS_MAX_TRADING_PHASE_CODE_LEN),
        ('__filler', c_char * 6),

        ('NumTrades', c_uint64),
        ('TotalVolumeTraded', c_uint64),
        ('TotalValueTraded', c_int64),

        ('PrevClosePx', c_int32),
        ('OpenPx', c_int32),
        ('HighPx', c_int32),
        ('LowPx', c_int32),
        ('TradePx', c_int32),
        ('ClosePx', c_int32),

        ('IOPV', c_int32),
        ('NAV', c_int32),
        ('TotalLongPosition', c_uint64),

        ('BidLevels', MdsPriceLevelEntryT * 5),
        ('OfferLevels', MdsPriceLevelEntryT * 5),
    ]


class MdsL1SnapshotBodyT(BaseUnion):
    _fields_ = [
        ('stock', MdsStockSnapshotBodyT),
        ('option', MdsStockSnapshotBodyT),
        ('index', MdsIndexSnapshotBodyT),
    ]


class _MdsL1SnapshotUnion(BaseUnion):
    _fields_ = [
        ('stock', MdsStockSnapshotBodyT),
        ('option', MdsStockSnapshotBodyT),
        ('index', MdsIndexSnapshotBodyT),
    ]


class MdsL1SnapshotT(BaseStructure):
    _fields_ = [
        ('head', MdsMktDataSnapshotHeadT),
        ('union', _MdsL1SnapshotUnion),
    ]


class MdsL2StockSnapshotBodyT(BaseStructure):
    _fields_ = [
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),

        ('TradingPhaseCode', c_char * MDS_MAX_TRADING_PHASE_CODE_LEN),
        ('__filler', c_char * 6),

        ('NumTrades', c_uint64),
        ('TotalVolumeTraded', c_uint64),
        ('TotalValueTraded', c_int64),

        ('PrevClosePx', c_int32),
        ('OpenPx', c_int32),
        ('HighPx', c_int32),
        ('LowPx', c_int32),
        ('TradePx', c_int32),
        ('ClosePx', c_int32),

        ('IOPV', c_int32),
        ('NAV', c_int32),
        ('TotalLongPosition', c_uint64),

        ('TotalBidQty', c_int64),
        ('TotalOfferQty', c_int64),
        ('WeightedAvgBidPx', c_int32),
        ('WeightedAvgOfferPx', c_int32),

        ('BidPriceLevel', c_int32),
        ('OfferPriceLevel', c_int32),

        ('BidLevels', MdsPriceLevelEntryT * 10),
        ('OfferLevels', MdsPriceLevelEntryT * 10),
    ]


class MdsL2StockSnapshotIncrementalT(BaseStructure):
    _fields_ = [
        ('NumTrades', c_uint64),
        ('TotalVolumeTraded', c_uint64),
        ('TotalValueTraded', c_int64),

        ('OpenPx', c_int32),
        ('HighPx', c_int32),
        ('LowPx', c_int32),
        ('TradePx', c_int32),
        ('ClosePx', c_int32),
        ('IOPV', c_int32),

        ('TotalBidQty', c_int64),
        ('TotalOfferQty', c_int64),
        ('WeightedAvgBidPx', c_int32),
        ('WeightedAvgOfferPx', c_int32),
        ('BidPriceLevel', c_int32),
        ('OfferPriceLevel', c_int32),

        ('BestBidPrice', c_int32),
        ('HasContainedBestBidLevel', c_uint8),
        ('NoBidLevel', c_uint8),
        ('__hasDeletedAtBidTail', c_uint8),
        ('__filler1', c_uint8),

        ('BestOfferPrice', c_int32),
        ('HasContainedBestOfferLevel', c_uint8),
        ('NoOfferLevel', c_uint8),
        ('__hasDeletedAtOfferTail', c_uint8),
        ('__filler2', c_uint8),

        ('PriceLevelOperator', c_uint8 * MDS_MAX_L2_PRICE_LEVEL_INCREMENTS),
        ('PriceLevels', MdsPriceLevelEntryT * MDS_MAX_L2_PRICE_LEVEL_INCREMENTS),
    ]


class MdsL2BestOrdersSnapshotBodyT(BaseStructure):
    _fields_ = [
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('__filler', c_uint8 * 5),
        ('NoBidOrders', c_uint8),
        ('NoOfferOrders', c_uint8),

        ('TotalVolumeTraded', c_uint64),
        ('BestBidPrice', c_int32),
        ('BestOfferPrice', c_int32),

        ('BidOrderQty', c_int32 * MDS_MAX_L2_DISCLOSE_ORDERS_CNT),
        ('OfferOrderQty', c_int32 * MDS_MAX_L2_DISCLOSE_ORDERS_CNT),
    ]


class MdsL2BestOrdersSnapshotIncrementalT(BaseStructure):
    _fields_ = [
        ('TotalVolumeTraded', c_uint64),

        ('BestBidPrice', c_int32),
        ('HasContainedBestBidLevel', c_uint8),
        ('ContinualDeletedBidOrders', c_uint8),
        ('NoBidOrders', c_uint8),
        ('__filler1', c_uint8),

        ('BestOfferPrice', c_int32),
        ('HasContainedBestOfferLevel', c_uint8),
        ('ContinualDeletedOfferOrders', c_uint8),
        ('NoOfferOrders', c_uint8),
        ('__filler2', c_uint8),

        ('OperatorEntryID', c_int8 * MDS_MAX_L2_DISCLOSE_ORDERS_INCREMENTS),
        ('OrderQty', c_int32 * MDS_MAX_L2_DISCLOSE_ORDERS_INCREMENTS),
    ]


class MdsL2MarketOverviewT(BaseStructure):
    _fields_ = [
        ('OrigDate', c_int32),
        ('OrigTime', c_int32),
        ('__exchSendingTime', c_int32),
        ('__mdsRecvTime', c_int32),
    ]


class MdsL2SnapshotBodyT(BaseUnion):
    _fields_ = [
        ('l2Stock', MdsL2StockSnapshotBodyT),
        ('l2StockIncremental', MdsL2StockSnapshotIncrementalT),
        ('l2BestOrders', MdsL2BestOrdersSnapshotBodyT),
        ('l2BestOrdersIncremental', MdsL2BestOrdersSnapshotIncrementalT),
        ('option', MdsStockSnapshotBodyT),
        ('index', MdsIndexSnapshotBodyT),
        ('l2MarketOverview', MdsL2MarketOverviewT),
    ]


class _MdsMktDataSnapshotUnion(BaseUnion):
    _fields_ = [
        ('l2Stock', MdsL2StockSnapshotBodyT),
        ('l2StockIncremental', MdsL2StockSnapshotIncrementalT),
        ('l2BestOrders', MdsL2BestOrdersSnapshotBodyT),
        ('l2BestOrdersIncremental', MdsL2BestOrdersSnapshotIncrementalT),
        ('stock', MdsStockSnapshotBodyT),
        ('option', MdsStockSnapshotBodyT),
        ('index', MdsIndexSnapshotBodyT),
        ('l2MarketOverview', MdsL2MarketOverviewT),
    ]


class MdsMktDataSnapshotT(BaseStructure):
    _fields_ = [
        ('head', MdsMktDataSnapshotHeadT),
        ('union', _MdsMktDataSnapshotUnion),
    ]


DATASIZE_MDS_L2_STOCK_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsL2StockSnapshotBodyT))
DATASIZE_MDS_L2_BEST_ORDERS_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsL2BestOrdersSnapshotBodyT))
DATASIZE_MDS_STOCK_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsStockSnapshotBodyT))
DATASIZE_MDS_OPTION_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsStockSnapshotBodyT))
DATASIZE_MDS_INDEX_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsIndexSnapshotBodyT))
DATASIZE_MDS_L2_MARKET_OVERVIEW = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsL2MarketOverviewT))


class MdsL2TradeT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('__isRepeated', c_int8),
        ('__origMdSource', c_uint8),

        ('tradeDate', c_int32),
        ('TransactTime', c_int32),

        ('instrId', c_int32),
        ('ChannelNo', c_uint16),
        ('__reserve', c_uint16),
        ('ApplSeqNum', c_int32),

        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('ExecType', c_char),
        ('TradeBSFlag', c_char),
        ('subStreamType', c_uint8),

        ('SseBizIndex', c_uint32),
        ('__filler', c_uint64),

        ('TradePrice', c_int32),
        ('TradeQty', c_int32),
        ('TradeMoney', c_int64),

        ('BidApplSeqNum', c_int64),
        ('OfferApplSeqNum', c_int64),

        ('__origNetTime', STimespec32T),
        ('__recvTime', STimespec32T),
        ('__collectedTime', STimespec32T),
        ('__processedTime', STimespec32T),
        ('__pushingTime', STimespec32T),
    ]


class MdsL2OrderT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('__isRepeated', c_int8),
        ('__origMdSource', c_uint8),

        ('tradeDate', c_int32),
        ('TransactTime', c_int32),

        ('instrId', c_int32),
        ('ChannelNo', c_uint16),
        ('__reserve', c_uint16),
        ('ApplSeqNum', c_int32),

        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('Side', c_char),
        ('OrderType', c_char),
        ('subStreamType', c_uint8),

        ('SseBizIndex', c_uint32),
        ('SseOrderNo', c_int64),
        ('Price', c_int32),
        ('OrderQty', c_int32),

        ('__origNetTime', STimespec32T),
        ('__recvTime', STimespec32T),
        ('__collectedTime', STimespec32T),
        ('__processedTime', STimespec32T),
        ('__pushingTime', STimespec32T),
    ]


class MdsWholeMktMsgBodyT(BaseUnion):
    _fields_ = [
        ('mktDataSnapshot', MdsMktDataSnapshotT),
        ('trade', MdsL2TradeT),
        ('order', MdsL2OrderT),
        ('trdSessionStatus', MdsTradingSessionStatusMsgT),
        ('securityStatus', MdsSecurityStatusMsgT),
    ]


class MdsStockStaticInfoT(BaseStructure):
    _fields_ = [
        ('securityId', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('oesSecurityType', c_uint8),
        ('subSecurityType', c_uint8),
        ('currType', c_uint8),
        ('qualificationClass', c_uint8),
        ('__filler1', c_uint8 * 5),
        ('instrId', c_int32),

        ('securityStatus', c_uint32),
        ('securityAttribute', c_uint32),

        ('suspFlag', c_uint8),
        ('isDayTrading', c_uint8),
        ('isRegistration', c_uint8),
        ('isCrdCollateral', c_uint8),
        ('isCrdMarginTradeUnderlying', c_uint8),
        ('isCrdShortSellUnderlying', c_uint8),
        ('isNoProfit', c_uint8),
        ('isWeightedVotingRights', c_uint8),
        ('isVie', c_uint8),
        ('pricingMethod', c_uint8),
        ('__filler2', c_uint8 * 6),

        ('upperLimitPrice', c_int32),
        ('lowerLimitPrice', c_int32),
        ('priceTick', c_int32),
        ('prevClose', c_int32),

        ('lmtBuyMaxQty', c_int32),
        ('lmtBuyMinQty', c_int32),
        ('lmtBuyQtyUnit', c_int32),
        ('mktBuyQtyUnit', c_int32),
        ('mktBuyMaxQty', c_int32),
        ('mktBuyMinQty', c_int32),

        ('lmtSellMaxQty', c_int32),
        ('lmtSellMinQty', c_int32),
        ('lmtSellQtyUnit', c_int32),
        ('mktSellQtyUnit', c_int32),
        ('mktSellMaxQty', c_int32),
        ('mktSellMinQty', c_int32),

        ('bondInterest', c_int64),
        ('parValue', c_int64),

        ('auctionLimitType', c_uint8),
        ('auctionReferPriceType', c_uint8),
        ('__filler3', c_uint8 * 2),
        ('auctionUpDownRange', c_int32),

        ('listDate', c_int32),
        ('maturityDate', c_int32),
        ('outstandingShare', c_int64),
        ('publicFloatShare', c_int64),

        ('underlyingSecurityId', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('__filler4', c_uint8 * 7),
        ('securityName', c_char * MDS_MAX_SECURITY_NAME_LEN),
        ('securityLongName', c_char * MDS_MAX_SECURITY_LONG_NAME_LEN),
        ('securityEnglishName', c_char * MDS_MAX_SECURITY_ENGLISH_NAME_LEN),
        ('securityIsinCode', c_char * MDS_MAX_SECURITY_ISIN_CODE_LEN),
        ('__reserve1', c_char * 24),
        ('__reserve2', c_char * 64),
    ]


class MdsOptionStaticInfoT(BaseStructure):
    _fields_ = [
        ('securityId', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('oesSecurityType', c_uint8),
        ('subSecurityType', c_uint8),
        ('contractType', c_uint8),
        ('exerciseType', c_uint8),
        ('deliveryType', c_uint8),
        ('__filler1', c_uint8 * 4),
        ('instrId', c_int32),

        ('contractUnit', c_int32),
        ('exercisePrice', c_int32),
        ('deliveryDate', c_int32),
        ('deliveryMonth', c_int32),

        ('listDate', c_int32),
        ('lastTradeDay', c_int32),
        ('exerciseBeginDate', c_int32),
        ('exerciseEndDate', c_int32),

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
        ('contractId', c_char * MDS_MAX_CONTRACT_EXCH_ID_LEN),
        ('securityName', c_char * MDS_MAX_CONTRACT_SYMBOL_LEN),
        ('underlyingSecurityId', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('__filler2', c_uint8 * 7),

        ('__reserve', c_char * 16),
    ]
