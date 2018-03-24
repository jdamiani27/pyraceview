from numpy import uint32


class PerCarPointsData(object):
    CUP_POINTS_BITS_ID = uint32(8)
    CUP_POINTS_BITS_DRIVER_POINTS = uint32(13)
    CUP_POINTS_BITS_RESERVED = uint32(3)

    def __init__(self, bit_buffer):
        self._id = bit_buffer.get_bits(self.CUP_POINTS_BITS_ID)
        self._points = bit_buffer.get_bits(self.CUP_POINTS_BITS_DRIVER_POINTS)
        bit_buffer.get_bits(self.CUP_POINTS_BITS_RESERVED)

    @property
    def id(self):
        return self._id

    @property
    def points(self):
        return self._points