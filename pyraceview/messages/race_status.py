from ..util import BitBuffer, ByteArray
from ..percar import PerCarRaceStatusData
from ..messages import MsgBase
from dataclasses import dataclass
from typing import List


TIMECODE_BITS = 32
LAP_BITS = 10
FLAG_BITS = 3
NUM_CAUTIONS_BITS = 5
FLAG_LAP_BITS = 10
NUM_CARS_BITS = 6
SUNSET_BITS = 3
RESERVED_BITS = 3

PREAMBLE_SIZE_BYTES = (
        TIMECODE_BITS
        + LAP_BITS
        + FLAG_BITS
        + NUM_CAUTIONS_BITS
        + FLAG_LAP_BITS
        + NUM_CARS_BITS
        + SUNSET_BITS
        + RESERVED_BITS
    ) // 8


@dataclass
class MsgRaceStatus(MsgBase):
    timecode: int
    lap: int
    flag: int
    num_cautions: int
    last_flag_change_lap: int
    num_cars: int
    sunset: int
    car_data: List[PerCarRaceStatusData]

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.timecode = int(bit_buffer.get_bits(TIMECODE_BITS))
        self.lap = int(bit_buffer.get_bits(LAP_BITS))
        self.flag = int(bit_buffer.get_bits(FLAG_BITS))
        self.num_cautions = int(bit_buffer.get_bits(NUM_CAUTIONS_BITS))
        self.last_flag_change_lap = int(bit_buffer.get_bits(FLAG_LAP_BITS))
        self.num_cars = int(bit_buffer.get_bits(NUM_CARS_BITS))
        self.sunset = int(bit_buffer.get_bits(SUNSET_BITS))

        bit_buffer.get_bits(RESERVED_BITS)

        byte_size = (self.header.size - PREAMBLE_SIZE_BYTES) // self.num_cars

        self.car_data = []

        for _ in range(self.num_cars):
            self.car_data.append(
                PerCarRaceStatusData(bit_buffer, byte_size)
            )
