from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarRaceStatusData
from ..messages import MsgHeader


TIMECODE_BITS = uint32(32)
LAP_BITS = uint32(10)
FLAG_BITS = uint32(3)
NUMBER_OF_CAUTIONS_BITS = uint32(5)
FLAG_LAP_BITS = uint32(10)
NUMBER_OF_CAR_BITS = uint32(6)
SUNSET_BITS = uint32(3)
RESERVED_BITS = uint32(3)

PREAMBLE_SIZE_BYTES = uint32(
    (
        TIMECODE_BITS
        + LAP_BITS
        + FLAG_BITS
        + NUMBER_OF_CAUTIONS_BITS
        + FLAG_LAP_BITS
        + NUMBER_OF_CAR_BITS
        + SUNSET_BITS
        + RESERVED_BITS
    )
    // 8
)


class MsgRaceStatus(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.timecode = int(bit_buffer.get_bits(TIMECODE_BITS))
        self.lap = int(bit_buffer.get_bits(LAP_BITS))
        self.flag = int(bit_buffer.get_bits(FLAG_BITS))
        self.number_of_cautions = int(bit_buffer.get_bits(NUMBER_OF_CAUTIONS_BITS))
        self.last_flag_change_lap = int(bit_buffer.get_bits(FLAG_LAP_BITS))
        self.number_of_cars = int(bit_buffer.get_bits(NUMBER_OF_CAR_BITS))
        self.sunset = int(bit_buffer.get_bits(SUNSET_BITS))

        bit_buffer.get_bits(RESERVED_BITS)

        msg_header = MsgHeader(msg_bytes)
        byte_size = uint32(
            (msg_header.size - PREAMBLE_SIZE_BYTES) // self.number_of_cars
        )

        self.car_data = {}

        for _ in range(self.number_of_cars):
            race_status_data = PerCarRaceStatusData(bit_buffer, byte_size)
            self.car_data[race_status_data.car_id] = race_status_data
