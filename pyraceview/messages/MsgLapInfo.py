from numpy import uint32
from ..util import BitBuffer, ByteArray
from ..percar import PerCarLapData


class MsgLapInfo(object):
    LAPINFO_BITS_VITC_TIME = uint32(32)
    LAPINFO_BITS_LAP = uint32(10)
    LAPINFO_BITS_NUM_CARS = uint32(6)
    LAPINFO_BITS_LEAD_CHANGES = uint32(8)
    LAPINFO_BITS_NUM_LEADERS = uint32(6)
    LAPINFO_BITS_NUM_CAUTIONS = uint32(5)
    LAPINFO_BITS_FLAG_LAP = uint32(10)
    LAPINFO_BITS_RESERVED = uint32(3)

    def __init__(self, msg_bytes):
        self.per_car_lap_data = []  # PerCarLapData
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self.vitc_time = int(bit_buffer.get_bits(self.LAPINFO_BITS_VITC_TIME))
        self.lap = int(bit_buffer.get_bits(self.LAPINFO_BITS_LAP))
        self.num_cars = int(bit_buffer.get_bits(self.LAPINFO_BITS_NUM_CARS))
        self.lead_changes = int(bit_buffer.get_bits(self.LAPINFO_BITS_LEAD_CHANGES))
        self.num_leaders = int(bit_buffer.get_bits(self.LAPINFO_BITS_NUM_LEADERS))
        self.num_cautions = int(bit_buffer.get_bits(self.LAPINFO_BITS_NUM_CAUTIONS))
        self.last_flag_change_lap = int(
            bit_buffer.get_bits(self.LAPINFO_BITS_FLAG_LAP)
        )
        bit_buffer.get_bits(self.LAPINFO_BITS_RESERVED)

        for _ in range(self.num_cars):
            self.per_car_lap_data.append(PerCarLapData(bit_buffer))
