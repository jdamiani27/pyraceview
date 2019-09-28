from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarRaceStatusData
from ..messages import MsgBase


TIMECODE_BITS = uint32(32)
LAP_BITS = uint32(10)
FLAG_BITS = uint32(3)
NUM_CAUTIONS_BITS = uint32(5)
FLAG_LAP_BITS = uint32(10)
NUM_CARS_BITS = uint32(6)
SUNSET_BITS = uint32(3)
RESERVED_BITS = uint32(3)

PREAMBLE_SIZE_BYTES = uint32(
    (
        TIMECODE_BITS
        + LAP_BITS
        + FLAG_BITS
        + NUM_CAUTIONS_BITS
        + FLAG_LAP_BITS
        + NUM_CARS_BITS
        + SUNSET_BITS
        + RESERVED_BITS
    )
    // 8
)


class MsgRaceStatus(MsgBase):
    def __init__(self, msg_bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self._timecode = int(bit_buffer.get_bits(TIMECODE_BITS))
        self._lap = int(bit_buffer.get_bits(LAP_BITS))
        self._flag = int(bit_buffer.get_bits(FLAG_BITS))
        self._num_cautions = int(bit_buffer.get_bits(NUM_CAUTIONS_BITS))
        self._last_flag_change_lap = int(bit_buffer.get_bits(FLAG_LAP_BITS))
        self._num_cars = int(bit_buffer.get_bits(NUM_CARS_BITS))
        self._sunset = int(bit_buffer.get_bits(SUNSET_BITS))

        bit_buffer.get_bits(RESERVED_BITS)

        byte_size = uint32(
            (self.header.size - PREAMBLE_SIZE_BYTES) // self._num_cars
        )

        self._car_data = []

        for _ in range(self._num_cars):
            self._car_data.append(
                PerCarRaceStatusData(bit_buffer, byte_size)
            )

    @property
    def flag(self):
        return self._flag

    @property
    def last_flag_change_lap(self):
        return self._last_flag_change_lap

    @property
    def num_cautions(self):
        return self._num_cautions

    @property
    def timecode(self):
        return self._timecode

    @property
    def lap(self):
        return self._lap

    @property
    def car_data(self):
        return self._car_data

    @property
    def num_cars(self):
        return self._num_cars

    @property
    def sunset(self):
        return self._sunset
