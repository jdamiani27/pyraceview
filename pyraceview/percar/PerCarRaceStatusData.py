from numpy import uint32, float64
from ..models import CarStats


BITS_CAR_NUMBER = uint32(8)
BITS_STATUS = uint32(3)
BITS_TOL_TYPE = uint32(1)
BITS_TOL = uint32(19)
BITS_EVENT = uint32(4)
BITS_SPEED = uint32(8)
BITS_THROTTLE = uint32(7)
BITS_BRAKE = uint32(7)
BITS_RPM = uint32(12)
BITS_RESERVED_VERSION1 = uint32(3)
TOTAL_BITS_COMMON = uint32(
    BITS_CAR_NUMBER
    + BITS_STATUS
    + BITS_TOL_TYPE
    + BITS_TOL
    + BITS_EVENT
    + BITS_SPEED
    + BITS_THROTTLE
    + BITS_BRAKE
    + BITS_RPM
)
BITS_FUEL = uint32(7)
BITS_LAP_FRACTION = uint32(17)
BITS_STEERING = uint32(7)
BITS_RESERVED_VERSION2 = uint32(4)
BITS_SPEED_VERSION3 = uint32(18)
BITS_RESERVED_VERSION3 = uint32(10)

VERSION1_SIZE_BYTES = uint32((TOTAL_BITS_COMMON + BITS_RESERVED_VERSION1) // 8)
VERSION2_SIZE_BYTES = uint32(
    (
        TOTAL_BITS_COMMON
        + BITS_RESERVED_VERSION2
        + BITS_FUEL
        + BITS_LAP_FRACTION
        + BITS_STEERING
        + BITS_RESERVED_VERSION2
    )
    // 8
)

VERSION3_SIZE_BYTES = uint32(
    (
        TOTAL_BITS_COMMON
        - BITS_SPEED
        + BITS_SPEED_VERSION3
        + BITS_FUEL
        + BITS_LAP_FRACTION
        + BITS_STEERING
        + BITS_RESERVED_VERSION3
    )
    // 8
)

PIT_IN = float64(8)
PIT_OUT = float64(7)


class PerCarRaceStatusData(object):
    def __init__(self, bit_buffer, byte_size):
        self._is_version_3 = False
        self.fuel = -1
        self.lap_fraction = float(-1)
        self.steer_angle = -1

        assert (
            byte_size == VERSION1_SIZE_BYTES
            or byte_size == VERSION2_SIZE_BYTES
            or byte_size == VERSION3_SIZE_BYTES
        ), "RaceStatusMessage size error"
        self.car_id = int(bit_buffer.get_bits(BITS_CAR_NUMBER))
        self._status = bit_buffer.get_bits(BITS_STATUS)
        self.tol_type = int(bit_buffer.get_bits(BITS_TOL_TYPE))
        self.time_off_leader = float(bit_buffer.get_bits(BITS_TOL))
        self.event = int(bit_buffer.get_bits(BITS_EVENT))

        if byte_size == VERSION3_SIZE_BYTES:
            self._speed = bit_buffer.get_bits(BITS_SPEED_VERSION3)
            self._is_version_3 = True
        else:
            self._speed = bit_buffer.get_bits(BITS_SPEED)

        self.throttle = int(bit_buffer.get_bits(BITS_THROTTLE))
        self.brake = int(bit_buffer.get_bits(BITS_BRAKE))
        self.rpm = int(bit_buffer.get_bits(BITS_RPM) * 4)

        if byte_size == VERSION1_SIZE_BYTES:
            bit_buffer.get_bits(BITS_RESERVED_VERSION1)
        elif (byte_size == VERSION2_SIZE_BYTES) or (byte_size == VERSION3_SIZE_BYTES):
            self.fuel = int(bit_buffer.get_bits(BITS_FUEL))
            self.lap_fraction = float(bit_buffer.get_bits(BITS_LAP_FRACTION) / 100000)
            self.steer_angle = int(bit_buffer.get_bits(BITS_STEERING) - 64)

        if byte_size == VERSION2_SIZE_BYTES:
            bit_buffer.get_bits(BITS_RESERVED_VERSION2)
        elif byte_size == VERSION3_SIZE_BYTES:
            bit_buffer.get_bits(BITS_RESERVED_VERSION3)

    @property
    def status(self):
        if int(self._status) == CarStats.CAR_STATUS_UNKNOWN:
            return CarStats.CAR_STATUS_PRERACE
        else:
            return int(self._status)

    @property
    def speed(self):
        s = float64(self._speed / 1000) if self._is_version_3 else float64(self._speed)
        return float(s)
