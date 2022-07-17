from ..models import Flag
from dataclasses import dataclass
from ..util import ByteArray


TIRES_IS_ESTIMATE_BITMASK = 1
ABNORMAL_PIT_BITMASK = 2
EXPANDED_TIME_FIELDS_BITMASK = 128
FLAG_BITMASK = 15

FLAG_CONVERSION = {
    1: Flag.PRE_RACE,
    2: Flag.GREEN,
    3: Flag.YELLOW,
    4: Flag.RED,
    5: Flag.CHECKERED,
    6: Flag.WHITE,
}


@dataclass
class PerCarPitStopExtendedData:
    race_lap: int
    lap: int
    rank_in: int
    rank_out: int
    flag: Flag
    to_stop: float
    to_left_jack_up: float
    to_left_jack_dn: float
    to_right_jack_up: float
    to_right_jack_dn: float
    to_restart: float
    to_exit: float
    tires: int
    flags: int
    pit_group: int
    tires_is_estimate: bool
    abnormal_stop: bool

    def __init__(self, byte_array: ByteArray):
        self.race_lap = int(byte_array.read_short())
        self.lap = int(byte_array.read_short())
        self.rank_in = int(byte_array.read_byte())
        self.rank_out = int(byte_array.read_byte())

        _flag_lookup = byte_array.read_byte()

        try:
            self.flag = FLAG_CONVERSION[_flag_lookup & FLAG_BITMASK]
        except KeyError:
            self.flag = Flag.UNDEFINED

        if _flag_lookup & EXPANDED_TIME_FIELDS_BITMASK:
            read_timing_val = byte_array.read_unsigned_int
        else:
            read_timing_val = byte_array.read_unsigned_short

        self.to_stop = float(read_timing_val() / 10)
        self.to_left_jack_up = float(read_timing_val() / 10)
        self.to_left_jack_dn = float(read_timing_val() / 10)
        self.to_right_jack_up = float(read_timing_val() / 10)
        self.to_right_jack_dn = float(read_timing_val() / 10)
        self.to_restart = float(read_timing_val() / 10)
        self.to_exit = float(read_timing_val() / 10)

        self.tires = int(byte_array.read_byte())
        self.flags = int(byte_array.read_byte())
        self.pit_group = int(byte_array.read_byte())

        self.tires_is_estimate = (self.flags & TIRES_IS_ESTIMATE_BITMASK) != 0
        self.abnormal_stop = (self.flags & ABNORMAL_PIT_BITMASK) != 0
