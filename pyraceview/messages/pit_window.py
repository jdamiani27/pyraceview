from ..messages import MsgBase
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPitWindowData
from dataclasses import dataclass
from typing import List


NUM_CARS_BITS = 8


@dataclass
class MsgPitWindow(MsgBase):
    num_cars: int
    car_data: List[PerCarPitWindowData]

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.num_cars = int(bit_buffer.get_bits(NUM_CARS_BITS))
        self.car_data = []

        for _ in range(self.num_cars):
            self.car_data.append(PerCarPitWindowData(bit_buffer))
