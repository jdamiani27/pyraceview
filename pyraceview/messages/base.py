from ..messages import MsgHeader


class MsgBase:
    def __init__(self, msg_bytes):
        self._header = MsgHeader(msg_bytes)

    @property
    def header(self):
        return self._header
