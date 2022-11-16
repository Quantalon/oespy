from ctypes import cast, POINTER

from oespy import MdsApi, MdsMktRspMsgBodyT, eMdsMsgTypeT


def on_msg(tcp_channel, msg_head, msg_item, callback_params):

    msg_id = msg_head.contents.msgId
    rsp_msg = cast(msg_item, POINTER(MdsMktRspMsgBodyT))[0]

    if msg_id == eMdsMsgTypeT.MDS_MSGTYPE_L2_SSE_ORDER.value:
        print('Recv Lv2 TickOrder')
        print(f'{rsp_msg.order.exchId=}')
        print(f'{rsp_msg.order.SecurityID=}')
        print(f'{rsp_msg.order.Price=}')
        print(f'{rsp_msg.order.OrderQty=}')

    # other types

    return 0


def main():
    mds = MdsApi()
    timeout_ms = 1000
    if mds.MdsApi_InitAll('./mds_client.conf'):
        print('MDS登录成功')
        mds.MdsApi_WaitOnMsg(timeout_ms, on_msg, None)
    mds.MdsApi_DestoryAll()


if __name__ == '__main__':
    main()
