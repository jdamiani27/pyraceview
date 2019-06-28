from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarRaceStatusData
from ..messages import MsgHeader


class MsgRaceStatus(object):  # extends MsgBase
    BITS_VITC_TIME = uint32(32)
    BITS_LAP = uint32(10)
    BITS_FLAG = uint32(3)
    BITS_CAUTIONS = uint32(5)
    BITS_FLAG_LAP = uint32(10)
    BITS_CARS = uint32(6)
    BITS_SUNSET = uint32(3)
    BITS_RESERVED = uint32(3)

    PREAMBLE_SIZE_BYTES = uint32((BITS_VITC_TIME + BITS_LAP
                                                 + BITS_FLAG
                                                 + BITS_CAUTIONS
                                                 + BITS_FLAG_LAP
                                                 + BITS_CARS
                                                 + BITS_SUNSET
                                                 + BITS_RESERVED) // 8)

    def __init__(self, msg_bytes):
        self._per_car_race_status = []  # PerCarRaceStatusData
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self._vitc_time = int(bit_buffer.get_bits(self.BITS_VITC_TIME))
        self._lap = int(bit_buffer.get_bits(self.BITS_LAP))
        self._flag = int(bit_buffer.get_bits(self.BITS_FLAG))
        self._number_cautions = int(bit_buffer.get_bits(self.BITS_CAUTIONS))
        self._last_flag_change_lap = int(bit_buffer.get_bits(self.BITS_FLAG_LAP))
        self._number_of_cars = int(bit_buffer.get_bits(self.BITS_CARS))
        self._sun_set_value = int(bit_buffer.get_bits(self.BITS_SUNSET))
        bit_buffer.get_bits(self.BITS_RESERVED)
        msg_header = MsgHeader(msg_bytes)
        byte_size = uint32((msg_header.size - self.PREAMBLE_SIZE_BYTES) // self._number_of_cars)

        i = 0
        while i < self._number_of_cars:
            self._per_car_race_status.append(PerCarRaceStatusData(bit_buffer, byte_size))
            i += 1

    @property
    def flag(self):
        return self._flag

    @property
    def last_flag_change_lap(self):
        return self._last_flag_change_lap

    @property
    def number_cautions(self):
        return self._number_cautions

    @property
    def vitc_time(self):
        return self._vitc_time

    @property
    def lap(self):
        return self._lap

    @property
    def per_car_race_status(self):
        return self._per_car_race_status

    @property
    def number_of_cars(self):
        return self._number_of_cars

    @property
    def sun_set_value(self):
        return self._sun_set_value
