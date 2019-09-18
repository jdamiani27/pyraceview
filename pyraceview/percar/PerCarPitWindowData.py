from numpy import uint32


class PerCarPitWindowData(object):
    def __init__(self, bit_buffer):
        self.car_id = int(bit_buffer.get_bits(uint32(8)))
        self.low = int(bit_buffer.get_bits(uint32(12)))
        self.high = int(bit_buffer.get_bits(uint32(12)))
