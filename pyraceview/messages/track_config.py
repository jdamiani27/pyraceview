from ..messages import MsgBase
from ..util import BitBuffer, ByteArray
from dataclasses import dataclass


ORIGIN_X_BITS = 32
ORIGIN_Y_BITS = 32
ORIGIN_Z_BITS = 32
TRACK_NAME_BITS = 64


@dataclass
class MsgTrackConfig(MsgBase):
    local_origin_x: int
    local_origin_y: int
    local_origin_z: int
    track_name: str

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        byte_array = ByteArray(msg_bytes)
        bit_buffer = BitBuffer(byte_array)
        bit_buffer.set_position(7)
        
        self.local_origin_x = int(bit_buffer.get_bits(ORIGIN_X_BITS))
        self.local_origin_y = int(bit_buffer.get_bits(ORIGIN_Y_BITS))
        self.local_origin_z = int(bit_buffer.get_bits(ORIGIN_Z_BITS))
        self.track_name = byte_array.read_utf_bytes(TRACK_NAME_BITS // 8)
