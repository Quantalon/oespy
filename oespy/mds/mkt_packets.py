from enum import Enum

from ..spk.types import STimespec32T
from ..utils import BaseStructure, BaseUnion
from ..utils.types import *
from .base_model import (MDS_MAX_SECURITY_CNT_PER_SUBSCRIBE, MDS_MAX_TEST_REQ_ID_LEN, MDS_MAX_SENDING_TIME_LEN,
                         MDS_MAX_USERNAME_LEN, MDS_MAX_PASSWORD_LEN)
from .base_model import (MdsMktDataSnapshotT, MdsL2TradeT, MdsL2OrderT, MdsTradingSessionStatusMsgT,
                         MdsSecurityStatusMsgT)
from .qry_packets import (MdsQryMktDataSnapshotReqT, MdsQrySecurityStatusReqT, MdsQryTrdSessionStatusReqT,
                          MdsQryStockStaticInfoReqT, MdsQryOptionStaticInfoReqT, MdsQryStockStaticInfoListReqT,
                          MdsQryOptionStaticInfoListReqT, MdsQrySnapshotListReqT, MdsQryStockStaticInfoRspT,
                          MdsQryOptionStaticInfoRspT, MdsQryStockStaticInfoListRspT, MdsQryOptionStaticInfoListRspT,
                          MdsQrySnapshotListRspT, MdsQryApplUpgradeInfoRspT)


MDS_APPL_VER_ID = "0.17.6.3"
MDS_APPL_VER_VALUE = 1001706031
MDS_MIN_APPL_VER_ID = "0.15.5"
MDS_APPL_NAME = "MDS"


class eMdsMsgTypeT(Enum):
    MDS_MSGTYPE_HEARTBEAT = 1
    MDS_MSGTYPE_TEST_REQUEST = 2
    MDS_MSGTYPE_LOGOUT = 4
    MDS_MSGTYPE_MARKET_DATA_REQUEST = 5
    MDS_MSGTYPE_COMPRESSED_PACKETS = 6

    MDS_MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH = 10
    MDS_MSGTYPE_INDEX_SNAPSHOT_FULL_REFRESH = 11
    MDS_MSGTYPE_OPTION_SNAPSHOT_FULL_REFRESH = 12
    MDS_MSGTYPE_TRADING_SESSION_STATUS = 13
    MDS_MSGTYPE_SECURITY_STATUS = 14

    MDS_MSGTYPE_L2_MARKET_DATA_SNAPSHOT = 20
    MDS_MSGTYPE_L2_BEST_ORDERS_SNAPSHOT = 21
    MDS_MSGTYPE_L2_TRADE = 22
    MDS_MSGTYPE_L2_ORDER = 23
    MDS_MSGTYPE_L2_SSE_ORDER = 28
    MDS_MSGTYPE_L2_MARKET_DATA_INCREMENTAL = 24
    MDS_MSGTYPE_L2_BEST_ORDERS_INCREMENTAL = 25
    MDS_MSGTYPE_L2_MARKET_OVERVIEW = 26
    MDS_MSGTYPE_L2_VIRTUAL_AUCTION_PRICE = 27

    MDS_MSGTYPE_CMD_CHANGE_PASSWORD = 60

    MDS_MSGTYPE_QRY_MARKET_DATA_SNAPSHOT = 80
    MDS_MSGTYPE_QRY_SECURITY_STATUS = 81
    MDS_MSGTYPE_QRY_TRADING_SESSION_STATUS = 82
    MDS_MSGTYPE_QRY_SNAPSHOT_LIST = 86
    MDS_MSGTYPE_QRY_OPTION_STATIC_INFO = 87
    MDS_MSGTYPE_QRY_STOCK_STATIC_INFO = 88
    MDS_MSGTYPE_QRY_STOCK_STATIC_INFO_LIST = 89
    MDS_MSGTYPE_QRY_OPTION_STATIC_INFO_LIST = 90


class eMdsSubscribeModeT(Enum):
    MDS_SUB_MODE_SET = 0
    MDS_SUB_MODE_APPEND = 1
    MDS_SUB_MODE_DELETE = 2

    MDS_SUB_MODE_BATCH_BEGIN = 10
    MDS_SUB_MODE_BATCH_APPEND = 11
    MDS_SUB_MODE_BATCH_DELETE = 12
    MDS_SUB_MODE_BATCH_END = 13


