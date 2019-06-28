from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPitWindowData


class MsgPitWindow(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self._num_cars = int(bit_buffer.get_bits(uint32(8)))

        i = 0

        self._per_car_pit_window_data = []

        while i < self._num_cars:
            self._per_car_pit_window_data.append(PerCarPitWindowData(bit_buffer))
            i += 1

    @property
    def per_car_pit_window_data(self):
        return self._per_car_pit_window_data
