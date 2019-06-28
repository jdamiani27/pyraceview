from numpy import uint32


class PerCarLapData(object):
    LAPINFO_PER_CAR_BITS_CAR_NUMBER = uint32(8)
    LAPINFO_PER_CAR_BITS_LAST_LAP_TIME = uint32(19)
    LAPINFO_PER_CAR_BITS_FASTEST_LAP_TIME = uint32(19)
    LAPINFO_PER_CAR_BITS_LAPS_LED = uint32(10)
    LAPINFO_PER_CAR_BITS_LAPS_IN_TOP_10 = uint32(10)
    LAPINFO_PER_CAR_BITS_LAP = uint32(6)

    def __init__(self, bit_buffer):
        self._car_id = int(bit_buffer.get_bits(self.LAPINFO_PER_CAR_BITS_CAR_NUMBER))
        self._last_lap_time = int(bit_buffer.get_bits(self.LAPINFO_PER_CAR_BITS_LAST_LAP_TIME))
        self._fastest_lap_time = int(bit_buffer.get_bits(self.LAPINFO_PER_CAR_BITS_FASTEST_LAP_TIME))
        self._laps_led = int(bit_buffer.get_bits(self.LAPINFO_PER_CAR_BITS_LAPS_LED))
        self._laps_in_top_10 = int(bit_buffer.get_bits(self.LAPINFO_PER_CAR_BITS_LAPS_IN_TOP_10))
        self._rank = int(bit_buffer.get_bits(self.LAPINFO_PER_CAR_BITS_LAP))

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
