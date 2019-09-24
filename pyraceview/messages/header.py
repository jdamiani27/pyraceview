from ..util import ByteArray


class MsgHeader(object):
    def __init__(self, msg_bytes):
        msg_ba = ByteArray(msg_bytes)
        self._sync = int(msg_ba.read_unsigned_short())
        self._clock = int(msg_ba.read_unsigned_short())
        self._size = int(msg_ba.read_unsigned_short())
        self._byte_type = chr(msg_ba.read_unsigned_byte())

    def __str__(self):
        return "Sync: {}, Clock: {}, Size: {}, Type: {}".format(
            self.sync, self.clock, self.size, self.byte_type
        )

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
    def byte_type(self):
        return self._byte_type
