from numpy import uint32


CAR_ID_BITS = uint32(8)
TOP_SPEED_BITS = uint32(16)
FASTEST_TIME_BITS = uint32(19)
AVERAGE_LAP_BITS = uint32(19)
AVERAGE_SPEED_BITS = uint32(16)
RESERVED_BITS = uint32(2)


class PerCarStatsData(object):
    def __init__(self, bit_buffer):
        self._car_id = bit_buffer.get_bits(CAR_ID_BITS)
        self._top_speed = bit_buffer.get_bits(TOP_SPEED_BITS) / 100
        self._fastest_time = bit_buffer.get_bits(FASTEST_TIME_BITS)
        self._average_lap = bit_buffer.get_bits(AVERAGE_LAP_BITS)
        self._average_speed = bit_buffer.get_bits(AVERAGE_SPEED_BITS) / 100
        bit_buffer.get_bits(RESERVED_BITS)

    @property
    def car_id(self):
        return int(self._car_id)

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
