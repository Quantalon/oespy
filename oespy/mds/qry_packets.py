from ..spk.types import SPK_MAX_PATH_LEN
from ..utils import BaseStructure
from ..utils.types import *
from .base_model import (MDS_MAX_POSTFIXED_INSTR_CODE_LEN, MDS_MAX_IP_LEN, MDS_APPL_UPGRADE_PROTOCOL_MAX_LEN,
                         MDS_MAX_USERNAME_LEN, MDS_MAX_PASSWORD_LEN, MDS_MAX_COMP_ID_LEN, MDS_VER_ID_MAX_LEN,
                         MDS_APPL_DISCARD_VERSION_MAX_COUNT, MDS_CLIENT_TAG_MAX_LEN)
from .base_model import MdsStockStaticInfoT, MdsL1SnapshotT, MdsOptionStaticInfoT


MDS_QRYRSP_MAX_STOCK_CNT = 100


class MdsQryMktDataSnapshotReqT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('__filler', c_uint8 * 2),
        ('instrId', c_int32),
    ]


MdsQrySecurityStatusReqT = MdsQryMktDataSnapshotReqT


class MdsQryTrdSessionStatusReqT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('__filler', c_uint8 * 6),
    ]


class MdsQryReqHeadT(BaseStructure):
    _fields_ = [
        ('maxPageSize', c_int32),
        ('lastPosition', c_int32),
    ]


class MdsQryRspHeadT(BaseStructure):
    _fields_ = [
        ('itemCount', c_int32),
        ('lastPosition', c_int32),
        ('isEnd', c_int8),
        ('__filler', c_uint8 * 7),
        ('userInfo', c_int64),
    ]


class MdsQryCursorT(BaseStructure):
    _fields_ = [
        ('seqNo', c_int32),
        ('isEnd', c_int8),
        ('__filler', c_int8 * 3),
        ('userInfo', c_int64),
    ]


class MdsQrySecurityCodeEntryT(BaseStructure):
    _fields_ = [
        ('instrId', c_int32),
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('__filler', c_uint8 * 2),
    ]


class MdsQryStockStaticInfoFilterT(BaseStructure):
    _fields_ = [
        ('securityId', c_char * MDS_MAX_POSTFIXED_INSTR_CODE_LEN),
        ('exchId', c_uint8),
        ('oesSecurityType', c_uint8),
        ('subSecurityType', c_uint8),
        ('__filler', c_uint8 * 5),
        ('instrId', c_int32),
        ('userInfo', c_int64),
    ]


class MdsQryStockStaticInfoReqT(BaseStructure):
    _fields_ = [
        ('reqHead', MdsQryReqHeadT),
        ('qryFilter', MdsQryStockStaticInfoFilterT),
    ]


class MdsQryStockStaticInfoRspT(BaseStructure):
    _fields_ = [
        ('rspHead', MdsQryRspHeadT),
        ('qryItems', MdsStockStaticInfoT * 1),
    ]


class MdsQryOptionStaticInfoFilterT(BaseStructure):
    _fields_ = [
        ('securityId', c_char * MDS_MAX_POSTFIXED_INSTR_CODE_LEN),
        ('exchId', c_uint8),
        ('oesSecurityType', c_uint8),
        ('subSecurityType', c_uint8),
        ('__filler', c_uint8 * 5),
        ('instrId', c_int32),
        ('userInfo', c_int64),
    ]


class MdsQryOptionStaticInfoReqT(BaseStructure):
    _fields_ = [
        ('reqHead', MdsQryReqHeadT),
        ('qryFilter', MdsQryOptionStaticInfoFilterT),
    ]


class MdsQryOptionStaticInfoRspT(BaseStructure):
    _fields_ = [
        ('rspHead', MdsQryRspHeadT),
        ('qryItems', MdsOptionStaticInfoT * 1),
    ]


class MdsQryStockStaticInfoListFilterT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('oesSecurityType', c_uint8),
        ('subSecurityType', c_uint8),
        ('__filler', c_uint8 * 5),
        ('userInfo', c_int64),
    ]


