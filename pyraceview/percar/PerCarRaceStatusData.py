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
TOTAL_COMMON_BITS = uint32(
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

VERSION1_SIZE_BYTES = uint32((TOTAL_COMMON_BITS + VERSION1_RESERVED_BITS) // 8)
VERSION2_SIZE_BYTES = uint32(
    (
        TOTAL_COMMON_BITS
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
        TOTAL_COMMON_BITS
        - SPEED_BITS
        + VERSION3_SPEED_BITS
        + FUEL_BITS
        + LAP_FRACTION_BITS
        + STEERING_BITS
        + VERSION3_RESERVED_BITS
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
        
        self.car_id = int(bit_buffer.get_bits(CAR_ID_BITS))
        self._status = bit_buffer.get_bits(STATUS_BITS)
        self.tol_type = int(bit_buffer.get_bits(TOL_TYPE_BITS))
        self.time_off_leader = float(bit_buffer.get_bits(TOL_BITS))
        self.event = int(bit_buffer.get_bits(EVENT_BITS))

        if byte_size == VERSION3_SIZE_BYTES:
            self._speed = bit_buffer.get_bits(VERSION3_SPEED_BITS)
            self._is_version_3 = True
        else:
            self._speed = bit_buffer.get_bits(SPEED_BITS)

        self.throttle = int(bit_buffer.get_bits(THROTTLE_BITS))
        self.brake = int(bit_buffer.get_bits(BRAKE_BITS))
        self.rpm = int(bit_buffer.get_bits(RPM_BITS) * 4)

        if byte_size == VERSION1_SIZE_BYTES:
            bit_buffer.get_bits(VERSION1_RESERVED_BITS)
        elif (byte_size == VERSION2_SIZE_BYTES) or (byte_size == VERSION3_SIZE_BYTES):
            self.fuel = int(bit_buffer.get_bits(FUEL_BITS))
            self.lap_fraction = float(bit_buffer.get_bits(LAP_FRACTION_BITS) / 100000)
            self.steer_angle = int(bit_buffer.get_bits(STEERING_BITS) - 64)

        if byte_size == VERSION2_SIZE_BYTES:
            bit_buffer.get_bits(VERSION2_RESERVED_BITS)
        elif byte_size == VERSION3_SIZE_BYTES:
            bit_buffer.get_bits(VERSION3_RESERVED_BITS)

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
