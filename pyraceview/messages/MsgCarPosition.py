from ..percar import PerCarPositionData
from ..util import BitBuffer, ByteArray
from numpy import uint32


NUMBER_OF_CAR_BITS = uint32(8)
TIMECODE_BITS = uint32(32)


class MsgCarPosition(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.number_of_cars = int(bit_buffer.get_bits(NUMBER_OF_CAR_BITS))
        self.timecode = int(bit_buffer.get_bits(TIMECODE_BITS))

        self.car_data = {}

        for _ in range(self.number_of_cars):
            position_data = PerCarPositionData(bit_buffer)
            self.car_data[position_data.car_id] = position_data
 