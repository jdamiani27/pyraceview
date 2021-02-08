from ..messages import MsgHeader
from dataclasses import dataclass


@dataclass
class MsgBase:
    header: MsgHeader

    def __init__(self, msg_bytes: bytes):
        self.header = MsgHeader(msg_bytes)
