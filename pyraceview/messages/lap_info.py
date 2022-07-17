from ..messages import MsgBase
from ..util import BitBuffer, ByteArray
from ..percar import PerCarLapData
from dataclasses import dataclass
from typing import List


TIMECODE_BITS = 32
LAP_BITS = 10
NUM_CARS_BITS = 6
LEAD_CHANGES_BITS = 8
NUM_LEADERS_BITS = 6
NUM_CAUTIONS_BITS = 5
FLAG_LAP_BITS = 10
RESERVED_BITS = 3


@dataclass
class MsgLapInfo(MsgBase):
    timecode: int
    lap: int
    num_cars: int
    lead_changes: int
    num_leaders: int
    num_cautions: int
    last_flag_change_lap: int
    car_data: List[PerCarLapData]

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.timecode = int(bit_buffer.get_bits(TIMECODE_BITS))
        self.lap = int(bit_buffer.get_bits(LAP_BITS))
        self.num_cars = int(bit_buffer.get_bits(NUM_CARS_BITS))
        self.lead_changes = int(bit_buffer.get_bits(LEAD_CHANGES_BITS))
        self.num_leaders = int(bit_buffer.get_bits(NUM_LEADERS_BITS))
        self.num_cautions = int(bit_buffer.get_bits(NUM_CAUTIONS_BITS))
        self.last_flag_change_lap = int(
            bit_buffer.get_bits(FLAG_LAP_BITS)
        )
        
        bit_buffer.get_bits(RESERVED_BITS)

        self.car_data = []

        for _ in range(self.num_cars):
            self.car_data.append(PerCarLapData(bit_buffer))
