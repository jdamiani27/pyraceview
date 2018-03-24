from ..util import Endian
from ..percar import PerCarPitStopExtendedData


class MsgPitLaneExtended(object):

    def __init__(self, msg_header, byte_array):
        self._pits = [] # CarEntry
        _loc3_ = byte_array.endian
        byte_array.position = 7
        
        byte_array.endian = Endian.LITTLE_ENDIAN if (_loc3_ == Endian.BIG_ENDIAN) else Endian.BIG_ENDIAN
        self._vitc = byte_array.read_unsigned_int()
        self._num_cars = byte_array.read_unsigned_byte()
        _loc5_ = 0

        while _loc5_ < self._num_cars:
            self._pits.append(CarEntry(byte_array))
            _loc5_ += 1

        byte_array.endian = _loc3_

    @property
    def vitc(self):
        return self._vitc

    @property
    def num_cars(self):
        return self._num_cars

    def get_car_id(self, param1):
        return self._pits[param1].car_id

    def get_car(self, param1):
        return self._pits[param1].pits


class CarEntry(object):

    def __init__(self, byte_array):
        self._pits = [] # PerCarPitStopExtendedData
        self._car_id = byte_array.read_unsigned_byte()
        _loc2_ = byte_array.read_byte()
        _loc3_ = 0

        while _loc3_ < _loc2_:
            self._pits.append(PerCarPitStopExtendedData(byte_array))
            _loc3_ += 1

    @property
    def car_id(self):
        return self._car_id

    @property
    def pits(self):
        return self._pits
