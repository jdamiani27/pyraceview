from dataclasses import dataclass
from ..util import BitBuffer


CAR_ID_BITS = 8
LAST_LAP_TIME_BITS = 19
FASTEST_LAP_TIME_BITS = 19
LAPS_LED_BITS = 10
LAPS_IN_TOP_10_BITS = 10
RANK_BITS = 6


@dataclass
class PerCarLapData:
    car_id: int
    last_lap_time: int
    fastest_lap_time: int
    laps_led: int
    laps_in_top_10: int
    rank: int

    def __init__(self, bit_buffer: BitBuffer):
        self.car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self.last_lap_time = int(bit_buffer.get_bits(LAST_LAP_TIME_BITS))
        self.fastest_lap_time = int(bit_buffer.get_bits(FASTEST_LAP_TIME_BITS))
        self.laps_led = int(bit_buffer.get_bits(LAPS_LED_BITS))
        self.laps_in_top_10 = int(bit_buffer.get_bits(LAPS_IN_TOP_10_BITS))
        self.rank = int(bit_buffer.get_bits(RANK_BITS))
