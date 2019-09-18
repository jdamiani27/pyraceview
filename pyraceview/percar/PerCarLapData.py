from numpy import uint32


LAPINFO_PER_CAR_BITS_CAR_NUMBER = uint32(8)
LAPINFO_PER_CAR_BITS_LAST_LAP_TIME = uint32(19)
LAPINFO_PER_CAR_BITS_FASTEST_LAP_TIME = uint32(19)
LAPINFO_PER_CAR_BITS_LAPS_LED = uint32(10)
LAPINFO_PER_CAR_BITS_LAPS_IN_TOP_10 = uint32(10)
LAPINFO_PER_CAR_BITS_LAP = uint32(6)


class PerCarLapData(object):
    def __init__(self, bit_buffer):
        self.car_id = int(bit_buffer.get_bits(LAPINFO_PER_CAR_BITS_CAR_NUMBER))
        self.last_lap_time = int(
            bit_buffer.get_bits(LAPINFO_PER_CAR_BITS_LAST_LAP_TIME)
        )
        self.fastest_lap_time = int(
            bit_buffer.get_bits(LAPINFO_PER_CAR_BITS_FASTEST_LAP_TIME)
        )
        self.laps_led = int(bit_buffer.get_bits(LAPINFO_PER_CAR_BITS_LAPS_LED))
        self.laps_in_top_10 = int(
            bit_buffer.get_bits(LAPINFO_PER_CAR_BITS_LAPS_IN_TOP_10)
        )
        self.rank = int(bit_buffer.get_bits(LAPINFO_PER_CAR_BITS_LAP))
