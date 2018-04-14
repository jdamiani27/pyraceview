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
    HEADING_RESOLUTION = float64(180 / 2**BITS_HEADING - uint32(1))

    _norm_x = float64(-1)
    _norm_y = float64(-1)
    _norm_z = float64(-1)

    def __init__(self, bit_buffer):
        self._car_id = bit_buffer.get_bits(self.BITS_CAR_NUM)
        _loc3_ = uint32(bit_buffer.get_bits(self.BITS_CAR_POS_X))
        _loc4_ = uint32(bit_buffer.get_bits(self.BITS_CAR_POS_Y))
        _loc5_ = uint32(bit_buffer.get_bits(self.BITS_CAR_POS_Z))
        self._pos_x = BitBuffer.make_bits_signed(_loc3_, self.BITS_CAR_POS_X) * self.POS_X_RESOLUTION
        self._pos_y = BitBuffer.make_bits_signed(_loc4_, self.BITS_CAR_POS_Y) * self.POS_Y_RESOLUTION
        self._pos_z = BitBuffer.make_bits_signed(_loc5_, self.BITS_CAR_POS_Z) * self.POS_Z_RESOLUTION
        _loc6_ = float64(bit_buffer.get_bits(self.BITS_ANGLE_ENCODED_NORM_X) * self.NORM_X_RESOLUTION)
        _loc7_ = float64(_loc6_ * (pi / 180))
        _loc8_ = float64(bit_buffer.get_bits(self.BITS_ANGLE_ENCODED_NORM_Y) * self.NORM_Y_RESOLUTION)
        _loc9_ = float64(_loc8_ * (pi / 180))
        self.set_normal(_loc7_, _loc9_)
        _loc10_ = float64(BitBuffer.make_bits_signed(bit_buffer.get_bits(self.BITS_HEADING), self.BITS_HEADING) * self.HEADING_RESOLUTION)
        _loc11_ = float64(_loc10_ * (pi / 180))
        self.set_heading(_loc11_)
        bit_buffer.get_bits(self.RESERVED_BITS)

    def set_normal(self, param1, param2):
        self._norm_x = float64(math.cos(param1))
        self._norm_y = float64(math.cos(param2))
        self._norm_z = float64(math.sqrt(1 - self._norm_x * self._norm_x
                                           - self._norm_y * self._norm_y))
        self._normal = Vector3D()
        self._normal.x = self._norm_x
        self._normal.y = self._norm_y
        self._normal.z = self._norm_z

    def set_heading(self, param1):
        _loc2_ = Vector3D()
        _loc2_.x = math.cos(param1)
        _loc2_.y = math.sin(param1)
        _loc2_.z = 0.

        _loc3_ = Vector3D()
        _loc3_.x = _loc2_.y * self._normal.z - self._normal.y * _loc2_.z
        _loc3_.y = _loc2_.z * self._normal.x - self._normal.z * _loc2_.x
        _loc3_.z = _loc2_.x * self._normal.y - self._normal.x * _loc2_.y
        _loc3_.normalize()

        self._heading = Vector3D()
        self._heading.x = self._normal.y * _loc3_.z - _loc3_.y * self._normal.z
        self._heading.y = self._normal.z * _loc3_.x - _loc3_.z * self._normal.x
        self._heading.z = self._normal.x * _loc3_.y - _loc3_.x * self._normal.y
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
    def normal(self):
        return self._normal

    @property
    def heading(self):
        return self._heading

    def get_position(self, param1):
        param1.x = self.pos_x
        param1.y = self.pos_y
        param1.z = self.pos_z

    def get_normal(self, param1):
        param1.x = self._normal.x
        param1.y = self._normal.y
        param1.z = self._normal.z

    def get_heading(self, param1):
        param1.x = self.heading.x
        param1.y = self.heading.y
        param1.z = self.heading.z
