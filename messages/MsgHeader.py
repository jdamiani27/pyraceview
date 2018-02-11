class MsgHeader(object):

    def __init__(self, message):
        self._sync = message.read_unsigned_byte()
        self._clock = message.read_unsigned_byte()
        self._size = message.read_unsigned_byte()
        self._byteType = chr(message.read_unsigned_byte())

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
