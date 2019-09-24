from numpy import uint32
from ..messages import MsgBase
from ..util import BitBuffer, ByteArray
from ..percar import PerCarLapData


TIMECODE_BITS = uint32(32)
LAP_BITS = uint32(10)
NUM_CARS_BITS = uint32(6)
LEAD_CHANGES_BITS = uint32(8)
NUM_LEADERS_BITS = uint32(6)
NUM_CAUTIONS_BITS = uint32(5)
FLAG_LAP_BITS = uint32(10)
RESERVED_BITS = uint32(3)


class MsgLapInfo(MsgBase):
    def __init__(self, msg_bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self._timecode = int(bit_buffer.get_bits(TIMECODE_BITS))
        self._lap = int(bit_buffer.get_bits(LAP_BITS))
        self._num_cars = int(bit_buffer.get_bits(NUM_CARS_BITS))
        self._lead_changes = int(bit_buffer.get_bits(LEAD_CHANGES_BITS))
        self._num_leaders = int(bit_buffer.get_bits(NUM_LEADERS_BITS))
        self._num_cautions = int(bit_buffer.get_bits(NUM_CAUTIONS_BITS))
        self._last_flag_change_lap = int(
            bit_buffer.get_bits(FLAG_LAP_BITS)
        )
        
        bit_buffer.get_bits(RESERVED_BITS)

        self._car_data = []

        for _ in range(self._num_cars):
            self._car_data.append(PerCarLapData(bit_buffer))

    @property
    def lap(self):
        return self._lap

    @property
    def car_data(self):
        return self._car_data

    @property
    def num_cautions(self):
        return self._num_cautions

    @property
    def last_flag_change_lap(self):
        return self._last_flag_change_lap

    @property
    def num_leaders(self):
        return self._num_leaders

    @property
    def lead_changes(self):
        return self._lead_changes

    @property
    def timecode(self):
        return self._timecode

    @property
    def num_cars(self):
        return self._num_cars
