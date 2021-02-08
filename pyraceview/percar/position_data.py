import math
from numpy import uint32, float64, pi
from ..util import BitBuffer, Vector3D
from dataclasses import dataclass


CAR_ID_BITS = uint32(8)
CAR_POS_X_BITS = uint32(18)
CAR_POS_Y_BITS = uint32(18)
CAR_POS_Z_BITS = uint32(15)
ANGLE_ENCODED_NORM_X_BITS = uint32(12)
ANGLE_ENCODED_NORM_Y_BITS = uint32(12)
HEADING_BITS = uint32(12)
RESERVED_BITS = uint32(1)
CAR_SIZE_BITS = uint32(
    CAR_ID_BITS
    + CAR_POS_X_BITS
    + CAR_POS_Y_BITS
    + CAR_POS_Z_BITS
    + ANGLE_ENCODED_NORM_X_BITS
    + ANGLE_ENCODED_NORM_Y_BITS
    + HEADING_BITS
    + RESERVED_BITS
)

POS_X_RESOLUTION = float64(0.1)
POS_Y_RESOLUTION = float64(0.1)
POS_Z_RESOLUTION = float64(0.05)
NORM_X_RESOLUTION = float64(180 / 2 ** ANGLE_ENCODED_NORM_X_BITS)
NORM_Y_RESOLUTION = float64(180 / 2 ** ANGLE_ENCODED_NORM_Y_BITS)
HEADING_RESOLUTION = float64(180 / 2 ** (HEADING_BITS - uint32(1)))


@dataclass
class PerCarPositionData:
    car_id: int
    pos_x: float
    pos_y: float
    pos_z: float
    norm_x: float
    norm_y: float
    norm_z: float
    heading_x: float
    heading_y: float
    heading_z: float

    def __init__(self, bit_buffer: BitBuffer):
        self.car_id = int(bit_buffer.get_bits(CAR_ID_BITS))

        # Read the car position
        pos_x_unsign = uint32(bit_buffer.get_bits(CAR_POS_X_BITS))
        pos_y_unsign = uint32(bit_buffer.get_bits(CAR_POS_Y_BITS))
        pos_z_unsign = uint32(bit_buffer.get_bits(CAR_POS_Z_BITS))
        
        self.pos_x = float(
            BitBuffer.make_bits_signed(pos_x_unsign, CAR_POS_X_BITS)
            * POS_X_RESOLUTION
        )
        self.pos_y = float(
            BitBuffer.make_bits_signed(pos_y_unsign, CAR_POS_Y_BITS)
            * POS_Y_RESOLUTION
        )
        self.pos_z = float(
            BitBuffer.make_bits_signed(pos_z_unsign, CAR_POS_Z_BITS)
            * POS_Z_RESOLUTION
        )

        # Read vector normal to car heading
        angle_x_deg = float(
            bit_buffer.get_bits(ANGLE_ENCODED_NORM_X_BITS) * NORM_X_RESOLUTION
        )
        angle_x_rad = angle_x_deg * (math.pi / 180)
        self.norm_x = math.cos(angle_x_rad)

        angle_y_deg = float(
            bit_buffer.get_bits(ANGLE_ENCODED_NORM_Y_BITS) * NORM_Y_RESOLUTION
        )
        angle_y_rad = angle_y_deg * (math.pi / 180)
        self.norm_y = math.cos(angle_y_rad)

        self.norm_z = math.sqrt(
            1 - self.norm_x * self.norm_x - self.norm_y * self.norm_y
        )

        # Read car heading vector
        heading_angle_deg = float(
            BitBuffer.make_bits_signed(
                bit_buffer.get_bits(HEADING_BITS), HEADING_BITS
            )
            * HEADING_RESOLUTION
        )
        heading_angle_rad = heading_angle_deg * (math.pi / 180)

        _loc2_ = Vector3D()
        _loc2_.x = math.cos(heading_angle_rad)
        _loc2_.y = math.sin(heading_angle_rad)
        _loc2_.z = 0.0

        _loc3_ = Vector3D()
        _loc3_.x = _loc2_.y * self.norm_z - self.norm_y * _loc2_.z
        _loc3_.y = _loc2_.z * self.norm_x - self.norm_z * _loc2_.x
        _loc3_.z = _loc2_.x * self.norm_y - self.norm_x * _loc2_.y
        _loc3_.normalize()

        heading = Vector3D()
        heading.x = self.norm_y * _loc3_.z - _loc3_.y * self.norm_z
        heading.y = self.norm_z * _loc3_.x - _loc3_.z * self.norm_x
        heading.z = self.norm_x * _loc3_.y - _loc3_.x * self.norm_y
        heading.normalize()

        self.heading_x, self.heading_y, self.heading_z = heading.x, heading.y, heading.z

        bit_buffer.get_bits(RESERVED_BITS)
