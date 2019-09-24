from numpy import uint32


CAR_ID_BITS = uint32(8)
LOW_BITS = uint32(12)
HIGH_BITS = uint32(12)


class PerCarPitWindowData(object):
    def __init__(self, bit_buffer):
        self._car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self._low = int(bit_buffer.get_bits(LOW_BITS))
        self._high = int(bit_buffer.get_bits(HIGH_BITS))

    @property
    def car_id(self):
        return self._car_id

    @property
    def low(self):
        return self._low

    @property
    def high(self):
        return self._high
