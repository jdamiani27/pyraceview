from numpy import uint32
from ..messages import MsgBase
from ..util import BitBuffer, ByteArray


ORIGIN_X_BITS = uint32(32)
ORIGIN_Y_BITS = uint32(32)
ORIGIN_Z_BITS = uint32(32)
TRACK_NAME_BITS = uint32(64)


class MsgTrackConfig(MsgBase):
    def __init__(self, msg_bytes):
        super().__init__(msg_bytes)
        
        byte_array = ByteArray(msg_bytes)
        bit_buffer = BitBuffer(byte_array)
        bit_buffer.set_position(7)
        
        self._local_origin_x = int(bit_buffer.get_bits(ORIGIN_X_BITS))
        self._local_origin_y = int(bit_buffer.get_bits(ORIGIN_Y_BITS))
        self._local_origin_z = int(bit_buffer.get_bits(ORIGIN_Z_BITS))
        self._track_name = byte_array.read_utf_bytes(
            TRACK_NAME_BITS // uint32(8)
        )

    @property
    def local_origin_x(self):
        return self._local_origin_x

    @property
    def local_origin_y(self):
        return self._local_origin_y

    @property
    def local_origin_z(self):
        return self._local_origin_z

    @property
    def track_name(self):
        return self._track_name
