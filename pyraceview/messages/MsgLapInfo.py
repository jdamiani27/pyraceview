from numpy import uint32
from ..util import BitBuffer
from ..percar import PerCarLapData


class MsgLapInfo(object):
    LAPINFO_BITS_VITC_TIME = uint32(32)
    LAPINFO_BITS_LAP = uint32(10)
    LAPINFO_BITS_NUM_CARS = uint32(6)
    LAPINFO_BITS_LEAD_CHANGES = uint32(8)
    LAPINFO_BITS_NUM_LEADERS = uint32(6)
    LAPINFO_BITS_NUM_CAUTIONS = uint32(5)
    LAPINFO_BITS_FLAG_LAP = uint32(10)
    LAPINFO_BITS_RESERVED = uint32(3)

    def __init__(self, msg_header, byte_array):
        self._per_car_lap_data = []
        _loc3_ = BitBuffer(byte_array)
        _loc3_.set_position(7)
        self._vitc_time = _loc3_.get_bits(self.LAPINFO_BITS_VITC_TIME)
        self._lap = _loc3_.get_bits(self.LAPINFO_BITS_LAP)
        self._num_cars = _loc3_.get_bits(self.LAPINFO_BITS_NUM_CARS)
        self._lead_changes = _loc3_.get_bits(self.LAPINFO_BITS_LEAD_CHANGES)
        self._num_leaders = _loc3_.get_bits(self.LAPINFO_BITS_NUM_LEADERS)
        self._num_cautions = _loc3_.get_bits(self.LAPINFO_BITS_NUM_CAUTIONS)
        self._last_flag_change_lap = _loc3_.get_bits(self.LAPINFO_BITS_FLAG_LAP)
        _loc3_.get_bits(self.LAPINFO_BITS_RESERVED)

        _loc4_ = 0

        while _loc4_ < self._num_cars:
            self._per_car_lap_data.append(PerCarLapData(_loc3_))
            _loc4_ += 1

    @property
    def lap(self):
        return self._lap

    @property
    def per_car_lap_data(self):
        return self._per_car_lap_data

    @property
    def num_cautions(self):
        return self._num_cautions

    @property
    def last_flag_change_lap(self):
        return self._last_flag_change_lap

    @property
    def num_leaders(self):
        return self._num_leaders

    @property
    def lead_changes(self):
        return self._lead_changes
