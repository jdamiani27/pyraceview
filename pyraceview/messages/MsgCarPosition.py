from ..percar import PerCarPositionData
from ..util import BitBuffer
from numpy import uint32


class MsgCarPosition(object):
    CAR_POSITION_CAR_BITS = uint32(8)
    CAR_POSITION_VITC_TIME_BITS = uint32(32)

    def __init__(self, param1, param2):
        _loc3_ = None
        _loc4_ = 0
        _loc5_ = None
        self._car_data = [] # PerCarPositionData
        self._car_reverse_lookup = {}

        if param2:
            _loc3_ = BitBuffer(param2)
            _loc3_.set_position(7)
            self._number_of_cars = _loc3_.get_bits(self.CAR_POSITION_CAR_BITS)
            self._vitcTime = _loc3_.get_bits(self.CAR_POSITION_VITC_TIME_BITS)
            _loc4_ = 0

            while _loc4_ < self._number_of_cars:
                _loc5_ = PerCarPositionData(_loc3_)
                self._car_data.append(_loc5_)
                self._car_reverse_lookup[_loc5_.car_id] = _loc5_
                _loc4_ += 1

    @property
    def car_data(self):
        return self._car_data

    def get_car_by_id(self, param1):
        return self._car_reverse_lookup[param1]

    @property
    def vitcTime(self):
        return self._vitcTime

    @property
    def number_of_cars(self):
        return self._number_of_cars
