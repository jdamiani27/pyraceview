from ..util import Endian, ByteArray
from ..percar import PerCarPitStopExtendedData


class MsgPitLaneExtended(object):
    def __init__(self, msg_bytes):
        byte_array = ByteArray(msg_bytes)
        endian = byte_array.endian
        byte_array.position = 7

        byte_array.endian = (
            Endian.LITTLE_ENDIAN if (endian == Endian.BIG_ENDIAN) else Endian.BIG_ENDIAN
        )
        self.timecode = int(byte_array.read_unsigned_int())
        number_of_cars = int(byte_array.read_unsigned_byte())

        if number_of_cars > 1:
            raise ValueError(f"Expected 1 car entry, received {number_of_cars}")

        self.car_id = int(byte_array.read_unsigned_byte())
        number_of_pits = int(byte_array.read_byte())

        if number_of_pits > 1:
            raise ValueError(f"Expected 1 pit entry, received {number_of_pits}")

        self.pit_stop = PerCarPitStopExtendedData(byte_array)

        byte_array.endian = endian
