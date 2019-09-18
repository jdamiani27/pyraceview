from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPointsData


CUP_POINTS_LAP_BITS = uint32(10)
CUP_POINTS_NUM_CAR_BITS = uint32(6)


class MsgCupInfo(object):
    def __init__(self, msg_bytes):
        self.per_car_points = []  # PerCarPointsData
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self.lap = int(bit_buffer.get_bits(CUP_POINTS_LAP_BITS))
        self.num_cars = int(bit_buffer.get_bits(CUP_POINTS_NUM_CAR_BITS))

        for _ in range(self.num_cars):
            self.per_car_points.append(PerCarPointsData(bit_buffer))
