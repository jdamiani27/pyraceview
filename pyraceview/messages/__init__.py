from ..util import ByteBuffer
from .header import MsgHeader
from .base import MsgBase
from .car_position import MsgCarPosition
from .car_stats import MsgCarStats
from .cup_info import MsgCupInfo
from .heartbeat import MsgHeartbeat
from .lap_info import MsgLapInfo
from .pit_lane_event import MsgPitLaneEvent
from .pit_lane_extended import MsgPitLaneExtended
from .pit_window import MsgPitWindow
from .race_status import MsgRaceStatus
from .track_config import MsgTrackConfig
from .vitc_to_lap import MsgVitcToLap


_parsers = {
    "a": MsgCarStats,
    "b": MsgPitLaneExtended,
    "d": MsgPitLaneExtended,
    "C": MsgCupInfo,
    "F": MsgPitWindow,
    "H": MsgHeartbeat,
    "l": MsgLapInfo,
    "O": MsgTrackConfig,
    "P": MsgPitLaneEvent,
    "s": MsgRaceStatus,
    "V": MsgVitcToLap,
    "W": MsgCarPosition,
}


class MsgFactory(object):

    HEADER_SIZE = 7

    def __init__(self, source=b""):
        self._buffer = ByteBuffer(source)

    def push_data(self, b):
        self._buffer.write(b)

    def has_message(self):
        available = self._buffer.size()
        if available >= self.HEADER_SIZE:
            header = MsgHeader(self._buffer.peek(self.HEADER_SIZE))
            if header.size + self.HEADER_SIZE <= available:
                return True

        return False

    def get_message(self):
        if self.has_message():
            header = MsgHeader(self._buffer.peek(self.HEADER_SIZE))
            message_parser = _parsers[header.byte_type]
            msg_bytes = self._buffer.read(header.size + self.HEADER_SIZE)
            return message_parser(msg_bytes)

        return None
