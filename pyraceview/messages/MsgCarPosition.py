from ..percar import PerCarPositionData
from ..util import BitBuffer, ByteArray
from numpy import uint32


CAR_POSITION_CAR_BITS = uint32(8)
CAR_POSITION_VITC_TIME_BITS = uint32(32)


class MsgCarPosition(object):
    def __init__(self, msg_bytes):
        self._car_data = []  # PerCarPositionData
        self._car_reverse_lookup = {}

        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self._number_of_cars = int(bit_buffer.get_bits(CAR_POSITION_CAR_BITS))
        self._vitc_time = int(bit_buffer.get_bits(CAR_POSITION_VITC_TIME_BITS))

        for _ in range(self._number_of_cars):
            position = PerCarPositionData(bit_buffer)
            self._car_data.append(position)
            self._car_reverse_lookup[position.car_id] = position

    @property
    def car_data(self):
        return self._car_data

    def get_car_by_id(self, car_id):
        return self._car_reverse_lookup[car_id]

    @property
    def vitc_time(self):
        return self._vitc_time

    @property
    def number_of_cars(self):
        return self._number_of_cars
