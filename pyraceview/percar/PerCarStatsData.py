from numpy import uint32


class PerCarStatsData(object):
    BITS_CAR_NUM = uint32(8)
    BITS_TOP_SPEED = uint32(16)
    BITS_FASTEST_TIME = uint32(19)
    BITS_AVERAGE_LAP = uint32(19)
    BITS_AVERAGE_SPEED = uint32(16)
    RESERVED = uint32(2)

    def __init__(self, param1):
        self.car_id = int(param1.get_bits(self.BITS_CAR_NUM))
        self.top_speed = float(param1.get_bits(self.BITS_TOP_SPEED) / 100)
        self.fastest_time = int(param1.get_bits(self.BITS_FASTEST_TIME))
        self.average_lap = int(param1.get_bits(self.BITS_AVERAGE_LAP))
        self.average_speed = float(param1.get_bits(self.BITS_AVERAGE_SPEED) / 100)
        param1.get_bits(self.RESERVED)
