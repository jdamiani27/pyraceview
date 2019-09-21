from numpy import uint32


BITS_CAR_NUM = uint32(8)
BITS_TOP_SPEED = uint32(16)
BITS_FASTEST_TIME = uint32(19)
BITS_AVERAGE_LAP = uint32(19)
BITS_AVERAGE_SPEED = uint32(16)
RESERVED = uint32(2)


class PerCarStatsData(object):
    def __init__(self, bit_buffer):
        self._id = bit_buffer.get_bits(BITS_CAR_NUM)
        self._top_speed = bit_buffer.get_bits(BITS_TOP_SPEED) / 100
        self._fastest_time = bit_buffer.get_bits(BITS_FASTEST_TIME)
        self._average_lap = bit_buffer.get_bits(BITS_AVERAGE_LAP)
        self._average_speed = bit_buffer.get_bits(BITS_AVERAGE_SPEED) / 100
        bit_buffer.get_bits(RESERVED)

    @property
    def car_id(self):
        return int(self._id)

    @property
    def top_speed(self):
        return float(self._top_speed)

    @property
    def fastest_time(self):
        return int(self._fastest_time)

    @property
    def average_lap(self):
        return int(self._average_lap)

    @property
    def average_speed(self):
        return float(self._average_speed)
