from ctypes import cast, POINTER

from oespy import MdsApi, eMdsMsgTypeT, MdsMktRspMsgBodyT


def handle_msg(tcp_channel, msg_head, msg_item, callback_params):
    msg_id = msg_head.contents.msgId

    try:
        msg_type = eMdsMsgTypeT(msg_id)
    except ValueError:
        print('Unknown Msg Type...')
        return 0

    rsp_msg = cast(msg_item, POINTER(MdsMktRspMsgBodyT))[0]
    match msg_type:
        case eMdsMsgTypeT.MDS_MSGTYPE_L2_TRADE:
            trade = rsp_msg.trade
            print(f'Recv Lv2 TickTrade: {trade.exchId=} {trade.SecurityID=} {trade.TradePrice=} {trade.TradeQty=}')
        case eMdsMsgTypeT.MDS_MSGTYPE_L2_ORDER | eMdsMsgTypeT.MDS_MSGTYPE_L2_SSE_ORDER:
            order = rsp_msg.order
            print(f'Recv Lv2 TickOrder: {order.exchId=} {order.SecurityID=} {order.Price=} {order.OrderQty=}')
        case eMdsMsgTypeT.MDS_MSGTYPE_L2_MARKET_DATA_SNAPSHOT:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_L2_BEST_ORDERS_SNAPSHOT:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_L2_MARKET_DATA_INCREMENTAL:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_L2_BEST_ORDERS_INCREMENTAL:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_L2_MARKET_OVERVIEW:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_OPTION_SNAPSHOT_FULL_REFRESH:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_INDEX_SNAPSHOT_FULL_REFRESH:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_SECURITY_STATUS:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_TRADING_SESSION_STATUS:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_MARKET_DATA_REQUEST:
            status = msg_head.contents.status
            if status == 0:
                ...
            else:
                ...
        case eMdsMsgTypeT.MDS_MSGTYPE_TEST_REQUEST:
            ...
        case eMdsMsgTypeT.MDS_MSGTYPE_HEARTBEAT:
            print('HEARTBEAT...')
        case eMdsMsgTypeT.MDS_MSGTYPE_COMPRESSED_PACKETS:
            ...
        case _:
            pass
    return 0


def main():
    config_file_name = './mds_client.conf'
    timeout_ms = 1000

    mds_api = MdsApi()

    print(f'{mds_api.MdsApi_GetApiVersion()=}')

    if not mds_api.MdsApi_CheckApiVersion():
        print('API的头文件版本与库文件版本不匹配')
        return

    if not mds_api.MdsApi_InitAll(config_file_name):
        print('初始化客户端环境失败')
        mds_api.MdsApi_DestoryAll()
        return






if __name__ == '__main__':
    main()
