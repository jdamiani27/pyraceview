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

    def __init__(self, param1:BitBuffer, param2:uint):
        self._is_version_3 = False
        self._fuel = -1
        self._lap_fraction = float64(-1)
        self._steer_angle = -1

        #Util.ASSERT(param2 == VERSION1_SIZE_BYTES || param2 == VERSION2_SIZE_BYTES || param2 == VERSION3_SIZE_BYTES,"RaceStatusMessage size error")
        self._id = param1.get_bits(self.BITS_CAR_NUMBER)
        self._status = param1.get_bits(self.BITS_STATUS)
        self._tol_type = param1.get_bits(self.BITS_TOL_TYPE)
        self._time_off_leader = float64(param1.get_bits(self.BITS_TOL))
        self._event = param1.get_bits(self.BITS_EVENT)

        if param2 == self.VERSION3_SIZE_BYTES:
            self._speed = param1.get_bits(self.BITS_SPEED_VERSION3)
            self._is_version_3 = True
        else:
            self._speed = param1.get_bits(self.BITS_SPEED)

        self._throttle = param1.get_bits(self.BITS_THROTTLE)
        self._brake = param1.get_bits(self.BITS_BRAKE)
        self._rpm = param1.get_bits(self.BITS_RPM) * 4

        if param2 == self.VERSION1_SIZE_BYTES:
            param1.get_bits(self.BITS_RESERVED_VERSION1)
        elif (param2 == self.VERSION2_SIZE_BYTES) or (param2 == self.VERSION3_SIZE_BYTES):
            self._fuel = param1.get_bits(self.BITS_FUEL)
            self._lap_fraction = param1.get_bits(self.BITS_LAP_FRACTION) / 100000
            self._steer_angle = param1.get_bits(self.BITS_STEERING) - 64

        if param2 == self.VERSION2_SIZE_BYTES:
            param1.get_bits(self.BITS_RESERVED_VERSION2)
        elif param2 == self.VERSION3_SIZE_BYTES:
            param1.get_bits(self.BITS_RESERVED_VERSION3)

    @property
    def id(self):
        return self._id

    @property
    def status(self):
        if self._status == CarStats.CAR_STATUS_UNKNOWN:
            return CarStats.CAR_STATUS_PRERACE
        else:
            return self._status

    @property
    def tol_type(self):
        return self._tol_type

    @property
    def time_off_leader(self):
        return self._time_off_leader

    @property
    def event(self):
        return self._event

    @property
    def speed(self):
        return float64(self._speed / 1000) if _is_version_3 else float64(self._speed)

    @property
    def throttle(self):
        return self._throttle

    @property
    def brake(self):
        return self._brake

    @property
    def rpm(self):
        return self._rpm

    @property
    def fuel(self):
        return self._fuel

    @property
    def steer_angle(self):
        return self._steer_angle

    @property
    def lapFraction(self):
        return self._lapFraction
