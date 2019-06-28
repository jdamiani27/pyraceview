from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarPointsData


class MsgCupInfo(object):
    CUP_POINTS_LAP_BITS = uint32(10)
    CUP_POINTS_NUM_CAR_BITS = uint32(6)

    def __init__(self, msg_bytes):
        self._per_car_points = [] # PerCarPointsData
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self._lap = int(bit_buffer.get_bits(self.CUP_POINTS_LAP_BITS))
        self._num_cars = int(bit_buffer.get_bits(self.CUP_POINTS_NUM_CAR_BITS))

        i = 0

        while i < self._num_cars:
            self._per_car_points.append(PerCarPointsData(bit_buffer))
            i += 1

    @property
    def per_car_points(self):
        return self._per_car_points

    @property
    def lap(self):
        return self._lap
