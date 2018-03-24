from numpy import uint32
from ..util import BitBuffer
from ..percar import PerCarPitWindowData


class MsgPitWindow(object):
    def __init__(self, msg_header, byte_array):
         _loc3_ = BitBuffer(byte_array)
         _loc3_.set_position(7)
         _loc4_ = _loc3_.get_bits(uint32(8))
         _loc5_ = 0

         self._per_car_pit_window_data = []

         while _loc5_ < _loc4_:
             _loc6_ = _loc3_.get_bits(uint32(8))
             _loc7_ = _loc3_.get_bits(uint32(12))
             _loc8_ = _loc3_.get_bits(uint32(12))
             self._per_car_pit_window_data.append(PerCarPitWindowData(_loc6_,_loc7_,_loc8_))
             _loc5_ += 1

    @property
    def per_car_pit_window_data(self):
        return self._per_car_pit_window_data
