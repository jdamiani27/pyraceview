from numpy import uint32
from ..util import BitBuffer
from ..percar import PerCarStatsData


class MsgCarStats(object):
    CAR_POSITION_VITC_TIME_BITS = uint32(32)
    NUMBER_OF_CAR_BITS = uint32(8)

    def __init__(self, msg_header, byte_array):
        self._car_data = [] #PerCarStatsData
        _loc3_ = BitBuffer(byte_array)
        _loc3_.set_position(7)
        self._vitcTime = _loc3_.get_bits(self.CAR_POSITION_VITC_TIME_BITS)
        self._number_of_cars = _loc3_.get_bits(self.NUMBER_OF_CAR_BITS)
        _loc4_ = 0

        while _loc4_ < self._number_of_cars:
            self._car_data.append(PerCarStatsData(_loc3_))
            _loc4_ += 1

    @property
    def car_data(self):
        return self._car_data
