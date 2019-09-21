from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarStatsData


TIMECODE_BITS = uint32(32)
NUMBER_OF_CAR_BITS = uint32(8)


class MsgCarStats(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.timecode = int(bit_buffer.get_bits(TIMECODE_BITS))
        self.number_of_cars = int(bit_buffer.get_bits(NUMBER_OF_CAR_BITS))

        self.car_data = {}

        for _ in range(self.number_of_cars):
            stats_data = PerCarStatsData(bit_buffer)
            self.car_data[stats_data.car_id] = stats_data
