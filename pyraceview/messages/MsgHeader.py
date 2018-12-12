from ..util import ByteArray


class MsgHeader(object):

    def __init__(self, msg_bytes):
        msg_ba = ByteArray(msg_bytes)
        self._sync = msg_ba.read_unsigned_short()
        self._clock = msg_ba.read_unsigned_short()
        self._size = msg_ba.read_unsigned_short()
        self._byteType = chr(msg_ba.read_unsigned_byte())

    @property
    def sync(self):
        return self._sync

    @property
    def clock(self):
        return self._clock

    @property
    def size(self):
        return self._size

    @property
    def byteType(self):
        return self._byteType
