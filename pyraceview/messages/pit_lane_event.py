from ..messages import MsgBase
from ..util import ByteArray


class MsgPitLaneEvent(MsgBase):
    def __init__(self, msg_bytes):
        super().__init__(msg_bytes)
        
        byte_array = ByteArray(msg_bytes)
        byte_array.position = 7
        self._car_id = int(byte_array.read_unsigned_byte())
        self._event_id = int(byte_array.read_unsigned_byte())
        byte_array.read_unsigned_byte()

    @property
    def car_id(self):
        return self._car_id

    @property
    def event_id(self):
        return self._event_id
