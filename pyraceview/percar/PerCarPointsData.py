from numpy import uint32


CAR_ID_BITS = uint32(8)
POINTS_BITS = uint32(13)
RESERVED_BITS = uint32(3)


class PerCarPointsData(object):
    def __init__(self, bit_buffer):
        self._car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self._points = int(bit_buffer.get_bits(POINTS_BITS))
        bit_buffer.get_bits(RESERVED_BITS)

    @property
    def car_id(self):
        return self._car_id

    @property
    def points(self):
        return self._points
