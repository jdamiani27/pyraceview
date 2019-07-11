import numpy as np
from .Endian import Endian


class ByteArray(object):
    def __init__(self, bytes):
        self._bytes = bytes
        self._position = 0
        self._endian = Endian.BIG_ENDIAN

    def read_unsigned_byte(self):
        return np.uint32(self.read(np.uint8))

    def read_byte(self):
        return np.int32(self.read(np.int8))

    def read_unsigned_short(self):
        return self.read(np.dtype(np.uint16).newbyteorder(self._endian.value))

    def read_short(self):
        return self.read(np.dtype(np.int16).newbyteorder(self._endian.value))

    def read_unsigned_int(self):
        return self.read(np.dtype(np.uint32).newbyteorder(self._endian.value))

    def read_utf_bytes(self, length):
        return self.read(np.dtype(("S", length))).decode("utf-8")

    def read(self, dtype):
        val = np.frombuffer(self.buffer, dtype=dtype, count=1)[0]
        self.position += val.itemsize

        return val

    @property
    def buffer(self):
        return self._bytes[self._position :]

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def endian(self):
        return self._endian

    @endian.setter
    def endian(self, value):
        self._endian = value
