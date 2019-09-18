from numpy import uint32


class PerCarPointsData(object):
    CUP_POINTS_BITS_ID = uint32(8)
    CUP_POINTS_BITS_DRIVER_POINTS = uint32(13)
    CUP_POINTS_BITS_RESERVED = uint32(3)

    def __init__(self, bit_buffer):
        self.car_id = int(bit_buffer.get_bits(self.CUP_POINTS_BITS_ID))
        self.points = int(bit_buffer.get_bits(self.CUP_POINTS_BITS_DRIVER_POINTS))
        bit_buffer.get_bits(self.CUP_POINTS_BITS_RESERVED)
