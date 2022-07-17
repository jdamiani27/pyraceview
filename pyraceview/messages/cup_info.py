from ..messages import MsgBase
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPointsData
from dataclasses import dataclass
from typing import List


LAP_BITS = 10
NUM_CARS_BITS = 6


@dataclass
class MsgCupInfo(MsgBase):
    lap: int
    num_cars: int
    car_data: List[PerCarPointsData]

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.lap = int(bit_buffer.get_bits(LAP_BITS))
        self.num_cars = int(bit_buffer.get_bits(NUM_CARS_BITS))

        self.car_data = []

        for _ in range(self.num_cars):
            self.car_data.append(PerCarPointsData(bit_buffer))
