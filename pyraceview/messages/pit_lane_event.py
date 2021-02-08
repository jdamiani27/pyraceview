from ..messages import MsgBase
from ..util import ByteArray
from dataclasses import dataclass


@dataclass
class MsgPitLaneEvent(MsgBase):
    car_id: int
    event_id: int

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        byte_array = ByteArray(msg_bytes)
        byte_array.position = 7
        self.car_id = int(byte_array.read_unsigned_byte())
        self.event_id = int(byte_array.read_unsigned_byte())
        byte_array.read_unsigned_byte()
