import struct
from .Endian import Endian


class ByteArray(object):
    def __init__(self, bytes):
        self._bytes = bytes
        self._position = 0
        self._endian = Endian.BIG_ENDIAN

    def read_unsigned_byte(self):
        return self.read("B")
        # return np.uint32(self.read(np.uint8))

    def read_byte(self):
        return self.read("b")
        # return np.int32(self.read(np.int8))

    def read_unsigned_short(self):
        return self.read(self.endian.value + "H")
        # return self.read(np.dtype(np.uint16).newbyteorder(self._endian.value))

    def read_short(self):
        return self.read(self.endian.value + "h")
        # return self.read(np.dtype(np.int16).newbyteorder(self._endian.value))

    def read_unsigned_int(self):
        return self.read(self.endian.value + "I")
        # return self.read(np.dtype(np.uint32).newbyteorder(self._endian.value))

    def read_utf_bytes(self, length):
        return ctypes.create_string_buffer(self.read(str(length) + "s")).decode("utf-8")

    def read(self, format_char):
        # val = np.frombuffer(self.buffer, dtype=dtype, count=1)[0]
        val = struct.unpack_from(format_char, self.buffer)[0]
        self.position += struct.calcsize(format_char)

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
