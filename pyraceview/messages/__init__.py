from ..util import ByteBuffer
from .MsgCarPosition import MsgCarPosition
from .MsgCarStats import MsgCarStats
from .MsgCupInfo import MsgCupInfo
from .MsgHeader import MsgHeader
from .MsgLapInfo import MsgLapInfo
from .MsgPitLaneEvent import MsgPitLaneEvent
from .MsgPitLaneExtended import MsgPitLaneExtended
from .MsgPitWindow import MsgPitWindow
from .MsgRaceStatus import MsgRaceStatus
from .MsgTrackConfig import MsgTrackConfig
from .MsgVitcToLap import MsgVitcToLap


_parsers = {
    "a": MsgCarStats,
    "b": MsgPitLaneExtended,
    "d": MsgPitLaneExtended,
    "C": MsgCupInfo,
    "F": MsgPitWindow,
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
            msg_bytes = self.buffer.read(header.size + self.HEADER_SIZE)
            return message_parser(msg_bytes)

        return None
