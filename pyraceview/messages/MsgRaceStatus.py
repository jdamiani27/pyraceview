from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarRaceStatusData
from ..messages import MsgHeader


BITS_VITC_TIME = uint32(32)
BITS_LAP = uint32(10)
BITS_FLAG = uint32(3)
BITS_CAUTIONS = uint32(5)
BITS_FLAG_LAP = uint32(10)
BITS_CARS = uint32(6)
BITS_SUNSET = uint32(3)
BITS_RESERVED = uint32(3)

PREAMBLE_SIZE_BYTES = uint32(
    (
        BITS_VITC_TIME
        + BITS_LAP
        + BITS_FLAG
        + BITS_CAUTIONS
        + BITS_FLAG_LAP
        + BITS_CARS
        + BITS_SUNSET
        + BITS_RESERVED
    )
    // 8
)


class MsgRaceStatus(object):  # extends MsgBase
    def __init__(self, msg_bytes):
        self.per_car_race_status = []  # PerCarRaceStatusData
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self.vitc_time = int(bit_buffer.get_bits(BITS_VITC_TIME))
        self.lap = int(bit_buffer.get_bits(BITS_LAP))
        self.flag = int(bit_buffer.get_bits(BITS_FLAG))
        self.number_cautions = int(bit_buffer.get_bits(BITS_CAUTIONS))
        self.last_flag_change_lap = int(bit_buffer.get_bits(BITS_FLAG_LAP))
        self.number_of_cars = int(bit_buffer.get_bits(BITS_CARS))
        self.sun_set_value = int(bit_buffer.get_bits(BITS_SUNSET))
        bit_buffer.get_bits(BITS_RESERVED)
        msg_header = MsgHeader(msg_bytes)
        byte_size = uint32(
            (msg_header.size - PREAMBLE_SIZE_BYTES) // self.number_of_cars
        )

        for _ in range(self.number_of_cars):
            self.per_car_race_status.append(PerCarRaceStatusData(bit_buffer, byte_size))
