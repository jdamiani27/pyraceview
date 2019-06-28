from numpy import uint32
from ..util import BitBuffer, ByteArray
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

    def __init__(self, msg_bytes):
        self._per_car_lap_data = [] # PerCarLapData
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self._vitc_time = int(bit_buffer.get_bits(self.LAPINFO_BITS_VITC_TIME))
        self._lap = int(bit_buffer.get_bits(self.LAPINFO_BITS_LAP))
        self._num_cars = int(bit_buffer.get_bits(self.LAPINFO_BITS_NUM_CARS))
        self._lead_changes = int(bit_buffer.get_bits(self.LAPINFO_BITS_LEAD_CHANGES))
        self._num_leaders = int(bit_buffer.get_bits(self.LAPINFO_BITS_NUM_LEADERS))
        self._num_cautions = int(bit_buffer.get_bits(self.LAPINFO_BITS_NUM_CAUTIONS))
        self._last_flag_change_lap = int(bit_buffer.get_bits(self.LAPINFO_BITS_FLAG_LAP))
        bit_buffer.get_bits(self.LAPINFO_BITS_RESERVED)

        i = 0

        while i < self._num_cars:
            self._per_car_lap_data.append(PerCarLapData(bit_buffer))
            i += 1

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

    @property
    def vitc_time(self):
        return self._vitc_time
