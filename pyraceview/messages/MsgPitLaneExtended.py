from ..util import Endian, ByteArray
from ..percar import PerCarPitStopExtendedData


class MsgPitLaneExtended(object):

    def __init__(self, msg_bytes):
        self._pits = [] # CarEntry
        byte_array = ByteArray(msg_bytes)
        endian = byte_array.endian
        byte_array.position = 7

        byte_array.endian = Endian.LITTLE_ENDIAN if (endian == Endian.BIG_ENDIAN) else Endian.BIG_ENDIAN
        self._vitc_time = byte_array.read_unsigned_int()
        self._num_cars = byte_array.read_unsigned_byte()

        i = 0

        while i < self._num_cars:
            self._pits.append(CarEntry(byte_array))
            i += 1

        byte_array.endian = endian

    @property
    def vitc_time(self):
        return self._vitc_time

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
        self._num_cars = byte_array.read_byte()

        i = 0

        while i < self._num_cars:
            self._pits.append(PerCarPitStopExtendedData(byte_array))
            i += 1

    @property
    def car_id(self):
        return self._car_id

    @property
    def pits(self):
        return self._pits
