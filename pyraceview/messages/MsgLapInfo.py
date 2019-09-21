from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarLapData


TIMECODE_BITS = uint32(32)
LAP_BITS = uint32(10)
NUMBER_OF_CAR_BITS = uint32(6)
LEAD_CHANGES_BITS = uint32(8)
NUMBER_OF_LEADERS_BITS = uint32(6)
NUMBER_OF_CAUTIONS_BITS = uint32(5)
FLAP_LAP_BITS = uint32(10)
RESERVED_BITS = uint32(3)


class MsgLapInfo(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.timecode = int(bit_buffer.get_bits(TIMECODE_BITS))
        self.lap = int(bit_buffer.get_bits(LAP_BITS))
        self.number_of_cars = int(bit_buffer.get_bits(NUMBER_OF_CAR_BITS))
        self.lead_changes = int(bit_buffer.get_bits(LEAD_CHANGES_BITS))
        self.number_of_leaders = int(bit_buffer.get_bits(NUMBER_OF_LEADERS_BITS))
        self.number_of_cautions = int(bit_buffer.get_bits(NUMBER_OF_CAUTIONS_BITS))
        self.last_flag_change_lap = int(bit_buffer.get_bits(FLAP_LAP_BITS))

        bit_buffer.get_bits(RESERVED_BITS)

        self.car_data = {}

        for _ in range(self.number_of_cars):
            lap_data = PerCarLapData(bit_buffer)
            self.car_data[lap_data.car_id] = lap_data
