from numpy import uint32
from ..util import BitBuffer, ByteArray


class MsgTrackConfig(object):
    TRACKCONFIG_BITS_ORIGIN_X = uint32(32)
    TRACKCONFIG_BITS_ORIGIN_Y = uint32(32)
    TRACKCONFIG_BITS_ORIGIN_Z = uint32(32)
    TRACKCONFIG_BITS_TRACK_NAME = uint32(64)

    def __init__(self, msg_bytes):
        byte_array = ByteArray(msg_bytes)
        bit_buffer = BitBuffer(byte_array)
        bit_buffer.set_position(7)
        self._local_origin_x = int(bit_buffer.get_bits(self.TRACKCONFIG_BITS_ORIGIN_X))
        self._local_origin_y = int(bit_buffer.get_bits(self.TRACKCONFIG_BITS_ORIGIN_Y))
        self._local_origin_z = int(bit_buffer.get_bits(self.TRACKCONFIG_BITS_ORIGIN_Z))
        self._track_name = byte_array.read_utf_bytes(self.TRACKCONFIG_BITS_TRACK_NAME // uint32(8))

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