class eMdsMktSubscribeFlagT(Enum):
    MDS_MKT_SUB_FLAG_DEFAULT = 0
    MDS_MKT_SUB_FLAG_ALL = 1
    MDS_MKT_SUB_FLAG_DISABLE = 2


class eMdsSubscribedTickTypeT(Enum):
    MDS_TICK_TYPE_LATEST_SIMPLIFIED = 0
    MDS_TICK_TYPE_LATEST_TIMELY = 1
    MDS_TICK_TYPE_ALL_INCREMENTS = 2


class eMdsSubscribedTickExpireTypeT(Enum):
    MDS_TICK_EXPIRE_TYPE_NONE = 0
    MDS_TICK_EXPIRE_TYPE_IMMEDIATE = 1
    MDS_TICK_EXPIRE_TYPE_TIMELY = 2
    MDS_TICK_EXPIRE_TYPE_TIMEOUT = 3


class eMdsSubscribedTickRebuildFlagT(Enum):
    MDS_TICK_REBUILD_FLAG_EXCLUDE_REBUILDED = 0
    MDS_TICK_REBUILD_FLAG_INCLUDE_REBUILDED = 1
    MDS_TICK_REBUILD_FLAG_ONLY_REBUILDED = 2


class eMdsSubscribeDataTypeT(Enum):
    MDS_SUB_DATA_TYPE_DEFAULT = 0
    MDS_SUB_DATA_TYPE_L1_SNAPSHOT = 0x0001
    MDS_SUB_DATA_TYPE_L2_SNAPSHOT = 0x0002
    MDS_SUB_DATA_TYPE_L2_BEST_ORDERS = 0x0004
    MDS_SUB_DATA_TYPE_L2_TRADE = 0x0008
    MDS_SUB_DATA_TYPE_L2_ORDER = 0x0010
    MDS_SUB_DATA_TYPE_L2_SSE_ORDER = 0x0020
    MDS_SUB_DATA_TYPE_L2_MARKET_OVERVIEW = 0x0040
    MDS_SUB_DATA_TYPE_TRADING_SESSION_STATUS = 0x0100
    MDS_SUB_DATA_TYPE_SECURITY_STATUS = 0x0200
    MDS_SUB_DATA_TYPE_INDEX_SNAPSHOT = 0x0400
    MDS_SUB_DATA_TYPE_OPTION_SNAPSHOT = 0x0800
    MDS_SUB_DATA_TYPE_NONE = 0x8000
    MDS_SUB_DATA_TYPE_ALL = 0xFFFF


class eMdsTickChannelNoT(Enum):
    MDS_CHANNEL_NO_DEFAULT = 0
    MDS_CHANNEL_NO_ONE = 0x01
    MDS_CHANNEL_NO_TWO = 0x02
    MDS_CHANNEL_NO_THREE = 0x04
    MDS_CHANNEL_NO_FOUR = 0x08
    MDS_CHANNEL_NO_ALL = 0x0F
    MDS_CHANNEL_NO_NONE = 0x80


class MdsMktDataRequestEntryT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('__filler', c_uint8 * 2),
        ('instrId', c_int32),
    ]


class MdsMktDataRequestReqT(BaseStructure):
    _fields_ = [
        ('subMode', c_uint8),
        ('tickType', c_uint8),
        ('sseStockFlag', c_int8),
        ('sseIndexFlag', c_int8),
        ('sseOptionFlag', c_int8),
        ('szseStockFlag', c_int8),
        ('szseIndexFlag', c_int8),
        ('szseOptionFlag', c_int8),
        ('isRequireInitialMktData', c_uint8),
        ('__channelNos', c_uint8),
        ('tickExpireType', c_uint8),
        ('tickRebuildFlag', c_uint8),
        ('dataTypes', c_int32),
        ('beginTime', c_int32),
        ('subSecurityCnt', c_int32),
    ]


class MdsMktDataRequestReqBufT(BaseStructure):
    _fields_ = [
        ('mktDataRequestReq', MdsMktDataRequestReqT),
        ('entries', MdsMktDataRequestEntryT * MDS_MAX_SECURITY_CNT_PER_SUBSCRIBE),
    ]


class MdsMktDataRequestRspT(BaseStructure):
    _fields_ = [
        ('subMode', c_uint8),
        ('tickType', c_uint8),
        ('isRequireInitialMktData', c_uint8),
        ('__channelNos', c_uint8),
        ('tickExpireType', c_uint8),
        ('tickRebuildFlag', c_uint8),
        ('__filler', c_uint8 * 2),
        ('dataTypes', c_int32),
        ('beginTime', c_int32),
        ('sseStockSubscribed', c_int32),
        ('sseIndexSubscribed', c_int32),
        ('sseOptionSubscribed', c_int32),
        ('szseStockSubscribed', c_int32),
        ('szseIndexSubscribed', c_int32),
        ('szseOptionSubscribed', c_int32),
    ]


