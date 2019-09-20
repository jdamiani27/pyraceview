from numpy import uint32


CAR_ID_BITS = uint32(8)
LAST_LAP_TIME_BITS = uint32(19)
FASTEST_LAP_TIME_BITS = uint32(19)
LAPS_LED_BITS = uint32(10)
LAPS_IN_TOP_10_BITS = uint32(10)
RANK_BITS = uint32(6)


class PerCarLapData(object):
    def __init__(self, bit_buffer):
        self.car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self.last_lap_time = int(
            bit_buffer.get_bits(LAST_LAP_TIME_BITS)
        )
        self.fastest_lap_time = int(
            bit_buffer.get_bits(FASTEST_LAP_TIME_BITS)
        )
        self.laps_led = int(bit_buffer.get_bits(LAPS_LED_BITS))
        self.laps_in_top_10 = int(
            bit_buffer.get_bits(LAPS_IN_TOP_10_BITS)
        )
        self.rank = int(bit_buffer.get_bits(RANK_BITS))
