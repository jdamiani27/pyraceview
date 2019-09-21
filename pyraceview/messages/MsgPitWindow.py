from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPitWindowData


class MsgPitWindow(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self._num_cars = int(bit_buffer.get_bits(uint32(8)))
        self._per_car_pit_window_data = []

        for _ in range(self._num_cars):
            self._per_car_pit_window_data.append(PerCarPitWindowData(bit_buffer))

    @property
    def per_car_pit_window_data(self):
        return self._per_car_pit_window_data
