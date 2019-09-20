from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPointsData


LAP_BITS = uint32(10)
NUMBER_OF_CAR_BITS = uint32(6)


class MsgCupInfo(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.lap = int(bit_buffer.get_bits(LAP_BITS))
        self.number_of_cars = int(bit_buffer.get_bits(NUMBER_OF_CAR_BITS))

        self.car_data = {}

        for _ in range(self.number_of_cars):
            points_data = PerCarPointsData(bit_buffer)
            self.car_data[points_data.car_id] = points_data
