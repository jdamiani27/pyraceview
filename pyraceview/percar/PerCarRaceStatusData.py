from numpy import uint32, float64
from ..models import CarStats


CAR_ID_BITS = uint32(8)
STATUS_BITS = uint32(3)
TOL_TYPE_BITS = uint32(1)
TOL_BITS = uint32(19)
EVENT_BITS = uint32(4)
SPEED_BITS = uint32(8)
THROTTLE_BITS = uint32(7)
BRAKE_BITS = uint32(7)
RPM_BITS = uint32(12)
VERSION1_RESERVED_BITS = uint32(3)
TOTAL_BITS_COMMON = uint32(
    CAR_ID_BITS
    + STATUS_BITS
    + TOL_TYPE_BITS
    + TOL_BITS
    + EVENT_BITS
    + SPEED_BITS
    + THROTTLE_BITS
    + BRAKE_BITS
    + RPM_BITS
)
FUEL_BITS = uint32(7)
LAP_FRACTION_BITS = uint32(17)
STEERING_BITS = uint32(7)
VERSION2_RESERVED_BITS = uint32(4)
VERSION3_SPEED_BITS = uint32(18)
VERSION3_RESERVED_BITS = uint32(10)

VERSION1_SIZE_BYTES = uint32((TOTAL_BITS_COMMON + VERSION1_RESERVED_BITS) // 8)
VERSION2_SIZE_BYTES = uint32(
    (
        TOTAL_BITS_COMMON
        + VERSION2_RESERVED_BITS
        + FUEL_BITS
        + LAP_FRACTION_BITS
        + STEERING_BITS
        + VERSION2_RESERVED_BITS
    )
    // 8
)

VERSION3_SIZE_BYTES = uint32(
    (
        TOTAL_BITS_COMMON
        - SPEED_BITS
        + VERSION3_SPEED_BITS
        + FUEL_BITS
        + LAP_FRACTION_BITS
        + STEERING_BITS
        + VERSION3_RESERVED_BITS
    )
    // 8
)


class PerCarRaceStatusData(object):
    def __init__(self, bit_buffer, byte_size):
        self._is_version_3 = False
        self._fuel = -1
        self._lap_fraction = float64(-1)
        self._steer_angle = -1

        assert (
            byte_size == VERSION1_SIZE_BYTES
            or byte_size == VERSION2_SIZE_BYTES
            or byte_size == VERSION3_SIZE_BYTES
        ), "RaceStatusMessage size error"

        self._car_id = bit_buffer.get_bits(CAR_ID_BITS)
        self._status = bit_buffer.get_bits(STATUS_BITS)
        self._tol_type = bit_buffer.get_bits(TOL_TYPE_BITS)
        self._time_off_leader = float64(bit_buffer.get_bits(TOL_BITS))
        self._event = bit_buffer.get_bits(EVENT_BITS)

        if byte_size == VERSION3_SIZE_BYTES:
            self._speed = bit_buffer.get_bits(VERSION3_SPEED_BITS)
            self._is_version_3 = True
        else:
            self._speed = bit_buffer.get_bits(SPEED_BITS)

        self._throttle = bit_buffer.get_bits(THROTTLE_BITS)
        self._brake = bit_buffer.get_bits(BRAKE_BITS)
        self._rpm = bit_buffer.get_bits(RPM_BITS) * 4

        if byte_size == VERSION1_SIZE_BYTES:
            bit_buffer.get_bits(VERSION1_RESERVED_BITS)
        elif (byte_size == VERSION2_SIZE_BYTES) or (
            byte_size == VERSION3_SIZE_BYTES
        ):
            self._fuel = bit_buffer.get_bits(FUEL_BITS)
            self._lap_fraction = bit_buffer.get_bits(LAP_FRACTION_BITS) / 100000
            self._steer_angle = bit_buffer.get_bits(STEERING_BITS) - 64

        if byte_size == VERSION2_SIZE_BYTES:
            bit_buffer.get_bits(VERSION2_RESERVED_BITS)
        elif byte_size == VERSION3_SIZE_BYTES:
            bit_buffer.get_bits(VERSION3_RESERVED_BITS)

    @property
    def car_id(self):
        return int(self._car_id)

    @property
    def status(self):
        if int(self._status) == CarStats.CAR_STATUS_UNKNOWN:
            return CarStats.CAR_STATUS_PRERACE
        else:
            return int(self._status)

    @property
    def tol_type(self):
        return int(self._tol_type)

    @property
    def time_off_leader(self):
        return float(self._time_off_leader)

    @property
    def event(self):
        return int(self._event)

    @property
    def speed(self):
        s = float64(self._speed / 1000) if self._is_version_3 else float64(self._speed)
        return float(s)

    @property
    def throttle(self):
        return int(self._throttle)

    @property
    def brake(self):
        return int(self._brake)

    @property
    def rpm(self):
        return int(self._rpm)

    @property
    def fuel(self):
        return int(self._fuel)

    @property
    def steer_angle(self):
        return int(self._steer_angle)

    @property
    def lap_fraction(self):
        return float(self._lap_fraction)
