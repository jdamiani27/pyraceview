import numpy as np


class ByteArray(object):

    def __init__(self, bytes):
        self._bytes = bytes
        self._position = 0

    def read_unsigned_byte(self):
        return np.uint32(self.read(np.uint8))

    def read_unsigned_short(self):
        return self.read(np.uint16)

    def read(self, dtype):
        val = np.frombuffer(self.buffer, dtype=dtype, count=1)[0]
        self.position += val.itemsize

        return val

    @property
    def buffer(self):
        return self._bytes[self._position:]

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
