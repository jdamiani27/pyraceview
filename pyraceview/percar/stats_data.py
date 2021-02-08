from numpy import uint32
from dataclasses import dataclass
from ..util import BitBuffer


CAR_ID_BITS = uint32(8)
TOP_SPEED_BITS = uint32(16)
FASTEST_TIME_BITS = uint32(19)
AVERAGE_LAP_BITS = uint32(19)
AVERAGE_SPEED_BITS = uint32(16)
RESERVED_BITS = uint32(2)


@dataclass
class PerCarStatsData:
    car_id: int
    top_speed: float
    fastest_time: int
    average_lap: int
    average_speed: float

    def __init__(self, bit_buffer: BitBuffer):
        self.car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self.top_speed = float(bit_buffer.get_bits(TOP_SPEED_BITS) / 100)
        self.fastest_time = int(bit_buffer.get_bits(FASTEST_TIME_BITS))
        self.average_lap = int(bit_buffer.get_bits(AVERAGE_LAP_BITS))
        self.average_speed = float(bit_buffer.get_bits(AVERAGE_SPEED_BITS) / 100)
        bit_buffer.get_bits(RESERVED_BITS)