class MdsQryStockStaticInfoListReqT(BaseStructure):
    _fields_ = [
        ('reqHead', MdsQryReqHeadT),
        ('qryFilter', MdsQryStockStaticInfoListFilterT),
        ('securityCodeCnt', c_int32),
        ('__filler', c_int32),
        ('securityCodeList', MdsQrySecurityCodeEntryT * 1),
    ]


class MdsQryStockStaticInfoListRspT(BaseStructure):
    _fields_ = [
        ('rspHead', MdsQryRspHeadT),
        ('qryItems', MdsStockStaticInfoT * 1),
    ]


MdsQryOptionStaticInfoListFilterT = MdsQryStockStaticInfoListFilterT

MdsQryOptionStaticInfoListReqT = MdsQryStockStaticInfoListReqT


class MdsQryOptionStaticInfoListRspT(BaseStructure):
    _fields_ = [
        ('rspHead', MdsQryRspHeadT),
        ('qryItems', MdsOptionStaticInfoT * 1),
    ]


class MdsQrySnapshotListFilterT(BaseStructure):
    _fields_ = [
        ('exchId', c_uint8),
        ('mdProductType', c_uint8),
        ('oesSecurityType', c_uint8),
        ('subSecurityType', c_uint8),
        ('mdLevel', c_uint8),
        ('__filler', c_uint8 * 11),
        ('userInfo', c_int64),
    ]


class MdsQrySnapshotListReqT(BaseStructure):
    _fields_ = [
        ('reqHead', MdsQryReqHeadT),
        ('qryFilter', MdsQrySnapshotListFilterT),
        ('securityCodeCnt', c_int32),
        ('__filler', c_int32),
        ('securityCodeList', MdsQrySecurityCodeEntryT * 1),
    ]


class MdsQrySnapshotListRspT(BaseStructure):
    _fields_ = [
        ('rspHead', MdsQryRspHeadT),
        ('qryItems', MdsL1SnapshotT * 1),
    ]


class MdsApplUpgradeSourceT(BaseStructure):
    _fields_ = [
        ('ipAddress', c_char * MDS_MAX_IP_LEN),
        ('protocol', c_char * MDS_APPL_UPGRADE_PROTOCOL_MAX_LEN),
        ('username', c_char * MDS_MAX_USERNAME_LEN),
        ('password', c_char * MDS_MAX_PASSWORD_LEN),
        ('encryptMethod', c_int32),
        ('__filler', c_int32),
        ('homePath', c_char * SPK_MAX_PATH_LEN),
        ('fileName', c_char * SPK_MAX_PATH_LEN),
    ]


class MdsApplUpgradeItemT(BaseStructure):
    _fields_ = [
        ('applName', c_char * MDS_MAX_COMP_ID_LEN),
        ('minApplVerId', c_char * MDS_VER_ID_MAX_LEN),
        ('maxApplVerId', c_char * MDS_VER_ID_MAX_LEN),
        ('discardApplVerId', c_char * MDS_VER_ID_MAX_LEN * MDS_APPL_DISCARD_VERSION_MAX_COUNT),
        ('discardVerCount', c_int32),
        ('newApplVerDate', c_int32),
        ('newApplVerId', c_char * MDS_VER_ID_MAX_LEN),
        ('newApplVerTag', c_char * MDS_CLIENT_TAG_MAX_LEN),
        ('primarySource', MdsApplUpgradeSourceT),
        ('secondarySource', MdsApplUpgradeSourceT),
    ]


class MdsApplUpgradeInfoT(BaseStructure):
    _fields_ = [
        ('clientUpgradeInfo', MdsApplUpgradeItemT),
        ('cApiUpgradeInfo', MdsApplUpgradeItemT),
        ('javaApiUpgradeInfo', MdsApplUpgradeItemT),
    ]


class MdsQryApplUpgradeInfoRspT(BaseStructure):
    _fields_ = [
        ('applUpgradeInfo', MdsApplUpgradeInfoT),
    ]
