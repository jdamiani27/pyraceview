from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPitWindowData


class MsgPitWindow(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self.num_cars = int(bit_buffer.get_bits(uint32(8)))
        self.per_car_pit_window_data = []

        for _ in range(self.num_cars):
            self.per_car_pit_window_data.append(PerCarPitWindowData(bit_buffer))
