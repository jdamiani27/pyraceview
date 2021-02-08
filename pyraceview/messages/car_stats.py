from numpy import uint32
from ..messages import MsgBase
from ..util import BitBuffer, ByteArray
from ..percar import PerCarStatsData
from dataclasses import dataclass
from typing import List


TIMECODE_BITS = uint32(32)
NUM_CARS_BITS = uint32(8)


@dataclass
class MsgCarStats(MsgBase):
    timecode: int
    num_cars:int
    car_data: List[PerCarStatsData]

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.timecode = int(bit_buffer.get_bits(TIMECODE_BITS))
        self.num_cars = int(bit_buffer.get_bits(NUM_CARS_BITS))

        self.car_data = []

        for _ in range(self.num_cars):
            self.car_data.append(PerCarStatsData(bit_buffer))
