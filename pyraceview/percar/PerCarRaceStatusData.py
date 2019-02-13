from numpy import uint32, float64
from ..models import CarStats


class PerCarRaceStatusData(object):

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
    TOTAL_BITS_COMMON = uint32(BITS_CAR_NUMBER + BITS_STATUS
                                               + BITS_TOL_TYPE
                                               + BITS_TOL
                                               + BITS_EVENT
                                               + BITS_SPEED
                                               + BITS_THROTTLE
                                               + BITS_BRAKE
                                               + BITS_RPM)
    BITS_FUEL = uint32(7)
    BITS_LAP_FRACTION = uint32(17)
    BITS_STEERING = uint32(7)
    BITS_RESERVED_VERSION2 = uint32(4)
    BITS_SPEED_VERSION3 = uint32(18)
    BITS_RESERVED_VERSION3 = uint32(10)

    VERSION1_SIZE_BYTES = uint32((TOTAL_BITS_COMMON + BITS_RESERVED_VERSION1) // 8)
    VERSION2_SIZE_BYTES = uint32((TOTAL_BITS_COMMON + BITS_RESERVED_VERSION2
                                                    + BITS_FUEL
                                                    + BITS_LAP_FRACTION
                                                    + BITS_STEERING
                                                    + BITS_RESERVED_VERSION2) // 8)

    VERSION3_SIZE_BYTES = uint32((TOTAL_BITS_COMMON - BITS_SPEED
                                                    + BITS_SPEED_VERSION3
                                                    + BITS_FUEL
                                                    + BITS_LAP_FRACTION
                                                    + BITS_STEERING
                                                    + BITS_RESERVED_VERSION3) // 8)

    PIT_IN = float64(8)
    PIT_OUT = float64(7)

    def __init__(self, bit_buffer, byte_size):
        self._is_version_3 = False
        self._fuel = -1
        self._lap_fraction = float64(-1)
        self._steer_angle = -1

        assert byte_size == self.VERSION1_SIZE_BYTES or byte_size == self.VERSION2_SIZE_BYTES or byte_size == self.VERSION3_SIZE_BYTES, "RaceStatusMessage size error"
        self._id = bit_buffer.get_bits(self.BITS_CAR_NUMBER)
        self._status = bit_buffer.get_bits(self.BITS_STATUS)
        self._tol_type = bit_buffer.get_bits(self.BITS_TOL_TYPE)
        self._time_off_leader = float64(bit_buffer.get_bits(self.BITS_TOL))
        self._event = bit_buffer.get_bits(self.BITS_EVENT)

        if byte_size == self.VERSION3_SIZE_BYTES:
            self._speed = bit_buffer.get_bits(self.BITS_SPEED_VERSION3)
            self._is_version_3 = True
        else:
            self._speed = bit_buffer.get_bits(self.BITS_SPEED)

        self._throttle = bit_buffer.get_bits(self.BITS_THROTTLE)
        self._brake = bit_buffer.get_bits(self.BITS_BRAKE)
        self._rpm = bit_buffer.get_bits(self.BITS_RPM) * 4

        if byte_size == self.VERSION1_SIZE_BYTES:
            bit_buffer.get_bits(self.BITS_RESERVED_VERSION1)
        elif (byte_size == self.VERSION2_SIZE_BYTES) or (byte_size == self.VERSION3_SIZE_BYTES):
            self._fuel = bit_buffer.get_bits(self.BITS_FUEL)
            self._lap_fraction = bit_buffer.get_bits(self.BITS_LAP_FRACTION) / 100000
            self._steer_angle = bit_buffer.get_bits(self.BITS_STEERING) - 64

        if byte_size == self.VERSION2_SIZE_BYTES:
            bit_buffer.get_bits(self.BITS_RESERVED_VERSION2)
        elif byte_size == self.VERSION3_SIZE_BYTES:
            bit_buffer.get_bits(self.BITS_RESERVED_VERSION3)

    @property
    def car_id(self):
        return int(self._id)

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
