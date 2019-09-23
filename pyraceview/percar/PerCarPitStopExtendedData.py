from ..models import Flag
from numpy import uint32


TIRES_IS_ESTIMATE_BITMASK = 1
ABNORMAL_PIT_BITMASK = 2
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
        self._race_lap = int(byte_array.read_short())
        self._lap = int(byte_array.read_short())
        self._rank_in = int(byte_array.read_byte())
        self._rank_out = int(byte_array.read_byte())

        _flag_lookup = byte_array.read_byte()

        try:
            self._flag = FLAG_CONVERSION[_flag_lookup & FLAG_BITMASK]
        except KeyError:
            self._flag = Flag.UNDEFINED

        if _flag_lookup & EXPANDED_TIME_FIELDS_BITMASK:
            self._to_stop = float(byte_array.read_unsigned_int() / 10)
            self._to_left_jack_up = float(byte_array.read_unsigned_int() / 10)
            self._to_left_jack_dn = float(byte_array.read_unsigned_int() / 10)
            self._to_right_jack_up = float(byte_array.read_unsigned_int() / 10)
            self._to_right_jack_dn = float(byte_array.read_unsigned_int() / 10)
            self._to_restart = float(byte_array.read_unsigned_int() / 10)
            self._to_exit = float(byte_array.read_unsigned_int() / 10)
        else:
            self._to_stop = float(byte_array.read_unsigned_short() / 10)
            self._to_left_jack_up = float(byte_array.read_unsigned_short() / 10)
            self._to_left_jack_dn = float(byte_array.read_unsigned_short() / 10)
            self._to_right_jack_up = float(byte_array.read_unsigned_short() / 10)
            self._to_right_jack_dn = float(byte_array.read_unsigned_short() / 10)
            self._to_restart = float(byte_array.read_unsigned_short() / 10)
            self._to_exit = float(byte_array.read_unsigned_short() / 10)

        self._tires = int(byte_array.read_byte())
        self._flags = int(byte_array.read_byte())
        self._pit_group = int(byte_array.read_byte())

    @property
    def race_lap(self):
        return self._race_lap

    @property
    def lap(self):
        return self._lap

    @property
    def flag(self):
        return self._flag

    @property
    def flags(self):
        return self._flags

    @property
    def rank_in(self):
        return self._rank_in

    @property
    def rank_out(self):
        return self._rank_out

    @property
    def to_stop(self):
        return self._to_stop

    @property
    def to_left_jack_up(self):
        return self._to_left_jack_up

    @property
    def to_left_jack_dn(self):
        return self._to_left_jack_dn

    @property
    def to_right_jack_up(self):
        return self._to_right_jack_up

    @property
    def to_right_jack_dn(self):
        return self._to_right_jack_dn

    @property
    def to_restart(self):
        return self._to_restart

    @property
    def to_exit(self):
        return self._to_exit

    @property
    def tires(self):
        return self._tires

    @property
    def pit_group(self):
        return self._pit_group

    @property
    def tires_is_estimate(self):
        return (self._flags & TIRES_IS_ESTIMATE_BITMASK) != 0

    @property
    def abnormal_stop(self):
        return (self._flags & ABNORMAL_PIT_BITMASK) != 0
