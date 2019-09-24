from ..messages import MsgBase


class MsgHeartbeat(MsgBase):
    def __init__(self, msg_bytes):
        super().__init__(msg_bytes)
