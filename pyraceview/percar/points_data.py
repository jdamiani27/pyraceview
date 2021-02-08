from numpy import uint32
from dataclasses import dataclass
from ..util import BitBuffer


CAR_ID_BITS = uint32(8)
POINTS_BITS = uint32(13)
RESERVED_BITS = uint32(3)


@dataclass
class PerCarPointsData:
    car_id: int
    points: int

    def __init__(self, bit_buffer: BitBuffer):
        self.car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self.points = int(bit_buffer.get_bits(POINTS_BITS))
        bit_buffer.get_bits(RESERVED_BITS)
