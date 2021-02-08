from ..messages import MsgBase
from ..util import Endian, ByteArray
from ..percar import PerCarPitStopExtendedData
from dataclasses import dataclass


@dataclass
class MsgPitLaneExtended(MsgBase):
    timecode: int
    car_id: int
    pit_stop: PerCarPitStopExtendedData

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        byte_array = ByteArray(msg_bytes)
        endian = byte_array.endian
        byte_array.position = 7

        byte_array.endian = (
            Endian.LITTLE_ENDIAN if (endian == Endian.BIG_ENDIAN) else Endian.BIG_ENDIAN
        )
        self.timecode = int(byte_array.read_unsigned_int())
        num_cars = int(byte_array.read_unsigned_byte())

        if num_cars > 1:
            raise ValueError(f"Expected 1 car entry, received {num_cars}")

        self.car_id = int(byte_array.read_unsigned_byte())
        num_pits = int(byte_array.read_byte())

        if num_pits > 1:
            raise ValueError(f"Expected 1 pit entry, received {num_pits}")

        self.pit_stop = PerCarPitStopExtendedData(byte_array)

        byte_array.endian = endian