class MdsTestRequestReqT(BaseStructure):
    _fields_ = [
        ('testReqId', c_char * MDS_MAX_TEST_REQ_ID_LEN),
        ('sendTime', c_char * MDS_MAX_SENDING_TIME_LEN),
        ('__filler', c_char * 2),
    ]


class MdsTestRequestRspT(BaseStructure):
    _fields_ = [
        ('testReqId', c_char * MDS_MAX_TEST_REQ_ID_LEN),
        ('origSendTime', c_char * MDS_MAX_SENDING_TIME_LEN),
        ('__filler1', c_char * 2),
        ('respTime', c_char * MDS_MAX_SENDING_TIME_LEN),
        ('__filler2', c_char * 2),
        ('__recvTime', STimespec32T),
        ('__collectedTime', STimespec32T),
        ('__pushingTime', STimespec32T),
    ]


class _UserInfo(BaseUnion):
    _fields_ = [
        ('u64', c_uint64),
        ('i64', c_int64),
        ('u32', c_uint32 * 2),
        ('i32', c_int32 * 2),
        ('c8', c_char * 8),
    ]


class MdsChangePasswordReqT(BaseStructure):
    _fields_ = [
        ('encryptMethod', c_int32),
        ('__filler', c_int32),
        ('username', c_char * MDS_MAX_USERNAME_LEN),
        ('userInfo', _UserInfo),
        ('oldPassword', c_char * MDS_MAX_PASSWORD_LEN),
        ('newPassword', c_char * MDS_MAX_PASSWORD_LEN),
    ]


class MdsChangePasswordRspT(BaseStructure):
    _fields_ = [
        ('encryptMethod', c_int32),
        ('__filler', c_int32),
        ('username', c_char * MDS_MAX_USERNAME_LEN),
        ('userInfo', _UserInfo),
        ('__filler2', c_int32),
        ('transDate', c_int32),
        ('transTime', c_int32),
        ('rejReason', c_int32),
    ]


class MdsMktReqMsgBodyT(BaseUnion):
    _fields_ = [
        ('wholeMktDataReqBuf', MdsMktDataRequestReqBufT),
        ('mktDataRequestReq', MdsMktDataRequestReqT),
        ('testRequestReq', MdsTestRequestReqT),
        ('qryMktDataSnapshotReq', MdsQryMktDataSnapshotReqT),
        ('qrySecurityStatusReq', MdsQrySecurityStatusReqT),
        ('qryTrdSessionStatusReq', MdsQryTrdSessionStatusReqT),
        ('qryStockStaticInfoReq', MdsQryStockStaticInfoReqT),
        ('qryOptionStaticInfoReq', MdsQryOptionStaticInfoReqT),
        ('qryStockStaticInfoListReq', MdsQryStockStaticInfoListReqT),
        ('qryOptionStaticInfoListReq', MdsQryOptionStaticInfoListReqT),
        ('qrySnapshotListReq', MdsQrySnapshotListReqT),
        ('changePasswordReq', MdsChangePasswordReqT),
    ]


class MdsMktRspMsgBodyT(BaseUnion):
    _fields_ = [
        ('mktDataRequestRsp', MdsMktDataRequestRspT),
        ('testRequestRsp', MdsTestRequestRspT),

        ('mktDataSnapshot', MdsMktDataSnapshotT),
        ('trade', MdsL2TradeT),
        ('order', MdsL2OrderT),

        ('trdSessionStatus', MdsTradingSessionStatusMsgT),
        ('securityStatus', MdsSecurityStatusMsgT),

        ('qryStockStaticInfoRsp', MdsQryStockStaticInfoRspT),
        ('qryOptionStaticInfoRsp', MdsQryOptionStaticInfoRspT),
        ('qryStockStaticInfoListRsp', MdsQryStockStaticInfoListRspT),
        ('qryOptionStaticInfoListRsp', MdsQryOptionStaticInfoListRspT),
        ('qrySnapshotListRsp', MdsQrySnapshotListRspT),
        ('qryApplUpgradeInfoRsp', MdsQryApplUpgradeInfoRspT),

        ('changePasswordRsp', MdsChangePasswordRspT),
    ]
