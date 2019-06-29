import math
from numpy import uint32, float64, pi
from ..util import BitBuffer, Vector3D


class PerCarPositionData(object):

    BITS_CAR_NUM = uint32(8)
    BITS_CAR_POS_X = uint32(18)
    BITS_CAR_POS_Y = uint32(18)
    BITS_CAR_POS_Z = uint32(15)
    BITS_ANGLE_ENCODED_NORM_X = uint32(12)
    BITS_ANGLE_ENCODED_NORM_Y = uint32(12)
    BITS_HEADING = uint32(12)
    RESERVED_BITS = uint32(1)
    CAR_SIZE = uint32(BITS_CAR_NUM + BITS_CAR_POS_X
                                   + BITS_CAR_POS_Y
                                   + BITS_CAR_POS_Z
                                   + BITS_ANGLE_ENCODED_NORM_X
                                   + BITS_ANGLE_ENCODED_NORM_Y
                                   + BITS_HEADING
                                   + RESERVED_BITS)

    POS_X_RESOLUTION = float64(0.1)
    POS_Y_RESOLUTION = float64(0.1)
    POS_Z_RESOLUTION = float64(0.05)
    NORM_X_RESOLUTION = float64(180 / 2**BITS_ANGLE_ENCODED_NORM_X)
    NORM_Y_RESOLUTION = float64(180 / 2**BITS_ANGLE_ENCODED_NORM_Y)
    HEADING_RESOLUTION = float64(180 / 2**(BITS_HEADING - uint32(1)))

    def __init__(self, bit_buffer):
        self._car_id = int(bit_buffer.get_bits(self.BITS_CAR_NUM))

        # Read the car position
        pos_x_unsign = uint32(bit_buffer.get_bits(self.BITS_CAR_POS_X))
        pos_y_unsign = uint32(bit_buffer.get_bits(self.BITS_CAR_POS_Y))
        pos_z_unsign = uint32(bit_buffer.get_bits(self.BITS_CAR_POS_Z))
        self._pos_x = float(BitBuffer.make_bits_signed(pos_x_unsign, self.BITS_CAR_POS_X) * self.POS_X_RESOLUTION)
        self._pos_y = float(BitBuffer.make_bits_signed(pos_y_unsign, self.BITS_CAR_POS_Y) * self.POS_Y_RESOLUTION)
        self._pos_z = float(BitBuffer.make_bits_signed(pos_z_unsign, self.BITS_CAR_POS_Z) * self.POS_Z_RESOLUTION)

        # Read vector normal to car heading
        angle_x_deg = float(bit_buffer.get_bits(self.BITS_ANGLE_ENCODED_NORM_X) * self.NORM_X_RESOLUTION)
        angle_x_rad = angle_x_deg * (math.pi / 180)
        self._norm_x = math.cos(angle_x_rad)

        angle_y_deg = float(bit_buffer.get_bits(self.BITS_ANGLE_ENCODED_NORM_Y) * self.NORM_Y_RESOLUTION)
        angle_y_rad = angle_y_deg * (math.pi / 180)
        self._norm_y = math.cos(angle_y_rad)

        self._norm_z = math.sqrt(1 - self._norm_x * self._norm_x
                                   - self._norm_y * self._norm_y)

        # Read car heading vector
        heading_angle_deg = float(BitBuffer.make_bits_signed(bit_buffer.get_bits(self.BITS_HEADING), self.BITS_HEADING) * self.HEADING_RESOLUTION)
        heading_angle_rad = heading_angle_deg * (math.pi / 180)
        self.set_heading(heading_angle_rad)

        bit_buffer.get_bits(self.RESERVED_BITS)

    def set_heading(self, angle):
        _loc2_ = Vector3D()
        _loc2_.x = math.cos(angle)
        _loc2_.y = math.sin(angle)
        _loc2_.z = 0.

        _loc3_ = Vector3D()
        _loc3_.x = _loc2_.y * self._norm_z - self._norm_y * _loc2_.z
        _loc3_.y = _loc2_.z * self._norm_x - self._norm_z * _loc2_.x
        _loc3_.z = _loc2_.x * self._norm_y - self._norm_x * _loc2_.y
        _loc3_.normalize()

        self._heading = Vector3D()
        self._heading.x = self._norm_y * _loc3_.z - _loc3_.y * self._norm_z
        self._heading.y = self._norm_z * _loc3_.x - _loc3_.z * self._norm_x
        self._heading.z = self._norm_x * _loc3_.y - _loc3_.x * self._norm_y
        self._heading.normalize()

    @property
    def car_id(self):
        return self._car_id

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def pos_z(self):
        return self._pos_z

    @property
    def norm_x(self):
        return self._norm_x

    @property
    def norm_y(self):
        return self._norm_y

    @property
    def norm_z(self):
        return self._norm_z

    @property
    def heading_x(self):
        return float(self._heading.x)

    @property
    def heading_y(self):
        return float(self._heading.y)

    @property
    def heading_z(self):
        return float(self._heading.z)
