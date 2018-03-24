from numpy import uint32
from ..util import BitBuffer
from ..percar import PerCarPointsData


class MsgCupInfo(object):
    CUP_POINTS_LAP_BITS = uint32(10)
    CUP_POINTS_NUM_CAR_BITS = uint32(6)

    def __init__(self, msg_header, byte_array):
        self._per_car_points = []
        _loc3_ = BitBuffer(byte_array)
        _loc3_.set_position(7)
        self._lap = _loc3_.get_bits(self.CUP_POINTS_LAP_BITS)
        self._num_cars = _loc3_.get_bits(self.CUP_POINTS_NUM_CAR_BITS)

        _loc4_ = 0

        while _loc4_ < self._num_cars:
            self._per_car_points.append(PerCarPointsData(_loc3_))
            _loc4_ += 1

    @property
    def per_car_points(self):
        return self._per_car_points
