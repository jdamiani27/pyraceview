from ..models import CarStats
from dataclasses import dataclass
from ..util import BitBuffer


CAR_ID_BITS = 8
STATUS_BITS = 3
TOL_TYPE_BITS = 1
TOL_BITS = 19
EVENT_BITS = 4
SPEED_BITS = 8
THROTTLE_BITS = 7
BRAKE_BITS = 7
RPM_BITS = 12
VERSION1_RESERVED_BITS = 3
TOTAL_BITS_COMMON = (
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
FUEL_BITS = 7
LAP_FRACTION_BITS = 17
STEERING_BITS = 7
VERSION2_RESERVED_BITS = 4
VERSION3_SPEED_BITS = 18
VERSION3_RESERVED_BITS = 10

VERSION1_SIZE_BYTES = (TOTAL_BITS_COMMON + VERSION1_RESERVED_BITS) // 8
VERSION2_SIZE_BYTES = (
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

VERSION3_SIZE_BYTES = (
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


@dataclass
class PerCarRaceStatusData:
    car_id: int
    tol_type: int
    status: CarStats
    time_off_leader: float
    event: int
    speed: float
    throttle: int
    brake: int
    rpm: int
    fuel: int = -1
    lap_fraction: float = -1.0
    steer_angle: int = -1    

    def __init__(self, bit_buffer: BitBuffer, byte_size: int):

        assert (
            byte_size == VERSION1_SIZE_BYTES
            or byte_size == VERSION2_SIZE_BYTES
            or byte_size == VERSION3_SIZE_BYTES
        ), "RaceStatusMessage size error"

        self.car_id = int(bit_buffer.get_bits(CAR_ID_BITS))

        _status = int(bit_buffer.get_bits(STATUS_BITS))

        if _status == CarStats.CAR_STATUS_UNKNOWN:
            self.status = CarStats.CAR_STATUS_PRERACE
        else:
            self.status = CarStats(_status)

        self.tol_type = int(bit_buffer.get_bits(TOL_TYPE_BITS))
        self.time_off_leader = float(bit_buffer.get_bits(TOL_BITS))
        self.event = int(bit_buffer.get_bits(EVENT_BITS))

        if byte_size == VERSION3_SIZE_BYTES:
            self.speed = float(bit_buffer.get_bits(VERSION3_SPEED_BITS) / 1000)
        else:
            self.speed = float(bit_buffer.get_bits(SPEED_BITS))

        self.throttle = int(bit_buffer.get_bits(THROTTLE_BITS))
        self.brake = int(bit_buffer.get_bits(BRAKE_BITS))
        self.rpm = int(bit_buffer.get_bits(RPM_BITS) * 4)

        if byte_size == VERSION1_SIZE_BYTES:
            bit_buffer.get_bits(VERSION1_RESERVED_BITS)
        elif (byte_size == VERSION2_SIZE_BYTES) or (
            byte_size == VERSION3_SIZE_BYTES
        ):
            self.fuel = int(bit_buffer.get_bits(FUEL_BITS))
            self.lap_fraction = float(bit_buffer.get_bits(LAP_FRACTION_BITS) / 100000)
            self.steer_angle = int(bit_buffer.get_bits(STEERING_BITS) - 64)

        if byte_size == VERSION2_SIZE_BYTES:
            bit_buffer.get_bits(VERSION2_RESERVED_BITS)
        elif byte_size == VERSION3_SIZE_BYTES:
            bit_buffer.get_bits(VERSION3_RESERVED_BITS)
