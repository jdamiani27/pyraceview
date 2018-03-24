from numpy import uint32
from ..util import BitBuffer
from ..percar import PerCarStatsData


class MsgCarStats(object):
    CAR_POSITION_VITC_TIME_BITS = uint32(32)
    NUMBER_OF_CAR_BITS = uint32(8)

    def __init__(self, msg_header, byte_array):
        self._car_data = [] # PerCarStatsData
        bit_buffer = BitBuffer(byte_array)
        bit_buffer.set_position(7)
        self._vitc_time = bit_buffer.get_bits(self.CAR_POSITION_VITC_TIME_BITS)
        self._number_of_cars = bit_buffer.get_bits(self.NUMBER_OF_CAR_BITS)
        i = 0

        while i < self._number_of_cars:
            self._car_data.append(PerCarStatsData(bit_buffer))
            i += 1

    @property
    def car_data(self):
        return self._car_data
