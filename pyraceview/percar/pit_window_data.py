from dataclasses import dataclass
from ..util import BitBuffer


CAR_ID_BITS = 8
LOW_BITS = 12
HIGH_BITS = 12


@dataclass
class PerCarPitWindowData:
    car_id: int
    low: int
    high: int

    def __init__(self, bit_buffer: BitBuffer):
        self.car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self.low = int(bit_buffer.get_bits(LOW_BITS))
        self.high = int(bit_buffer.get_bits(HIGH_BITS))
