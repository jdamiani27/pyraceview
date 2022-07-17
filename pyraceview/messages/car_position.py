from ..messages import MsgBase
from ..percar import PerCarPositionData
from ..util import BitBuffer, ByteArray
from dataclasses import dataclass
from typing import List


NUM_CARS_BITS = 8
TIMECODE_BITS = 32


@dataclass
class MsgCarPosition(MsgBase):
    num_cars: int
    timecode: int
    car_data: List[PerCarPositionData]

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.num_cars = int(bit_buffer.get_bits(NUM_CARS_BITS))
        self.timecode = int(bit_buffer.get_bits(TIMECODE_BITS))

        self.car_data = []

        for _ in range(self.num_cars):
            self.car_data.append(PerCarPositionData(bit_buffer))
