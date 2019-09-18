from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarStatsData


class MsgCarStats(object):
    CAR_POSITION_VITC_TIME_BITS = uint32(32)
    NUMBER_OF_CAR_BITS = uint32(8)

    def __init__(self, msg_bytes):
        self.car_data = []  # PerCarStatsData
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self.vitc_time = int(bit_buffer.get_bits(self.CAR_POSITION_VITC_TIME_BITS))
        self.number_of_cars = int(bit_buffer.get_bits(self.NUMBER_OF_CAR_BITS))

        for _ in range(self.number_of_cars):
            self.car_data.append(PerCarStatsData(bit_buffer))
