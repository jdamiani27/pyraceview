from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPitWindowData


NUMBER_OF_CAR_BITS = uint32(8)


class MsgPitWindow(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.number_of_cars = int(bit_buffer.get_bits(NUMBER_OF_CAR_BITS))

        self.car_data = []

        for _ in range(self.number_of_cars):
            pit_window_data = PerCarPitWindowData(bit_buffer)
            self.car_data[pit_window_data.car_id] = pit_window_data
