from ..util import ByteArray


class MsgPitLaneEvent(object):
    def __init__(self, msg_bytes):
        byte_array = ByteArray(msg_bytes)
        byte_array.position = 7
        self.car_id = int(byte_array.read_unsigned_byte())
        self.event_id = int(byte_array.read_unsigned_byte())
        byte_array.read_unsigned_byte()
