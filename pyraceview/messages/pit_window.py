from numpy import uint32
from ..messages import MsgBase
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPitWindowData


NUM_CARS_BITS = uint32(8)


class MsgPitWindow(MsgBase):
    def __init__(self, msg_bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self._num_cars = int(bit_buffer.get_bits(NUM_CARS_BITS))
        self._car_data = []

        for _ in range(self._num_cars):
            self._car_data.append(PerCarPitWindowData(bit_buffer))

    @property
    def car_data(self):
        return self._car_data

    @property
    def num_cars(self):
        return self._num_cars
