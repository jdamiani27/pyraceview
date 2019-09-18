from ..models import Flag
from numpy import uint32


BITMASK_TIRES_IS_ESTIMATE = 1
BITMASK_ABNORMAL_PIT = 2
EXPANDED_TIME_FIELDS_BITMASK = uint32(128)
FLAG_BITMASK = uint32(15)

FLAG_CONVERSION = {
    1: Flag.PRE_RACE,
    2: Flag.GREEN,
    3: Flag.YELLOW,
    4: Flag.RED,
    5: Flag.CHECKERED,
    6: Flag.WHITE,
}


class PerCarPitStopExtendedData(object):
    def __init__(self, byte_array):
        self.race_lap = int(byte_array.read_short())
        self.lap = int(byte_array.read_short())
        self.rank_in = int(byte_array.read_byte())
        self.rank_out = int(byte_array.read_byte())

        _loc2_ = byte_array.read_byte()

        try:
            self.flag = FLAG_CONVERSION[_loc2_ & FLAG_BITMASK]
        except KeyError:
            self.flag = Flag.UNDEFINED

        if _loc2_ & EXPANDED_TIME_FIELDS_BITMASK:
            self.to_stop = float(byte_array.read_unsigned_int() / 10)
            self.to_left_jack_up = float(byte_array.read_unsigned_int() / 10)
            self.to_left_jack_dn = float(byte_array.read_unsigned_int() / 10)
            self.to_right_jack_up = float(byte_array.read_unsigned_int() / 10)
            self.to_right_jack_dn = float(byte_array.read_unsigned_int() / 10)
            self.to_restart = float(byte_array.read_unsigned_int() / 10)
            self.to_exit = float(byte_array.read_unsigned_int() / 10)
        else:
            self.to_stop = float(byte_array.read_unsigned_short() / 10)
            self.to_left_jack_up = float(byte_array.read_unsigned_short() / 10)
            self.to_left_jack_dn = float(byte_array.read_unsigned_short() / 10)
            self.to_right_jack_up = float(byte_array.read_unsigned_short() / 10)
            self.to_right_jack_dn = float(byte_array.read_unsigned_short() / 10)
            self.to_restart = float(byte_array.read_unsigned_short() / 10)
            self.to_exit = float(byte_array.read_unsigned_short() / 10)

        self.tires = int(byte_array.read_byte())
        self.flags = int(byte_array.read_byte())
        self.pit_group = int(byte_array.read_byte())

    @property
    def tires_is_estimate(self):
        return (self.flags & BITMASK_TIRES_IS_ESTIMATE) != 0

    @property
    def abnormal_stop(self):
        return (self.flags & BITMASK_ABNORMAL_PIT) != 0
