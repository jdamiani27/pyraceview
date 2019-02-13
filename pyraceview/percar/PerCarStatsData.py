from numpy import uint32


class PerCarStatsData(object):
    BITS_CAR_NUM = uint32(8)
    BITS_TOP_SPEED = uint32(16)
    BITS_FASTEST_TIME = uint32(19)
    BITS_AVERAGE_LAP = uint32(19)
    BITS_AVERAGE_SPEED = uint32(16)
    RESERVED = uint32(2)

    def __init__(self, param1):
        self._id = param1.get_bits(self.BITS_CAR_NUM)
        self._top_speed = param1.get_bits(self.BITS_TOP_SPEED) / 100
        self._fastest_time = param1.get_bits(self.BITS_FASTEST_TIME)
        self._average_lap = param1.get_bits(self.BITS_AVERAGE_LAP)
        self._average_speed = param1.get_bits(self.BITS_AVERAGE_SPEED) / 100
        param1.get_bits(self.RESERVED)

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
