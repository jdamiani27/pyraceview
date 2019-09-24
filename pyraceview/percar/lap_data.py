from numpy import uint32


CAR_ID_BITS = uint32(8)
LAST_LAP_TIME_BITS = uint32(19)
FASTEST_LAP_TIME_BITS = uint32(19)
LAPS_LED_BITS = uint32(10)
LAPS_IN_TOP_10_BITS = uint32(10)
RANK_BITS = uint32(6)


class PerCarLapData(object):
    def __init__(self, bit_buffer):
        self._car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self._last_lap_time = int(bit_buffer.get_bits(LAST_LAP_TIME_BITS))
        self._fastest_lap_time = int(bit_buffer.get_bits(FASTEST_LAP_TIME_BITS))
        self._laps_led = int(bit_buffer.get_bits(LAPS_LED_BITS))
        self._laps_in_top_10 = int(bit_buffer.get_bits(LAPS_IN_TOP_10_BITS))
        self._rank = int(bit_buffer.get_bits(RANK_BITS))

    @property
    def car_id(self):
        return self._car_id

    @property
    def last_lap_time(self):
        return self._last_lap_time

    @property
    def fastest_lap_time(self):
        return self._fastest_lap_time

    @property
    def laps_led(self):
        return self._laps_led

    @property
    def laps_in_top_10(self):
        return self._laps_in_top_10

    @property
    def rank(self):
        return self._rank
