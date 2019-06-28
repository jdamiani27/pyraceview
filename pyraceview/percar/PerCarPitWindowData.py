from numpy import uint32


class PerCarPitWindowData(object):

    def __init__(self, bit_buffer):
        self._car_id = int(bit_buffer.get_bits(uint32(8)))
        self._low = int(bit_buffer.get_bits(uint32(12)))
        self._high = int(bit_buffer.get_bits(uint32(12)))

    @property
    def car_id(self):
        return self._car_id

    @property
    def low(self):
        return self._low

    @property
    def high(self):
        return self._high
