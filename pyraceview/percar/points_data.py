from dataclasses import dataclass
from ..util import BitBuffer


CAR_ID_BITS = 8
POINTS_BITS = 13
RESERVED_BITS = 3


@dataclass
class PerCarPointsData:
    car_id: int
    points: int

    def __init__(self, bit_buffer: BitBuffer):
        self.car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self.points = int(bit_buffer.get_bits(POINTS_BITS))
        bit_buffer.get_bits(RESERVED_BITS)
